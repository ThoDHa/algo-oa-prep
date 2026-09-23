"""Unit tests for the docs/index.md table generator.

The generator merges scripts/grind75_table.json (the 77 hand-maintained
Grind 75 rows) with scripts/neetcode150_manifest.json into one unified
LeetCode table, renders the Amazon OA bank table separately, and credits
the list sources. Run with:

    cd practice && uv run pytest ../scripts/
"""

import datetime
import json
from pathlib import Path

import pytest

import generate_index_tables as gen

SCRIPTS_DIR = Path(__file__).resolve().parent
GRIND_TABLE_PATH = SCRIPTS_DIR / "grind75_table.json"
NEETCODE_MANIFEST_PATH = SCRIPTS_DIR / "neetcode150_manifest.json"
AMAZON_MANIFEST_PATH = SCRIPTS_DIR / "amazon_oa_manifest.json"


# ---------------------------------------------------------------------------
# Test fixtures: small synthetic manifests shaped like the committed ones
# ---------------------------------------------------------------------------


def fixture_grind():
    return [
        {
            "number": 1,
            "slug": "two-sum",
            "title": "Two Sum",
            "difficulty": "Easy",
            "category": "Array, Hash Table",
            "time": "15 minutes",
        },
        {
            "number": 2,
            "slug": "min-stack",
            "title": "Minimum Stack",
            "difficulty": "Medium",
            "category": "Stack",
            "time": "20 minutes",
        },
        {
            "number": None,
            "slug": "flood-fill",
            "title": "Flood Fill",
            "difficulty": "Easy",
            "category": "Graph, DFS",
            "time": "20 minutes",
        },
    ]


def fixture_neetcode():
    return [
        {
            "order": 1,
            "section": "Arrays & Hashing",
            "title": "Two Sum (NeetCode)",
            "lcSlug": "two-sum",
            "dirSlug": "two_sum",
            "difficulty": "Easy",
        },
        {
            "order": 2,
            "section": "Stack",
            "title": "Min Stack (NeetCode)",
            "lcSlug": "min-stack",
            "dirSlug": "min_stack",
            "difficulty": "Medium",
        },
        {
            "order": 7,
            "section": "Greedy",
            "title": "Jump Game",
            "lcSlug": "jump-game",
            "dirSlug": "jump_game",
            "difficulty": "Medium",
        },
    ]


def fixture_amazon():
    return [
        {
            "slug": "amazon-maximize-adjacent-difference-with-one-reversal",
            "title": "Maximize Adjacent Difference With One Reversal",
            "url": "https://www.fastprep.io/problems/amazon-maximize-adjacent-difference-with-one-reversal",
            "companies": ["Amazon"],
            "updated": "2026-09-19",
            "parse_status": "parsed-with-cases",
        },
        {
            "slug": "amazon-first-non-repeating-character",
            "title": "First Non-Repeating Character",
            "url": "https://www.fastprep.io/problems/amazon-first-non-repeating-character",
            "companies": ["Amazon"],
            "updated": "2026-09-18",
            "parse_status": "parsed-with-cases",
        },
    ]


EXPECTED_AMAZON_OVERLAP_LC_SLUGS = frozenset(
    {
        "cheapest-flights-within-k-stops",
        "container-with-most-water",
        "course-schedule",
        "course-schedule-ii",
        "find-median-from-data-stream",
        "group-anagrams",
        "interleaving-string",
        "longest-substring-without-repeating-characters",
        "meeting-rooms-ii",
        "merge-intervals",
        "merge-k-sorted-lists",
        "minimum-window-substring",
        "sliding-window-maximum",
        "task-scheduler",
        "trapping-rain-water",
        "word-break",
        "word-search-ii",
    }
)


def write_json(tmp_path, name, payload):
    path = tmp_path / name
    path.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    return path


