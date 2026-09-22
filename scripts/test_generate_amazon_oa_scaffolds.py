"""Unit tests for the Amazon OA bank extractor and FastPrep page parser.

The fixtures under scripts/fixtures/ are trimmed copies of the cached bank
pages (Tech-OA-Interview-Questions) and one synthetic FastPrep problem page
shaped like the real server-rendered HTML. Run with:

    uv run --project practice python -m pytest scripts/
"""

import ast
import json
import re
from pathlib import Path

import pytest

import generate_amazon_oa_scaffolds as gen

SCRIPTS_DIR = Path(__file__).resolve().parent
FIXTURES_DIR = SCRIPTS_DIR / "fixtures"

BANK_PAGE = (FIXTURES_DIR / "bank_coding.md").read_text(encoding="utf-8")
BANK_PAGE_2 = (FIXTURES_DIR / "bank_coding_page_2.md").read_text(encoding="utf-8")
FASTPREP_PAGE = (FIXTURES_DIR / "fastprep_problem.html").read_text(encoding="utf-8")

REAL_BANK_PAGES = [
    Path("/tmp/opencode/tech-oa/coding.md"),
    Path("/tmp/opencode/tech-oa/coding-page-2.md"),
]


# ---------------------------------------------------------------------------
# Bank row extraction
# ---------------------------------------------------------------------------


def test_parse_bank_rows_extracts_every_table_row():
    rows = gen.parse_bank_rows(BANK_PAGE)
    assert len(rows) == 6
    first = rows[0]
    assert first["companies"] == ["Stripe"]
    assert first["title"] == "Incident Monitor"
    assert first["slug"] == "stripe-incident-monitor"
    assert first["url"] == "https://www.fastprep.io/problems/stripe-incident-monitor"


def test_parse_bank_rows_normalizes_updated_date_stripping_emoji():
    rows = gen.parse_bank_rows(BANK_PAGE)
    assert rows[0]["updated"] == "2026-09-19"
    assert rows[4]["updated"] == "2026-09-17"
    assert rows[5]["updated"] == "2020-08-27"


def test_parse_bank_rows_splits_multi_company_cell():
    rows = gen.parse_bank_rows(BANK_PAGE)
    assert rows[4]["companies"] == ["Amazon", "Google"]


def test_parse_bank_rows_ignores_non_table_lines():
    rows = gen.parse_bank_rows(BANK_PAGE)
    # Header, alignment row, title, and link lines produce no rows.
    assert all(row["slug"] for row in rows)


# ---------------------------------------------------------------------------
# Manifest building: Amazon filter, dedup, recency ordering
# ---------------------------------------------------------------------------


def test_build_manifest_keeps_only_amazon_tagged_rows():
    manifest = gen.build_manifest([BANK_PAGE, BANK_PAGE_2])
    assert {entry["slug"] for entry in manifest} == {
        "amazon-maximize-adjacent-difference-with-one-reversal",
        "amazon-inventory-allocation",
        "amazon-lru-query-result-cache",
        "amazon-currency-conversion-rate",
    }


def test_build_manifest_dedups_by_slug_keeping_most_recent():
    manifest = gen.build_manifest([BANK_PAGE, BANK_PAGE_2])
    entries = [e for e in manifest if e["slug"].endswith("one-reversal")]
    assert len(entries) == 1
    assert entries[0]["updated"] == "2026-09-19"


def test_build_manifest_sorts_most_recent_first():
    manifest = gen.build_manifest([BANK_PAGE, BANK_PAGE_2])
    updated = [entry["updated"] for entry in manifest]
    assert updated == sorted(updated, reverse=True)


def test_build_manifest_breaks_date_ties_by_slug_ascending():
    page = (
        "| Company | OA / Interview Question | Practice | Updated |\n"
        "| :-- | :-- | :-: | :-- |\n"
        "|**Amazon**|[Zeta Task](https://www.fastprep.io/problems/amazon-zeta-task)|[![Practice][p]](https://www.fastprep.io/problems/amazon-zeta-task)|Sep 19, 2026|\n"
        "|**Amazon**|[Alpha Task](https://www.fastprep.io/problems/amazon-alpha-task)|[![Practice][p]](https://www.fastprep.io/problems/amazon-alpha-task)|Sep 19, 2026|\n"
    )
    manifest = gen.build_manifest([page])
    assert [entry["slug"] for entry in manifest] == [
        "amazon-alpha-task",
        "amazon-zeta-task",
    ]


def test_build_manifest_entries_carry_required_fields():
    manifest = gen.build_manifest([BANK_PAGE])
    entry = next(e for e in manifest if e["slug"] == "amazon-lru-query-result-cache")
    assert entry["title"] == "LRU Cache for Query Results"
    assert entry["companies"] == ["Amazon", "Google"]
    assert entry["updated"] == "2026-09-17"
    assert entry["url"].startswith("https://www.fastprep.io/problems/")


