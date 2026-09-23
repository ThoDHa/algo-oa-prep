"""Generate the docs/problems/index.md landing page and the mkdocs.yml
Problems nav for grind75.

Pipeline:
  1. Validate the three committed data sources: scripts/grind75_table.json
     (the 77 hand-maintained Grind 75 rows extracted from the original hand
     table), scripts/neetcode150_manifest.json (the 150-entry NeetCode
     track), and scripts/amazon_oa_manifest.json (the 350-entry Amazon OA
     bank, most recently updated first).
  2. Merge the two LeetCode tracks into one unified table: 168 unique
     problems, 59 of them on both tracks (one row, both credited), Grind 75
     order first, then the NeetCode-only problems in track order. Rows are
     numbered 1..168 continuously in emitted order, so the hand-table's
     original Grind numbers never collide with the NeetCode track orders.
  3. Cross-reference the Amazon OA bank: rows whose problem also appears
     there (amazon slug minus the amazon- prefix matching a NeetCode
     lcSlug) carry an "Amazon OA" marker with a legend under the table.
  4. Emit three marker-bounded sections into docs/problems/index.md: the
     unified LeetCode table, the separate Amazon OA table, and the Sources
     credits. --check compares the marker spans against a fresh render, so
     the tables stay generator-owned and refreshable.
  5. Emit the mkdocs.yml Problems nav: the landing page as section parent
     (navigation.indexes) with two subsections, LeetCode (all 168 problem
     pages at one level, unified-table order) and Amazon OA (the bank
     index). --check verifies the nav shape, so the subsections stay
     generator-owned and refreshable.

Offline contract: the committed JSON sources are the only inputs; nothing
is fetched, and the marker-bounded spans (plus the nav's Problems section)
are the only text ever rewritten.

Usage (from the repository root):
  cd practice && uv run pytest ../scripts/          # run the generator tests
  python3 scripts/generate_index_tables.py [--check]
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import List, Optional, Sequence

REPO_ROOT = Path(__file__).resolve().parent.parent
GRIND_TABLE_PATH = REPO_ROOT / "scripts" / "grind75_table.json"
NEETCODE_MANIFEST_PATH = REPO_ROOT / "scripts" / "neetcode150_manifest.json"
AMAZON_MANIFEST_PATH = REPO_ROOT / "scripts" / "amazon_oa_manifest.json"
PROBLEMS_INDEX_PATH = REPO_ROOT / "docs" / "problems" / "index.md"
MKDOCS_PATH = REPO_ROOT / "mkdocs.yml"

UNIFIED_SECTION_START = "<!-- unified-leetcode:start -->"
UNIFIED_SECTION_END = "<!-- unified-leetcode:end -->"
AMAZON_SECTION_START = "<!-- amazon-oa:start -->"
AMAZON_SECTION_END = "<!-- amazon-oa:end -->"
SOURCES_SECTION_START = "<!-- sources:start -->"
SOURCES_SECTION_END = "<!-- sources:end -->"
# Fresh splices land immediately before this heading; marker-bounded
# replacements keep their in-place position instead.
LANDING_ANCHOR = "## Study Guide and Practice"

NAV_PROBLEMS_MARKER = "  - Problems:\n"
NAV_LEETCODE_HEADER = '    - "LeetCode":\n'
NAV_AMAZON_HEADER = '    - "Amazon OA": problems/amazon_oa/index.md\n'
NAV_LEETCODE_CHILD_PATTERN = re.compile(r'^      - "(.+?)": problems/(.+?)\.md$')
NAV_NEXT_TOP_PATTERN = re.compile(r"^  - ", re.M)
NAV_ADMISSIBLE_SLUG_COUNT = 168

GRIND_TRACK = "Grind 75"
NEETCODE_TRACK = "NeetCode 150"
BOTH_TRACKS = "Grind 75 + NeetCode 150"

GRIND_ROW_COUNT = 77
NUMBERED_GRIND_COUNT = 75
NEETCODE_TRACK_SIZE = 150
AMAZON_ROW_COUNT = 350
GRIND_ONLY_COUNT = 18
OVERLAP_COUNT = 59
NEETCODE_ONLY_COUNT = 91
UNIQUE_PROBLEM_COUNT = GRIND_ROW_COUNT + NEETCODE_ONLY_COUNT

GRIND_TABLE_FIELDS = ("number", "slug", "title", "difficulty", "category", "time")
NEETCODE_MANIFEST_FIELDS = (
    "order",
    "section",
    "title",
    "lcSlug",
    "dirSlug",
    "difficulty",
)
AMAZON_MANIFEST_FIELDS = (
    "slug",
    "title",
    "url",
    "companies",
    "updated",
    "parse_status",
)
DIFFICULTIES = ("Easy", "Medium", "Hard")

AMAZON_SLUG_PREFIX = "amazon-"
UNIFIED_TABLE_HEADER = "| # | Problem | Difficulty | Category | Tracks | Time |"
AMAZON_TABLE_HEADER = "| # | Problem | Updated |"
AMAZON_MARKER = "· Amazon OA"
AMAZON_LEGEND = (
    f"Rows marked {AMAZON_MARKER} also appear in the"
    " [Amazon OA bank](amazon_oa/index.md)."
)


class SourceError(ValueError):
    """Raised when a committed data source violates its contract."""


# ---------------------------------------------------------------------------
# Loading and validation
# ---------------------------------------------------------------------------


def _load_json_list(path: Path, source_name: str) -> list:
    """Read a JSON list file, raising SourceError with context on failure.

    Args:
        path: Path to the JSON file.
        source_name: Human-readable source name for error messages.

    Returns:
        The parsed JSON list.

    Raises:
        SourceError: When the file is missing, unreadable, invalid JSON,
            or not a JSON list.
    """
    if not path.exists():
        raise SourceError(f"{source_name} not found: {path}")
    try:
        entries = json.loads(path.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, UnicodeDecodeError) as error:
        raise SourceError(f"{source_name} {path} is not valid JSON: {error}") from error
    if not isinstance(entries, list):
        raise SourceError(f"{source_name} {path} must be a JSON list")
    return entries


def _require_fields(entries: Sequence[dict], fields: Sequence[str], source_name: str) -> None:
    """Check that every entry carries the required fields.

    Args:
        entries: The manifest entries.
        fields: Required field names.
        source_name: Human-readable source name for error messages.

    Raises:
        SourceError: When an entry misses a field or is not an object.
    """
    for entry in entries:
        if not isinstance(entry, dict):
            raise SourceError(f"{source_name} entries must be JSON objects, got {type(entry).__name__}")
        missing = [field for field in fields if field not in entry]
        if missing:
            raise SourceError(
                f"{source_name} entry is missing field(s) {', '.join(missing)}: {entry}"
            )


def load_grind_table(path: Path = GRIND_TABLE_PATH) -> List[dict]:
    """Load the committed Grind 75 metadata table.

    Args:
        path: Path to grind75_table.json (default: scripts/grind75_table.json).

    Returns:
        The 77 rows in hand-table order.

    Raises:
        SourceError: When the file is missing or not a JSON list.
    """
    return _load_json_list(path, "Grind 75 table")


def validate_grind_table(rows: Sequence[dict]) -> None:
    """Check the Grind 75 table against the hand-table contract.

    The contract: exactly GRIND_ROW_COUNT rows with the hand-table fields,
    unique slugs, rows 1..75 numbered in order followed by the unnumbered
    extra rows.

    Args:
        rows: The loaded grind75_table.json rows.

    Raises:
        SourceError: On any contract violation.
    """
    if len(rows) != GRIND_ROW_COUNT:
        raise SourceError(f"Grind 75 table must carry {GRIND_ROW_COUNT} rows, got {len(rows)}")
    _require_fields(rows, GRIND_TABLE_FIELDS, "Grind 75 table")
    slugs = [row["slug"] for row in rows]
    duplicates = sorted({slug for slug in slugs if slugs.count(slug) > 1})
    if duplicates:
        raise SourceError(f"Grind 75 table has duplicate slug(s): {', '.join(duplicates)}")
    numbers = [row["number"] for row in rows]
    numbered = [number for number in numbers if number is not None]
    if numbered != list(range(1, NUMBERED_GRIND_COUNT + 1)):
        raise SourceError(
            "Grind 75 table numbering must be 1..75 in order followed by unnumbered rows,"
            f" got {numbered}"
        )
    for row in rows:
        if not isinstance(row["number"], int) and row["number"] is not None:
            raise SourceError(f"Grind 75 row number must be an integer or null: {row}")
        for field in ("slug", "title", "difficulty", "category", "time"):
            if not isinstance(row[field], str) or not row[field]:
                raise SourceError(f"Grind 75 row field {field} must be a non-empty string: {row}")


def load_neetcode_manifest(path: Path = NEETCODE_MANIFEST_PATH) -> List[dict]:
    """Load the committed NeetCode 150 manifest.

    Args:
        path: Path to neetcode150_manifest.json (default: scripts/neetcode150_manifest.json).

    Returns:
        The 150 entries in track order.

    Raises:
        SourceError: When the file is missing or not a JSON list.
    """
    return _load_json_list(path, "NeetCode 150 manifest")


def validate_neetcode_manifest(entries: Sequence[dict]) -> None:
    """Check the NeetCode 150 manifest against the merge-relevant contract.

    The full track contract (sections, difficulty totals) is owned by the
    NeetCode generator; this validates what the unified table consumes:
    NEETCODE_TRACK_SIZE entries, orders 1..150, unique lcSlugs and
    dirSlugs, canonical difficulties.

    Args:
        entries: The loaded manifest entries.

    Raises:
        SourceError: On any contract violation.
    """
    if len(entries) != NEETCODE_TRACK_SIZE:
        raise SourceError(
            f"NeetCode 150 manifest must carry {NEETCODE_TRACK_SIZE} entries, got {len(entries)}"
        )
    _require_fields(entries, NEETCODE_MANIFEST_FIELDS, "NeetCode 150 manifest")
    orders = [entry["order"] for entry in entries]
    if orders != list(range(1, NEETCODE_TRACK_SIZE + 1)):
        raise SourceError(f"NeetCode 150 orders must be 1..{NEETCODE_TRACK_SIZE} in order")
    for slug_field in ("lcSlug", "dirSlug"):
        slugs = [entry[slug_field] for entry in entries]
        duplicates = sorted({slug for slug in slugs if slugs.count(slug) > 1})
        if duplicates:
            raise SourceError(
                f"NeetCode 150 manifest has duplicate {slug_field}(s): {', '.join(duplicates)}"
            )
    for entry in entries:
        if entry["difficulty"] not in DIFFICULTIES:
            raise SourceError(
                f"NeetCode 150 difficulty must be one of {', '.join(DIFFICULTIES)}: {entry}"
            )


def load_amazon_manifest(path: Path = AMAZON_MANIFEST_PATH) -> List[dict]:
    """Load the committed Amazon OA manifest.

    Args:
        path: Path to amazon_oa_manifest.json (default: scripts/amazon_oa_manifest.json).

    Returns:
        The 350 entries, most recently updated first.

    Raises:
        SourceError: When the file is missing or not a JSON list.
    """
    return _load_json_list(path, "Amazon OA manifest")


def validate_amazon_manifest(entries: Sequence[dict]) -> None:
    """Check the Amazon OA manifest against the table contract.

    The contract: exactly AMAZON_ROW_COUNT entries with the manifest
    fields, unique slugs, sorted most recently updated first.

    Args:
        entries: The loaded manifest entries.

    Raises:
        SourceError: On any contract violation.
    """
    if len(entries) != AMAZON_ROW_COUNT:
        raise SourceError(f"Amazon OA manifest must carry {AMAZON_ROW_COUNT} entries, got {len(entries)}")
    _require_fields(entries, AMAZON_MANIFEST_FIELDS, "Amazon OA manifest")
    slugs = [entry["slug"] for entry in entries]
    if len(set(slugs)) != len(slugs):
        duplicates = sorted({slug for slug in slugs if slugs.count(slug) > 1})
        raise SourceError(f"Amazon OA manifest has duplicate slug(s): {', '.join(duplicates)}")
    updated = [entry["updated"] for entry in entries]
    if updated != sorted(updated, reverse=True):
        raise SourceError(
            "Amazon OA manifest must be sorted most recently updated first"
            f" (first out-of-order pair near {updated[0]!r})"
        )


# ---------------------------------------------------------------------------
# Track merger
# ---------------------------------------------------------------------------


def merge_tracks(grind: Sequence[dict], neetcode: Sequence[dict]) -> List[dict]:
    """Merge the Grind 75 rows and the NeetCode 150 track into unified rows.

    Grind 75 rows keep their hand-table metadata verbatim and come first in
    hand-table order; NeetCode-only problems follow in track order with the
    section as category and an empty Time cell (NeetCode publishes no
    minutes). Overlaps merge by lcSlug into one row carrying both track
    names, keeping the Grind 75 metadata. Rows carry no sequence number:
    the unified table is numbered continuously at render time, so the
    hand-table's original Grind numbers cannot collide with the NeetCode
    track orders.

    Args:
        grind: The validated grind75_table.json rows.
        neetcode: The validated neetcode150_manifest.json entries.

    Returns:
        Unified rows with slug, dirSlug, title, difficulty, category,
        tracks, and time.
    """
    neet_by_lc_slug = {entry["lcSlug"]: entry for entry in neetcode}
    grind_slugs = {row["slug"] for row in grind}
    rows: List[dict] = []
    for row in grind:
        rows.append(
            {
                "slug": row["slug"],
                "dirSlug": row["slug"].replace("-", "_"),
                "title": row["title"],
                "difficulty": row["difficulty"],
                "category": row["category"],
                "tracks": BOTH_TRACKS if row["slug"] in neet_by_lc_slug else GRIND_TRACK,
                "time": row["time"],
            }
        )
    for entry in neetcode:
        if entry["lcSlug"] in grind_slugs:
            continue
        rows.append(
            {
                "slug": entry["lcSlug"],
                "dirSlug": entry["dirSlug"],
                "title": entry["title"],
                "difficulty": entry["difficulty"],
                "category": entry["section"],
                "tracks": NEETCODE_TRACK,
                "time": "",
            }
        )
    return rows


def verify_merge_shape(rows: Sequence[dict]) -> None:
    """Check the committed merge against the expected universe split.

    Guards the constants against upstream data drift: a Grind 75 or
    NeetCode refresh that changes the overlap must update the constants
    consciously.

    Args:
        rows: The merged rows.

    Raises:
        SourceError: When the track split no longer matches the constants.
    """
    tracks = [row["tracks"] for row in rows]
    actual = {
        "unique": len(rows),
        "both": tracks.count(BOTH_TRACKS),
        "grind-only": tracks.count(GRIND_TRACK),
        "neetcode-only": tracks.count(NEETCODE_TRACK),
    }
    expected = {
        "unique": UNIQUE_PROBLEM_COUNT,
        "both": OVERLAP_COUNT,
        "grind-only": GRIND_ONLY_COUNT,
        "neetcode-only": NEETCODE_ONLY_COUNT,
    }
    if actual != expected:
        raise SourceError(
            "merged track split drifted from the constants"
            f" (expected {expected}, got {actual});"
            " refresh grind75_table.json / neetcode150_manifest.json and the constants together"
        )


# ---------------------------------------------------------------------------
# Amazon overlap
# ---------------------------------------------------------------------------


def amazon_overlap_lc_slugs(neetcode: Sequence[dict], amazon: Sequence[dict]) -> set:
    """Find the unified-table problems that also appear in the Amazon bank.

    The match rule: an Amazon slug minus the ``amazon-`` prefix equals a
    NeetCode lcSlug. Requiring the lcSlug match keeps the marker on the
    rows a reader reaches through the unified table's problem set; Grind-only
    problems absent from the NeetCode track stay unmarked.

    Args:
        neetcode: The NeetCode manifest entries.
        amazon: The Amazon OA manifest entries.

    Returns:
        The matching LeetCode slugs.
    """
    lc_slugs = {entry["lcSlug"] for entry in neetcode}
    return {
        entry["slug"][len(AMAZON_SLUG_PREFIX) :]
        for entry in amazon
        if entry["slug"].startswith(AMAZON_SLUG_PREFIX)
        and entry["slug"][len(AMAZON_SLUG_PREFIX) :] in lc_slugs
    }


# ---------------------------------------------------------------------------
# Renderers
# ---------------------------------------------------------------------------


def render_unified_section(rows: Sequence[dict], overlap: set) -> str:
    """Render the marker-bounded unified LeetCode table section.

    Columns `| # | Problem | Difficulty | Category | Tracks | Time |`;
    `#` is the continuous row position (1..N in emitted order, so the
    hand-table Grind numbers never collide with the NeetCode track orders)
    and `Problem` links the write-up. Rows in the overlap set carry the
    Amazon OA marker in the Tracks cell, with a legend under the table.

    Args:
        rows: The merged unified rows.
        overlap: LeetCode slugs from these rows also in the Amazon OA bank.

    Returns:
        The section text: start marker through end marker, trailing newline.
    """
    overlap_count = sum(1 for row in rows if row["tracks"] == BOTH_TRACKS)
    lines = [
        UNIFIED_SECTION_START,
        "## Problem List",
        "",
        f"The unified LeetCode problem set across the"
        f" [Grind 75](https://www.techinterviewhandbook.org/grind75)"
        f" and the [NeetCode 150](https://neetcode.io/practice/practice/neetcode150):"
        f" {len(rows)} unique problems, {overlap_count} on both tracks and credited to each."
        " Grind 75 study order first, then the NeetCode-only problems in track order."
        " Tracks names the plan(s) a problem belongs to; Time carries the Grind 75"
        " suggested minutes and stays empty for NeetCode-only problems.",
        "",
        UNIFIED_TABLE_HEADER,
        "|---|---------|------------|----------|--------|------|",
    ]
    for position, row in enumerate(rows, start=1):
        problem = f"[{row['title']}]({row['dirSlug']}.md)"
        tracks = row["tracks"]
        if row["slug"] in overlap:
            tracks = f"{tracks} {AMAZON_MARKER}"
        lines.append(
            f"| {position} | {problem} | {row['difficulty']}"
            f" | {row['category']} | {tracks} | {row['time']} |"
        )
    if any(row["slug"] in overlap for row in rows):
        lines.append("")
        lines.append(AMAZON_LEGEND)
    lines.append(UNIFIED_SECTION_END)
    return "\n".join(lines) + "\n"


def render_amazon_section(entries: Sequence[dict]) -> str:
    """Render the marker-bounded Amazon OA table section.

    Separate from the LeetCode tables: columns `| # | Problem | Updated |`,
    most recently updated first, `Problem` linking the write-up page.

    Args:
        entries: The validated Amazon OA manifest entries.

    Returns:
        The section text: start marker through end marker, trailing newline.
    """
    lines = [
        AMAZON_SECTION_START,
        "## Amazon OA Problems",
        "",
        "The Amazon OA coding bank, separate from the LeetCode tables above:"
        f" {len(entries)} Amazon-tagged online-assessment problems, most recently"
        " updated first. The problems come from"
        " [perixtar/Tech-OA-Interview-Questions](https://github.com/perixtar/Tech-OA-Interview-Questions)"
        " with statement pages on [FastPrep](https://www.fastprep.io)."
        " The full bank index with companies lives at"
        " [problems/amazon_oa/index.md](amazon_oa/index.md);"
        " practice stubs live under the"
        " [`practice/amazon_oa/`](https://github.com/ThoDHa/algo-oa-prep/tree/main/practice/amazon_oa)"
        " workspace.",
        "",
        AMAZON_TABLE_HEADER,
        "|---|---------|---------|",
    ]
    for position, entry in enumerate(entries, start=1):
        problem = f"[{entry['title']}](amazon_oa/{entry['slug']}.md)"
        lines.append(f"| {position} | {problem} | {entry['updated']} |")
    lines.append(AMAZON_SECTION_END)
    return "\n".join(lines) + "\n"


def render_sources_section() -> str:
    """Render the marker-bounded Sources credits section.

    Credits all three upstream list curators; static by design (the credits
    do not depend on the data files).

    Returns:
        The section text: start marker through end marker, trailing newline.
    """
    lines = [
        SOURCES_SECTION_START,
        "## Sources",
        "",
        "The three problem banks are curated elsewhere; this site adds the"
        " write-ups, pattern guides, and practice workspace.",
        "",
        "- [Grind 75](https://www.techinterviewhandbook.org/grind75), curated by the"
        " [Tech Interview Handbook](https://www.techinterviewhandbook.org/) team.",
        "- [NeetCode 150](https://neetcode.io/practice/practice/neetcode150), curated by the"
        " [NeetCode](https://neetcode.io/) team.",
        "- The Amazon OA bank, from"
        " [perixtar/Tech-OA-Interview-Questions](https://github.com/perixtar/Tech-OA-Interview-Questions)"
        " with problem pages on [FastPrep](https://www.fastprep.io).",
        SOURCES_SECTION_END,
    ]
    return "\n".join(lines) + "\n"


def load_validated_sources() -> tuple:
    """Load and validate all three committed data sources.

    Shared by the render, emission, and check paths so every consumer sees
    the same contract enforcement.

    Returns:
        The (grind rows, neetcode entries, amazon entries) triple.

    Raises:
        SourceError: When any source violates its contract.
    """
    grind = load_grind_table()
    neetcode = load_neetcode_manifest()
    amazon = load_amazon_manifest()
    validate_grind_table(grind)
    validate_neetcode_manifest(neetcode)
    validate_amazon_manifest(amazon)
    return grind, neetcode, amazon


def render_sections() -> List[tuple]:
    """Render every docs/problems/index.md section this generator owns.

    Shared by the emission and check paths so the two can never drift.

    Returns:
        One (name, start marker, end marker, rendered text) tuple per
        section, in document order.
    """
    grind, neetcode, amazon = load_validated_sources()
    merged = merge_tracks(grind, neetcode)
    verify_merge_shape(merged)
    overlap = amazon_overlap_lc_slugs(neetcode, amazon)
    return [
        (
            "unified-leetcode",
            UNIFIED_SECTION_START,
            UNIFIED_SECTION_END,
            render_unified_section(merged, overlap),
        ),
        ("amazon-oa", AMAZON_SECTION_START, AMAZON_SECTION_END, render_amazon_section(amazon)),
        ("sources", SOURCES_SECTION_START, SOURCES_SECTION_END, render_sources_section()),
    ]


# ---------------------------------------------------------------------------
# Emission
# ---------------------------------------------------------------------------


def write_sections(landing_path: Optional[Path] = None) -> bool:
    """Emit the three marker-bounded sections into docs/problems/index.md.

    Present marker spans are replaced in place; absent sections are spliced
    as one block immediately before the landing anchor. Only the marker
    spans (and the fresh splice point) are ever rewritten.

    Args:
        landing_path: Overrides the docs/problems/index.md path (default:
            module constant).

    Returns:
        True when the file was modified, False when it already matched.

    Raises:
        SystemExit: When markers are unclosed or no landing anchor exists.
    """
    landing_path = landing_path if landing_path is not None else PROBLEMS_INDEX_PATH
    text = landing_path.read_text(encoding="utf-8")
    original = text
    missing: List[str] = []
    for _name, start_marker, end_marker, rendered in render_sections():
        start_at = text.find(start_marker)
        if start_at == -1:
            missing.append(rendered)
            continue
        end_at = text.find(end_marker, start_at)
        if end_at == -1:
            raise SystemExit(f"{index_path} has {start_marker!r} without {end_marker!r}")
        text = text[:start_at] + rendered.rstrip() + text[end_at + len(end_marker) :]
    if missing:
        anchor_at = text.find(LANDING_ANCHOR)
        if anchor_at == -1:
            raise SystemExit(
                f"{landing_path} has no {LANDING_ANCHOR!r} anchor to splice the"
                f" {len(missing)} missing section(s) against"
            )
        block = "\n\n".join(missing)
        text = text[:anchor_at] + block + "\n\n" + text[anchor_at:]
    if text == original:
        return False
    landing_path.write_text(text, encoding="utf-8")
    return True


# ---------------------------------------------------------------------------
# mkdocs.yml Problems nav
# ---------------------------------------------------------------------------


def render_problems_nav(merged: Sequence[dict]) -> str:
    """Render the Problems nav block: landing parent plus two subsections.

    The landing page is the section parent (mkdocs-material's
    navigation.indexes renders it as the Problems index); the LeetCode
    subsection carries every merged row at one level in unified-table order
    (Grind 75 study order, then the NeetCode-only track order); the Amazon
    OA subsection carries the bank index page.

    Args:
        merged: The validated merged rows (see `merge_tracks`).

    Returns:
        The nav block from the Problems marker through the Amazon OA line,
        each line newline-terminated.
    """
    lines = [
        NAV_PROBLEMS_MARKER,
        "    - problems/index.md\n",
        NAV_LEETCODE_HEADER,
    ]
    lines.extend(
        f'      - "{row["title"]}": problems/{row["dirSlug"]}.md\n' for row in merged
    )
    lines.append(NAV_AMAZON_HEADER)
    return "".join(lines)


def write_problems_nav(mkdocs_path: Optional[Path] = None) -> bool:
    """Replace the mkdocs.yml Problems nav section with the generated shape.

    Everything between the Problems marker and the next top-level nav entry
    (a line starting with exactly two spaces, a hyphen, and a space) or the
    end of file is regenerated; everything outside the section is untouched.

    Args:
        mkdocs_path: Overrides the mkdocs.yml path (default: module constant).

    Returns:
        True when the file was modified, False when it already matched.

    Raises:
        SystemExit: When mkdocs.yml has no Problems nav section.
    """
    mkdocs_path = mkdocs_path if mkdocs_path is not None else MKDOCS_PATH
    text = mkdocs_path.read_text(encoding="utf-8")
    marker_at = text.find(NAV_PROBLEMS_MARKER)
    if marker_at == -1:
        raise SystemExit("mkdocs.yml has no Problems nav section to replace")
    section_at = marker_at + len(NAV_PROBLEMS_MARKER)
    next_top_at = len(text)
    for match in NAV_NEXT_TOP_PATTERN.finditer(text[section_at:]):
        next_top_at = section_at + match.start()
        break
    _grind, _neetcode, _amazon = load_validated_sources()
    merged = merge_tracks(_grind, _neetcode)
    verify_merge_shape(merged)
    updated = text[:marker_at] + render_problems_nav(merged) + text[next_top_at:]
    if updated == text:
        return False
    mkdocs_path.write_text(updated, encoding="utf-8")
    return True


# ---------------------------------------------------------------------------
# Idempotency check
# ---------------------------------------------------------------------------


def check(landing_path: Optional[Path] = None) -> int:
    """Exit 0 when every owned landing section matches a fresh render.

    Read-only: nothing is written or rewritten.

    Args:
        landing_path: Overrides the docs/problems/index.md path (default:
            module constant).

    Returns:
        A process exit code: 0 when identical, 1 with a diff summary otherwise.
    """
    landing_path = landing_path if landing_path is not None else PROBLEMS_INDEX_PATH
    stale: List[str] = []
    sections = render_sections()
    if not landing_path.exists():
        stale.append("docs/problems/index.md (missing)")
        text = ""
    else:
        text = landing_path.read_text(encoding="utf-8")
    for name, start_marker, end_marker, rendered in sections:
        start_at = text.find(start_marker)
        if start_at == -1:
            stale.append(f"docs/problems/index.md (no {name} markers)")
            continue
        end_at = text.find(end_marker, start_at)
        if end_at == -1:
            stale.append(f"docs/problems/index.md ({name} markers unclosed)")
            continue
        if text[start_at : end_at + len(end_marker)] != rendered.rstrip():
            stale.append(f"docs/problems/index.md ({name} section differs)")
    if stale:
        print(f"--check: {len(stale)} index section(s) differ from a fresh generation:")
        for item in stale[:20]:
            print(f"  {item}")
        return 1
    print(f"--check: {len(sections)} index sections up to date")
    return check_problems_nav()


def check_problems_nav(mkdocs_path: Optional[Path] = None) -> int:
    """Exit 0 when the committed mkdocs.yml Problems nav matches a fresh render.

    The audit compares the whole Problems span in mkdocs.yml (from the
    Problems marker through the next top-level nav entry, or the end of
    file) against a fresh render: rogue entries inside the section, child
    order, duplicates, extras, and omissions are all drift. The landing
    parent line and the Amazon OA subsection must both sit exactly where
    the fresh render puts them.

    Args:
        mkdocs_path: Overrides the mkdocs.yml path (default: module constant).

    Returns:
        A process exit code: 0 when the nav matches, 1 with a diff summary
        otherwise.
    """
    mkdocs_path = mkdocs_path if mkdocs_path is not None else MKDOCS_PATH
    stale: List[str] = []
    text = mkdocs_path.read_text(encoding="utf-8") if mkdocs_path.exists() else ""
    _grind, _neetcode, _amazon = load_validated_sources()
    merged = merge_tracks(_grind, _neetcode)
    verify_merge_shape(merged)
    fresh = render_problems_nav(merged)
    if not text:
        stale.append("mkdocs.yml (missing)")
    elif text.count(NAV_PROBLEMS_MARKER) != 1:
        stale.append("mkdocs.yml (Problems nav section not found exactly once)")
    else:
        at = text.find(NAV_PROBLEMS_MARKER)
        section_at = at + len(NAV_PROBLEMS_MARKER)
        next_top_at = len(text)
        for match in NAV_NEXT_TOP_PATTERN.finditer(text[section_at:]):
            next_top_at = section_at + match.start()
            break
        if text[at:next_top_at] != fresh:
            actual_children = nav_leetcode_children(text[at:])
            expected_children = [row["dirSlug"] for row in merged]
            detail = []
            if len(actual_children) != len(set(actual_children)):
                dupes = sorted(
                    {slug for slug in actual_children if actual_children.count(slug) > 1}
                )
                detail.append(f"duplicates: {', '.join(dupes[:5])}")
            extras = sorted(set(actual_children) - set(expected_children))
            if extras:
                detail.append(f"extra: {', '.join(extras[:5])}")
            missing = sorted(set(expected_children) - set(actual_children))
            if missing:
                detail.append(f"missing: {', '.join(missing[:5])}")
            if not detail:
                if actual_children != expected_children:
                    detail.append("child order drifts from the unified table")
                elif "    - problems/index.md" not in text[at:next_top_at]:
                    detail.append("no problems/index.md landing parent")
                else:
                    detail.append("unrecognized entries inside the Problems section")
            stale.append("mkdocs.yml (Problems nav drift: " + "; ".join(detail) + ")")
    if stale:
        print(f"--check: {len(stale)} nav audit finding(s):")
        for item in stale[:20]:
            print(f"  {item}")
        return 1
    print(f"--check: mkdocs Problems nav up to date ({len(merged)} LeetCode children)")
    return 0


def nav_leetcode_children(problems_text: str) -> List[str]:
    """Extract the LeetCode subsection's dirSlugs in file order.

    Args:
        problems_text: The mkdocs.yml text starting at the Problems marker.

    Returns:
        The child dirSlugs between the LeetCode header and the first line
        that is not a LeetCode child; empty when the header is absent.
    """
    header_at = problems_text.find(NAV_LEETCODE_HEADER)
    if header_at == -1:
        return []
    children: List[str] = []
    for line in problems_text[header_at + len(NAV_LEETCODE_HEADER) :].splitlines():
        match = NAV_LEETCODE_CHILD_PATTERN.match(line)
        if match is None:
            break
        children.append(match.group(2))
    return children


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------


def main(argv: Optional[Sequence[str]] = None) -> int:
    """Run the generator CLI.

    Args:
        argv: Command-line arguments (defaults to sys.argv[1:]).

    Returns:
        Process exit code.
    """
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--check", action="store_true", help="Verify the index sections match a fresh generation; exit 0 when up to date")
    args = parser.parse_args(argv)

    grind, neetcode, amazon = load_validated_sources()
    print(
        f"sources: {len(grind)} Grind 75 rows, {len(neetcode)} NeetCode 150 entries,"
        f" {len(amazon)} Amazon OA entries validated"
    )

    if args.check:
        # --check is read-only verification: it never writes.
        return check()

    landing_written = write_sections()
    print(
        "landing: sections written"
        if landing_written
        else "landing: sections already up to date"
    )
    if write_problems_nav():
        print("nav: Problems section written")
    else:
        print("nav: Problems section already up to date")
    return 0


if __name__ == "__main__":
    sys.exit(main())