def valid_grind(count=gen.GRIND_ROW_COUNT):
    """A synthetic Grind table of the contract size: 75 numbered, 2 extras."""
    assert count == gen.GRIND_ROW_COUNT
    numbered = [
        {
            "number": n,
            "slug": f"problem-{n}",
            "title": f"Problem {n}",
            "difficulty": "Easy",
            "category": "Category",
            "time": f"{n} minutes",
        }
        for n in range(1, gen.NUMBERED_GRIND_COUNT + 1)
    ]
    extras = [
        {
            "number": None,
            "slug": f"extra-{n}",
            "title": f"Extra {n}",
            "difficulty": "-",
            "category": "-",
            "time": "-",
        }
        for n in (1, 2)
    ]
    return numbered + extras


def valid_neetcode(count=gen.NEETCODE_TRACK_SIZE):
    """A synthetic NeetCode manifest of the contract size."""
    return [
        {
            "order": n,
            "section": "Arrays & Hashing",
            "title": f"Track Problem {n}",
            "lcSlug": f"track-problem-{n}",
            "dirSlug": f"track_problem_{n}",
            "difficulty": "Easy",
        }
        for n in range(1, count + 1)
    ]


def valid_amazon(count=gen.AMAZON_ROW_COUNT):
    """A synthetic Amazon manifest of the contract size, most-recent first."""
    return [
        {
            "slug": f"amazon-problem-{n}",
            "title": f"Amazon Problem {n}",
            "url": f"https://www.fastprep.io/problems/amazon-problem-{n}",
            "companies": ["Amazon"],
            "updated": (datetime.date(2020, 1, 1) + datetime.timedelta(days=n)).isoformat(),
            "parse_status": "parsed-with-cases",
        }
        for n in range(count, 0, -1)
    ]


def amazon_entry_for(lc_slug):
    """A synthetic Amazon OA entry whose slug mirrors a LeetCode slug."""
    return {
        "slug": f"{gen.AMAZON_SLUG_PREFIX}{lc_slug}",
        "title": f"Amazon {lc_slug}",
        "url": f"https://www.fastprep.io/problems/{gen.AMAZON_SLUG_PREFIX}{lc_slug}",
        "companies": ["Amazon"],
        "updated": "2026-09-17",
        "parse_status": "parsed-with-cases",
    }


def render_fixture_section(amazon=None):
    """Render the unified section for the synthetic fixtures.

    Args:
        amazon: Amazon manifest override (default: fixture_amazon(), which
            matches nothing on the synthetic track).

    Returns:
        The rendered unified section text.
    """
    neetcode = fixture_neetcode()
    amazon = fixture_amazon() if amazon is None else amazon
    rows = gen.merge_tracks(fixture_grind(), neetcode)
    overlap = gen.amazon_overlap_lc_slugs(neetcode, amazon)
    return gen.render_unified_section(rows, overlap)


def unified_table_rows(section):
    """Extract the table row lines (excluding the header) from a section."""
    return [
        line
        for line in section.splitlines()
        if line.startswith("| ") and not line.startswith("| #")
    ]


def row_number(line):
    """Parse the continuous row number from a table row line."""
    return int(line.split("|")[1].strip())


def unified_row_lc_slug(line):
    """Parse the LeetCode slug from a row's Problem cell link.

    Write-up paths use the dirSlug form (underscores); the overlap set
    speaks lcSlug (hyphens), so the slug converts back per the repo-wide
    dirSlug = lcSlug.replace("-", "_") convention.
    """
    problem_cell = line.split("|")[2].strip()
    url = problem_cell[problem_cell.index("(") + 1 : problem_cell.index(")")]
    return url.rstrip("/").rsplit("/", 1)[1].removesuffix(".md").replace("_", "-")


# ---------------------------------------------------------------------------
# The committed data sources satisfy their contracts
# ---------------------------------------------------------------------------


def test_committed_grind_table_passes_validation():
    gen.validate_grind_table(gen.load_grind_table(GRIND_TABLE_PATH))


