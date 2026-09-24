"""Unit tests for the progress tracker's canonical order parser.

The canonical order comes from the problem table the index-tables
generator emits into docs/problems/index.md. Run with:

    cd practice && uv run pytest test_progress.py
"""

import progress
import pytest


@pytest.fixture
def patch_docs_index(tmp_path, monkeypatch):
    """Point the tracker at a caller-written landing page."""

    def _patch(text):
        index = tmp_path / "index.md"
        index.write_text(text, encoding="utf-8")
        monkeypatch.setattr(progress, "DOCS_INDEX", index)
        return index

    return _patch


UNIFIED_TABLE = """\
# Problems

<!-- unified-leetcode:start -->
## Problem List

| Problem | Difficulty | Category | Practice at | Tracks | Time |
|---|---------|------------|----------|--------|------|
| [Two Sum](two_sum.md) | Easy | Array, Hash Table | [LeetCode](https://leetcode.com/problems/two-sum/) | [Grind 75](https://www.techinterviewhandbook.org/grind75?order=grind75-order) + [NeetCode 150](https://neetcode.io/practice/neetcode150) | 15 minutes |
| [Daily Temperatures](daily_temperatures.md) | Medium | Stack | [LeetCode](https://leetcode.com/problems/daily-temperatures/) | [NeetCode 150](https://neetcode.io/practice/neetcode150) |  |
| [Implement Trie (Prefix Tree)](implement_trie_prefix_tree.md) | Medium | Trie | [LeetCode](https://leetcode.com/problems/implement-trie-prefix-tree/) | [Grind 75](https://www.techinterviewhandbook.org/grind75?order=grind75-order) + [NeetCode 150](https://neetcode.io/practice/neetcode150) | 35 minutes |

Rows marked · Amazon OA also appear in the [Amazon OA bank](amazon_oa/index.md).
<!-- unified-leetcode:end -->

<!-- amazon-oa:start -->
## Amazon OA Problems

| Problem | Updated | Practice at |
|---|---------|---------|
| [Some OA Problem](amazon_oa/amazon-some-oa-problem.md) | 2026-09-19 | [FastPrep](https://www.fastprep.io/problems/amazon-some-oa-problem) |
<!-- amazon-oa:end -->
"""


def test_canonical_order_reads_table_rows_in_appearance_order(patch_docs_index):
    patch_docs_index(UNIFIED_TABLE)
    assert progress.canonical_order(
        ["daily_temperatures", "two_sum", "implement_trie_prefix_tree"]
    ) == ["two_sum", "daily_temperatures", "implement_trie_prefix_tree"]


def test_canonical_order_appends_problems_missing_from_the_table(patch_docs_index):
    patch_docs_index(UNIFIED_TABLE)
    assert progress.canonical_order(["two_sum", "zz_extra", "aa_extra"]) == [
        "two_sum",
        "aa_extra",
        "zz_extra",
    ]


def test_canonical_order_ignores_amazon_table_rows(patch_docs_index):
    patch_docs_index(UNIFIED_TABLE)
    ordered = progress.canonical_order(["amazon_some_oa_problem", "two_sum"])
    assert ordered == ["two_sum", "amazon_some_oa_problem"]


def test_canonical_order_tolerates_titles_with_parentheses(patch_docs_index):
    patch_docs_index(UNIFIED_TABLE)
    assert "implement_trie_prefix_tree" in progress.canonical_order(
        ["implement_trie_prefix_tree"]
    )


def test_canonical_order_falls_back_to_alphabetical_when_the_table_is_missing(
    patch_docs_index,
):
    patch_docs_index("# Problems\n\nNo table here.\n")
    assert progress.canonical_order(["bb", "aa"]) == ["aa", "bb"]


def test_canonical_order_falls_back_when_the_file_is_missing(tmp_path, monkeypatch):
    monkeypatch.setattr(progress, "DOCS_INDEX", tmp_path / "absent.md")
    assert progress.canonical_order(["bb", "aa"]) == ["aa", "bb"]


def test_committed_landing_page_orders_the_full_problem_universe():
    known = sorted(
        entry.name
        for entry in progress.PRACTICE_DIR.iterdir()
        if entry.is_dir() and (entry / "solution.py").is_file()
    )
    ordered = progress.canonical_order(known)
    assert len(ordered) == len(known)
    assert set(ordered) == set(known)
    assert ordered[0] == "two_sum"