@pytest.mark.skipif(
    not all(path.exists() for path in REAL_BANK_PAGES),
    reason="cached bank pages not present (offline fixture-only run)",
)
def test_real_bank_pages_yield_350_unique_amazon_entries():
    texts = [path.read_text(encoding="utf-8") for path in REAL_BANK_PAGES]
    manifest = gen.build_manifest(texts)
    assert len(manifest) == 350
    slugs = [entry["slug"] for entry in manifest]
    assert len(set(slugs)) == 350
    updated = [entry["updated"] for entry in manifest]
    assert updated == sorted(updated, reverse=True)


# ---------------------------------------------------------------------------
# FastPrep page parsing
# ---------------------------------------------------------------------------


def test_extract_problem_record_reassembles_next_flight_payloads():
    problem = gen.extract_problem_record(FASTPREP_PAGE)
    assert problem is not None
    assert problem["id"] == "amazon-maximize-adjacent-difference-with-one-reversal"
    assert problem["title"] == "Maximize Adjacent Difference With One Reversal"
    assert problem["difficulty"] == "hard"
    assert problem["functionName"] == "solve"


def test_extract_problem_record_returns_none_without_flight_data():
    assert gen.extract_problem_record("<html><body>no data</body></html>") is None


# ---------------------------------------------------------------------------
# Example-to-cases conversion (the cases contract)
# ---------------------------------------------------------------------------


def test_cases_from_record_parses_json_representable_example():
    problem = gen.extract_problem_record(FASTPREP_PAGE)
    result = gen.cases_from_record(problem)
    assert result.function_name == "solve"
    assert result.skip_reason is None
    assert result.cases == [
        {"id": "example_1", "args": [[2, 3, 1, 5, 4]], "expected": 10}
    ]


def test_cases_from_record_parses_quoted_string_inputs():
    problem = dict(
        gen.extract_problem_record(FASTPREP_PAGE),
        functionName="minLength",
        examples=[
            {
                "id": 2,
                "inputText": [
                    {"inputName": "s", "inputValue": "'abcabc'", "inputType": "string"},
                ],
                "outputText": "3",
                "outputType": "int",
            }
        ],
    )
    result = gen.cases_from_record(problem)
    assert result.cases == [{"id": "example_2", "args": ["abcabc"], "expected": 3}]


def test_cases_from_record_skips_tree_typed_inputs_naming_the_slug():
    problem = dict(
        gen.extract_problem_record(FASTPREP_PAGE),
        id="amazon-some-tree-problem",
        examples=[
            {
                "id": 1,
                "inputText": [
                    {"inputName": "root", "inputValue": "[1,2,3]", "inputType": "TreeNode"}
                ],
                "outputText": "2",
                "outputType": "int",
            }
        ],
    )
    result = gen.cases_from_record(problem)
    assert result.cases == []
    assert "amazon-some-tree-problem" in result.skip_reason


def test_cases_from_record_skips_unparseable_output_naming_the_slug():
    problem = dict(
        gen.extract_problem_record(FASTPREP_PAGE),
        id="amazon-prose-output",
        examples=[
            {
                "id": 1,
                "inputText": [
                    {"inputName": "n", "inputValue": "5", "inputType": "int"}
                ],
                "outputText": "any valid ordering is accepted",
                "outputType": "string",
            }
        ],
    )
    result = gen.cases_from_record(problem)
    assert result.cases == []
    assert "amazon-prose-output" in result.skip_reason


def test_cases_from_record_skips_design_operation_sequences():
    problem = dict(
        gen.extract_problem_record(FASTPREP_PAGE),
        id="amazon-lru-query-result-cache",
        examples=[
            {
                "id": 1,
                "inputText": [
                    {"inputName": "operations", "inputValue": '["LRUCache","put"]', "inputType": "string[]"},
                    {"inputName": "arguments", "inputValue": "[[2],[1,1]]", "inputType": "integer[][]"},
                ],
                "outputText": "[null,null]",
                "outputType": "long[]",
            }
        ],
    )
    result = gen.cases_from_record(problem)
    assert result.cases == []
    assert "amazon-lru-query-result-cache" in result.skip_reason


def test_cases_from_record_accepts_level_order_tree_output():
    problem = dict(
        gen.extract_problem_record(FASTPREP_PAGE),
        id="amazon-tree-output",
        examples=[
            {
                "id": 1,
                "inputText": [
                    {"inputName": "levelOrder", "inputValue": "[3,9,20]", "inputType": "int[]"},
                    {"inputName": "inorder", "inputValue": "[9,3,20]", "inputType": "int[]"},
                ],
                "outputText": "[3,9,20,null,null,15,7]",
                "outputType": "TreeNode",
            }
        ],
    )
    result = gen.cases_from_record(problem)
    assert result.cases == [
        {"id": "example_1", "args": [[3, 9, 20], [9, 3, 20]], "expected": [3, 9, 20, None, None, 15, 7]}
    ]