def test_committed_grind_table_carries_77_rows_numbered_1_to_75():
    rows = gen.load_grind_table(GRIND_TABLE_PATH)
    assert len(rows) == gen.GRIND_ROW_COUNT
    numbered = [row["number"] for row in rows if row["number"] is not None]
    assert numbered == list(range(1, 76))


def test_committed_grind_table_rows_match_the_hand_table_verbatim():
    rows = gen.load_grind_table(GRIND_TABLE_PATH)
    assert rows[0] == {
        "number": 1,
        "slug": "two-sum",
        "title": "Two Sum",
        "difficulty": "Easy",
        "category": "Array, Hash Table",
        "time": "15 minutes",
    }
    assert rows[37] == {
        "number": 38,
        "slug": "min-stack",
        "title": "Minimum Stack",
        "difficulty": "Medium",
        "category": "Stack",
        "time": "20 minutes",
    }
    assert rows[-1] == {
        "number": None,
        "slug": "maximum-frequency-stack",
        "title": "Maximum Frequency Stack",
        "difficulty": "-",
        "category": "-",
        "time": "-",
    }


def test_committed_grind_table_slugs_derive_their_writeup_paths():
    docs_problems = SCRIPTS_DIR.parent / "docs" / "problems"
    for row in gen.load_grind_table(GRIND_TABLE_PATH):
        writeup = docs_problems / (row["slug"].replace("-", "_") + ".md")
        assert writeup.exists(), writeup


def test_committed_neetcode_manifest_passes_merge_validation():
    gen.validate_neetcode_manifest(gen.load_neetcode_manifest(NEETCODE_MANIFEST_PATH))


def test_committed_amazon_manifest_passes_validation():
    gen.validate_amazon_manifest(gen.load_amazon_manifest(AMAZON_MANIFEST_PATH))


# ---------------------------------------------------------------------------
# Loader validation errors
# ---------------------------------------------------------------------------


def test_load_grind_table_rejects_a_missing_file(tmp_path):
    with pytest.raises(gen.SourceError, match="not found"):
        gen.load_grind_table(tmp_path / "absent.json")


def test_load_grind_table_rejects_a_non_json_list(tmp_path):
    path = write_json(tmp_path, "grind.json", {"number": 1})
    with pytest.raises(gen.SourceError, match="JSON list"):
        gen.load_grind_table(path)


def test_load_grind_table_rejects_rows_with_missing_fields(tmp_path):
    rows = valid_grind()
    del rows[0]["time"]
    path = write_json(tmp_path, "grind.json", rows)
    with pytest.raises(gen.SourceError, match="time"):
        gen.validate_grind_table(gen.load_grind_table(path))


def test_load_grind_table_rejects_duplicate_slugs(tmp_path):
    rows = valid_grind()
    rows[1]["slug"] = rows[0]["slug"]
    path = write_json(tmp_path, "grind.json", rows)
    with pytest.raises(gen.SourceError, match="problem-1"):
        gen.validate_grind_table(gen.load_grind_table(path))


def test_load_grind_table_rejects_broken_numbering(tmp_path):
    rows = valid_grind()
    rows[0]["number"] = 4
    path = write_json(tmp_path, "grind.json", rows)
    with pytest.raises(gen.SourceError, match="numbering"):
        gen.validate_grind_table(gen.load_grind_table(path))


def test_load_neetcode_manifest_rejects_duplicate_lc_slugs(tmp_path):
    entries = valid_neetcode()
    entries[1]["lcSlug"] = entries[0]["lcSlug"]
    path = write_json(tmp_path, "neet.json", entries)
    with pytest.raises(gen.SourceError, match="track-problem-1"):
        gen.validate_neetcode_manifest(gen.load_neetcode_manifest(path))


def test_load_amazon_manifest_rejects_rows_out_of_recency_order(tmp_path):
    entries = valid_amazon()
    entries.reverse()
    path = write_json(tmp_path, "amazon.json", entries)
    with pytest.raises(gen.SourceError, match="recent"):
        gen.validate_amazon_manifest(gen.load_amazon_manifest(path))


def test_load_amazon_manifest_rejects_duplicate_slugs(tmp_path):
    entries = valid_amazon()
    entries[1]["slug"] = entries[0]["slug"]
    path = write_json(tmp_path, "amazon.json", entries)
    with pytest.raises(gen.SourceError, match="duplicate"):
        gen.validate_amazon_manifest(gen.load_amazon_manifest(path))


# ---------------------------------------------------------------------------
# The merger
# ---------------------------------------------------------------------------


def test_merge_tracks_yields_grind_order_then_neetcode_only_order():
    rows = gen.merge_tracks(fixture_grind(), fixture_neetcode())
    assert [row["slug"] for row in rows] == [
        "two-sum",
        "min-stack",
        "flood-fill",
        "jump-game",
    ]


def test_merge_tracks_merges_overlaps_into_one_row_crediting_both_tracks():
    rows = gen.merge_tracks(fixture_grind(), fixture_neetcode())
    merged = [row for row in rows if row["slug"] == "two-sum"]
    assert len(merged) == 1
    assert merged[0]["tracks"] == gen.BOTH_TRACKS


def test_merge_tracks_labels_grind_only_rows():
    rows = gen.merge_tracks(fixture_grind(), fixture_neetcode())
    flood_fill = next(row for row in rows if row["slug"] == "flood-fill")
    assert flood_fill["tracks"] == gen.GRIND_TRACK


def test_merge_tracks_labels_neetcode_only_rows():
    rows = gen.merge_tracks(fixture_grind(), fixture_neetcode())
    jump_game = next(row for row in rows if row["slug"] == "jump-game")
    assert jump_game["tracks"] == gen.NEETCODE_TRACK


def test_merge_tracks_keeps_grind_metadata_for_overlap_rows():
    rows = gen.merge_tracks(fixture_grind(), fixture_neetcode())
    min_stack = next(row for row in rows if row["slug"] == "min-stack")
    assert min_stack["title"] == "Minimum Stack"
    assert min_stack["difficulty"] == "Medium"
    assert min_stack["category"] == "Stack"
    assert min_stack["time"] == "20 minutes"


def test_merge_tracks_leaves_time_empty_for_neetcode_only_rows():
    rows = gen.merge_tracks(fixture_grind(), fixture_neetcode())
    jump_game = next(row for row in rows if row["slug"] == "jump-game")
    assert jump_game["time"] == ""


def test_merge_tracks_uses_the_neetcode_section_as_category_for_neetcode_only_rows():
    rows = gen.merge_tracks(fixture_grind(), fixture_neetcode())
    jump_game = next(row for row in rows if row["slug"] == "jump-game")
    assert jump_game["category"] == "Greedy"


# ---------------------------------------------------------------------------
# The Amazon overlap rule
# ---------------------------------------------------------------------------


def test_amazon_overlap_lc_slugs_strips_the_amazon_prefix_and_matches_lc_slugs():
    amazon = fixture_amazon() + [amazon_entry_for("min-stack")]
    assert gen.amazon_overlap_lc_slugs(fixture_neetcode(), amazon) == {"min-stack"}


def test_amazon_overlap_lc_slugs_ignores_amazon_slugs_outside_the_track():
    amazon = fixture_amazon() + [amazon_entry_for("flood-fill")]
    assert gen.amazon_overlap_lc_slugs(fixture_neetcode(), amazon) == set()


def test_amazon_overlap_lc_slugs_ignores_entries_without_the_amazon_prefix():
    entry = amazon_entry_for("min-stack")
    entry["slug"] = "min-stack"
    assert gen.amazon_overlap_lc_slugs(fixture_neetcode(), [entry]) == set()