def test_cases_from_record_skips_examples_with_no_inputs():
    problem = dict(
        gen.extract_problem_record(FASTPREP_PAGE),
        id="amazon-no-input-example",
        examples=[
            {"id": 1, "inputText": [], "outputText": "1", "outputType": "int"}
        ],
    )
    result = gen.cases_from_record(problem)
    assert result.cases == []
    assert "amazon-no-input-example" in result.skip_reason


# ---------------------------------------------------------------------------
# Scaffold rendering (structural conventions)
# ---------------------------------------------------------------------------


def test_render_writeup_follows_template_section_order():
    problem = gen.extract_problem_record(FASTPREP_PAGE)
    entry = {"slug": problem["id"], "title": problem["title"], "url": "https://x", "companies": ["Amazon"], "updated": "2026-09-19"}
    text = gen.render_writeup(entry, problem)
    headings = re.findall(r"^#+ .*$", text, flags=re.M)
    assert headings[0].startswith("# [")
    assert "## Examples" in headings
    assert "## Constraints" in headings
    assert headings.index("## Examples") < headings.index("## Constraints")
    assert "## Solutions" in headings
    assert "solutions branch" in text


def test_render_writeup_uses_placeholder_metadata_when_absent():
    problem = dict(gen.extract_problem_record(FASTPREP_PAGE), difficulty=None, topics=[])
    entry = {"slug": problem["id"], "title": problem["title"], "url": "https://x", "companies": ["Amazon"], "updated": "2026-09-19"}
    text = gen.render_writeup(entry, problem)
    assert "unknown difficulty" in text


def test_emit_scaffolds_tolerates_unparseable_pages(tmp_path, monkeypatch):
    docs_dir = tmp_path / "docs" / "problems" / "amazon_oa"
    practice_dir = tmp_path / "practice" / "amazon_oa"
    monkeypatch.setattr(gen, "DOCS_DIR", docs_dir)
    monkeypatch.setattr(gen, "PRACTICE_DIR", practice_dir)
    monkeypatch.setattr(
        gen,
        "fetch_problem_page",
        lambda slug, cache_dir=None, delay=True, network=True: "<html>no payload</html>",
    )
    entry = {"slug": "amazon-gone", "title": "Gone", "url": "https://x/gone", "companies": ["Amazon"], "updated": "2026-09-19"}
    stats = gen.emit_scaffolds([entry], fetch=False)
    assert stats["generated"] == 1
    assert stats["parse_failures"] == ["amazon-gone"]
    assert stats["cases_empty"] == 1
    writeup = (docs_dir / "amazon-gone.md").read_text(encoding="utf-8")
    assert "Statement not parseable" in writeup
    test_text = (practice_dir / "amazon-gone" / "test_amazon-gone.py").read_text(encoding="utf-8")
    assert "amazon-gone" in test_text
    assert json.loads((practice_dir / "amazon-gone" / "cases.json").read_text()) == []


def test_fetch_problem_page_without_network_never_leaves_the_cache(tmp_path):
    slug = "amazon-cached"
    cache_dir = tmp_path / "cache"
    cache_dir.mkdir()
    (cache_dir / f"{slug}.html").write_text("<html>cached</html>", encoding="utf-8")
    assert gen.fetch_problem_page(slug, cache_dir=cache_dir, network=False) == "<html>cached</html>"
    missed = gen.fetch_problem_page("amazon-never-fetched", cache_dir=cache_dir, network=False)
    assert "amazon-never-fetched" in missed
    assert not (cache_dir / "amazon-never-fetched.html").exists()


def test_render_test_skips_empty_cases_naming_the_slug():
    entry = {"slug": "amazon-empty-cases", "title": "T", "url": "https://x", "companies": ["Amazon"], "updated": "2026-09-19"}
    text = gen.render_test(entry, function_name="solve", cases=[], skip_reason="no parseable examples for amazon-empty-cases")
    assert "pytest.skip" in text
    assert "amazon-empty-cases" in text
    assert "len(CASES) == 0" in text


def test_render_test_parametrizes_when_cases_exist():
    entry = {"slug": "amazon-has-cases", "title": "T", "url": "https://x", "companies": ["Amazon"], "updated": "2026-09-19"}
    cases = [{"id": "example_1", "args": [[1]], "expected": 1}]
    text = gen.render_test(entry, function_name="solve", cases=cases, skip_reason=None)
    assert "@pytest.mark.parametrize" in text
    assert ".solve" in text


def test_render_test_embeds_python_literals_not_json():
    cases = [{"id": "example_1", "args": [[3, 9, 20]], "expected": [3, 9, 20, None, None, 15, 7]}]
    text = gen.render_test(
        entry={"slug": "amazon-tree-out", "title": "T", "url": "https://x", "companies": ["Amazon"], "updated": "2026-09-19"},
        function_name="solve",
        cases=cases,
        skip_reason=None,
    )
    module = ast.parse(text)
    cases_node = next(
        node.value
        for node in module.body
        if isinstance(node, ast.Assign) and getattr(node.targets[0], "id", "") == "CASES"
    )
    embedded = ast.literal_eval(cases_node)
    assert embedded == cases