def test_committed_amazon_overlap_rule_yields_exactly_the_17_listed_problems():
    overlap = gen.amazon_overlap_lc_slugs(
        gen.load_neetcode_manifest(NEETCODE_MANIFEST_PATH),
        gen.load_amazon_manifest(AMAZON_MANIFEST_PATH),
    )
    assert overlap == EXPECTED_AMAZON_OVERLAP_LC_SLUGS


# ---------------------------------------------------------------------------
# The committed merge shape
# ---------------------------------------------------------------------------


def test_committed_merge_yields_the_expected_universe_split():
    grind = gen.load_grind_table(GRIND_TABLE_PATH)
    neetcode = gen.load_neetcode_manifest(NEETCODE_MANIFEST_PATH)
    rows = gen.merge_tracks(grind, neetcode)
    tracks = [row["tracks"] for row in rows]
    assert len(rows) == gen.UNIQUE_PROBLEM_COUNT
    assert tracks.count(gen.BOTH_TRACKS) == gen.OVERLAP_COUNT
    assert tracks.count(gen.GRIND_TRACK) == gen.GRIND_ONLY_COUNT
    assert tracks.count(gen.NEETCODE_TRACK) == gen.NEETCODE_ONLY_COUNT
    assert gen.UNIQUE_PROBLEM_COUNT == gen.GRIND_ROW_COUNT + gen.NEETCODE_ONLY_COUNT


def committed_section():
    """Render the unified section from the committed data sources.

    Returns:
        The rendered unified section text with the committed Amazon overlap.
    """
    grind = gen.load_grind_table(GRIND_TABLE_PATH)
    neetcode = gen.load_neetcode_manifest(NEETCODE_MANIFEST_PATH)
    amazon = gen.load_amazon_manifest(AMAZON_MANIFEST_PATH)
    rows = gen.merge_tracks(grind, neetcode)
    return gen.render_unified_section(rows, gen.amazon_overlap_lc_slugs(neetcode, amazon))


def test_committed_unified_section_states_the_merge_counts():
    section = committed_section()
    assert str(gen.UNIQUE_PROBLEM_COUNT) in section
    assert str(gen.OVERLAP_COUNT) in section


def test_committed_merge_first_and_last_rows_follow_the_contract():
    rows = gen.merge_tracks(
        gen.load_grind_table(GRIND_TABLE_PATH),
        gen.load_neetcode_manifest(NEETCODE_MANIFEST_PATH),
    )
    assert rows[0]["slug"] == "two-sum"
    assert rows[-1]["slug"] == "reverse-integer"
    assert rows[-1]["tracks"] == gen.NEETCODE_TRACK
    assert rows[-1]["time"] == ""


# ---------------------------------------------------------------------------
# The emitters
# ---------------------------------------------------------------------------


def test_render_unified_section_emits_the_marker_bounded_six_column_table():
    section = render_fixture_section()
    assert section.startswith(gen.UNIFIED_SECTION_START)
    assert section.rstrip().endswith(gen.UNIFIED_SECTION_END)
    assert "## Problem List" in section
    assert "| # | Problem | Difficulty | Category | Tracks | Time |" in section
    row = [line for line in section.splitlines() if "two_sum" in line][0]
    assert row == (
        "| 1 "
        "| [Two Sum](problems/two_sum.md) | Easy | Array, Hash Table "
        "| Grind 75 + NeetCode 150 | 15 minutes |"
    )


def test_render_unified_section_numbers_rows_continuously_in_emitted_order():
    section = render_fixture_section()
    rows = unified_table_rows(section)
    assert [row_number(row) for row in rows] == [1, 2, 3, 4]


def test_committed_unified_section_numbers_rows_one_through_168_with_no_gaps_or_dupes():
    rows = unified_table_rows(committed_section())
    assert len(rows) == gen.UNIQUE_PROBLEM_COUNT
    assert [row_number(row) for row in rows] == list(
        range(1, gen.UNIQUE_PROBLEM_COUNT + 1)
    )


def test_render_unified_section_appends_the_amazon_marker_to_overlapping_rows():
    amazon = fixture_amazon() + [amazon_entry_for("min-stack")]
    section = render_fixture_section(amazon=amazon)
    min_stack = [line for line in section.splitlines() if "min_stack" in line][0]
    assert min_stack.endswith(f"| Grind 75 + NeetCode 150 {gen.AMAZON_MARKER} | 20 minutes |")
    two_sum = [line for line in section.splitlines() if "two_sum" in line][0]
    assert gen.AMAZON_MARKER not in two_sum


def test_render_unified_section_marks_exactly_the_17_committed_amazon_overlap_rows():
    rows = unified_table_rows(committed_section())
    marked_slugs = {
        unified_row_lc_slug(row) for row in rows if gen.AMAZON_MARKER in row
    }
    assert marked_slugs == EXPECTED_AMAZON_OVERLAP_LC_SLUGS
    assert sum(gen.AMAZON_MARKER in row for row in rows) == 17


def test_render_unified_section_excludes_grind_only_amazon_matches_from_the_marker():
    amazon = fixture_amazon() + [amazon_entry_for("flood-fill")]
    section = render_fixture_section(amazon=amazon)
    flood_fill = [line for line in section.splitlines() if "flood_fill" in line][0]
    assert gen.AMAZON_MARKER not in flood_fill


def test_render_unified_section_carries_the_amazon_legend():
    section = render_fixture_section(amazon=fixture_amazon() + [amazon_entry_for("min-stack")])
    assert gen.AMAZON_LEGEND in section
    assert "problems/amazon_oa/index.md" in section


def test_render_amazon_section_lists_rows_most_recent_first():
    section = gen.render_amazon_section(fixture_amazon())
    assert section.startswith(gen.AMAZON_SECTION_START)
    assert section.rstrip().endswith(gen.AMAZON_SECTION_END)
    assert "## Amazon OA Problems" in section
    assert "| # | Problem | Updated |" in section
    row = [line for line in section.splitlines() if "amazon-maximize" in line][0]
    assert row == (
        "| 1 | [Maximize Adjacent Difference With One Reversal]"
        "(problems/amazon_oa/amazon-maximize-adjacent-difference-with-one-reversal.md)"
        " | 2026-09-19 |"
    )


def test_render_amazon_section_numbers_rows_sequentially():
    section = gen.render_amazon_section(fixture_amazon())
    rows = [line for line in section.splitlines() if line.startswith("| ")]
    numbers = [line.split("|")[1].strip() for line in rows if line.split("|")[1].strip().isdigit()]
    assert numbers == ["1", "2"]


def test_render_sources_section_credits_all_three_lists():
    section = gen.render_sources_section()
    assert section.startswith(gen.SOURCES_SECTION_START)
    assert section.rstrip().endswith(gen.SOURCES_SECTION_END)
    assert "## Sources" in section
    assert "https://www.techinterviewhandbook.org/grind75" in section
    assert "https://neetcode.io/practice/practice/neetcode150" in section
    assert "https://github.com/perixtar/Tech-OA-Interview-Questions" in section
    assert "https://www.fastprep.io" in section


# ---------------------------------------------------------------------------
# Emission into docs/index.md
# ---------------------------------------------------------------------------


def fresh_index(tmp_path):
    index_path = tmp_path / "index.md"
    index_path.write_text(
        "# Home\n\nIntro prose.\n\n## Pattern Intuition\n\nProse.\n",
        encoding="utf-8",
    )
    return index_path


def test_write_sections_splices_all_three_sections_before_the_anchor(tmp_path):
    index_path = fresh_index(tmp_path)
    changed = gen.write_sections(index_path=index_path)
    assert changed is True
    text = index_path.read_text(encoding="utf-8")
    assert text.index(gen.UNIFIED_SECTION_START) < text.index(gen.AMAZON_SECTION_START)
    assert text.index(gen.AMAZON_SECTION_START) < text.index(gen.SOURCES_SECTION_START)
    assert text.index(gen.SOURCES_SECTION_START) < text.index("## Pattern Intuition")


def test_write_sections_is_byte_stable_on_regeneration(tmp_path):
    index_path = fresh_index(tmp_path)
    gen.write_sections(index_path=index_path)
    first = index_path.read_text(encoding="utf-8")
    changed = gen.write_sections(index_path=index_path)
    assert changed is False
    assert index_path.read_text(encoding="utf-8") == first


def test_write_sections_replaces_a_mutated_row(tmp_path):
    index_path = fresh_index(tmp_path)
    gen.write_sections(index_path=index_path)
    text = index_path.read_text(encoding="utf-8")
    text = text.replace("[Two Sum](problems/two_sum.md)", "[Wrong Sum](problems/wrong_sum.md)")
    index_path.write_text(text, encoding="utf-8")
    changed = gen.write_sections(index_path=index_path)
    assert changed is True
    assert "[Two Sum](problems/two_sum.md)" in index_path.read_text(encoding="utf-8")


def test_write_sections_requires_a_landing_anchor_when_markers_are_absent(tmp_path):
    index_path = tmp_path / "index.md"
    index_path.write_text("# Home\n\nNo tables here.\n", encoding="utf-8")
    with pytest.raises(SystemExit, match="Pattern Intuition"):
        gen.write_sections(index_path=index_path)


# ---------------------------------------------------------------------------
# The --check gate
# ---------------------------------------------------------------------------


def test_check_passes_after_emission(tmp_path):
    index_path = fresh_index(tmp_path)
    gen.write_sections(index_path=index_path)
    assert gen.check(index_path=index_path) == 0


def test_check_fails_when_a_row_drifts(tmp_path):
    index_path = fresh_index(tmp_path)
    gen.write_sections(index_path=index_path)
    text = index_path.read_text(encoding="utf-8")
    index_path.write_text(
        text.replace("[Two Sum](problems/two_sum.md)", "[Wrong Sum](problems/wrong_sum.md)"),
        encoding="utf-8",
    )
    assert gen.check(index_path=index_path) == 1


def test_check_fails_when_markers_are_missing(tmp_path):
    index_path = fresh_index(tmp_path)
    assert gen.check(index_path=index_path) == 1


# ---------------------------------------------------------------------------
# CLI wiring
# ---------------------------------------------------------------------------


def test_main_emits_sections_and_exits_zero(tmp_path, monkeypatch, capsys):
    index_path = fresh_index(tmp_path)
    monkeypatch.setattr(gen, "INDEX_PATH", index_path)
    assert gen.main([]) == 0
    assert gen.UNIFIED_SECTION_START in index_path.read_text(encoding="utf-8")
    assert "sections written" in capsys.readouterr().out


def test_main_check_mode_is_read_only_and_exits_zero(tmp_path, monkeypatch):
    index_path = fresh_index(tmp_path)
    gen.write_sections(index_path=index_path)
    before = index_path.read_text(encoding="utf-8")
    monkeypatch.setattr(gen, "INDEX_PATH", index_path)
    assert gen.main(["--check"]) == 0
    assert index_path.read_text(encoding="utf-8") == before


def test_main_check_mode_fails_on_drift(tmp_path, monkeypatch):
    index_path = fresh_index(tmp_path)
    gen.write_sections(index_path=index_path)
    text = index_path.read_text(encoding="utf-8")
    index_path.write_text(text.replace("## Sources", "## Credits"), encoding="utf-8")
    monkeypatch.setattr(gen, "INDEX_PATH", index_path)
    assert gen.main(["--check"]) == 1


def test_committed_index_satisfies_the_check_gate():
    assert gen.check() == 0
