// Client-side filtering for the problem tables.
//
// Companion to tablesort-init.js: the two problem tables on the problems
// landing get a compact filter toolbar (problem text, difficulty, tracks
// where those columns exist, a live visible count, a clear button, and the
// reset-sort action folded in from tablesort-init). A table counts as
// filterable when its header row has a Problem column and a Time or Updated
// column, so every other article table (pattern guides, sources) stays
// untouched. Like tablesort-init.js, per-page work subscribes to document$
// for instant navigation, and the data attribute guard keeps repeat emissions
// from stacking duplicate toolbars: the toolbar is inserted into the article
// DOM above the table, so instant navigation caches it together with its
// listeners and whatever filter state the visitor left behind.
//
// Filterable tables supersede tablesort-init's standalone "Reset sort"
// button: at install time that button is still the table's previous sibling
// (the sort module's subscription runs first), so it is removed by its
// marker attribute and rebuilt as a compact toolbar control bound to the
// same resetTablesortState. Tables without a toolbar keep the standalone
// button, and both files degrade independently when the other is absent.
//
// Filtering only toggles row visibility, never row order, so Tablesort keeps
// working on the DOM it sees: hidden rows move with a sort but stay hidden,
// and Clear filters leaves sort state (aria-sort and row order) alone, while
// Reset sort leaves filter state alone.

// The Amazon OA table has no Difficulty column; its Time cell carries the
// difficulty-based estimates the table prose documents (Easy 15 / Medium 25 /
// Hard 40 minutes), with a dash where the difficulty is unknown.
const TIME_TO_DIFFICULTY = {
  "15 minutes": "Easy",
  "25 minutes": "Medium",
  "40 minutes": "Hard",
};
const UNKNOWN_DIFFICULTY = "Unknown";
const DIFFICULTY_OPTIONS = ["Easy", "Medium", "Hard"];
const TRACK_OPTIONS = ["Grind 75", "NeetCode 150", "Amazon OA"];
const ALL_OPTION_VALUE = "";
const TOOLBAR_GAP = "0.4rem";
const PROBLEM_INPUT_WIDTH = "14rem";
const BUTTON_COMPACT_PADDING = "0.2rem 0.8rem";

/** Maps each filterable column's header text to its cell index. */
const columnMap = (table) => {
  const headerRow = table.tHead ? table.tHead.rows[0] : table.rows[0];
  const columns = {
    problem: -1,
    difficulty: -1,
    tracks: -1,
    time: -1,
    updated: -1,
  };
  Array.from(headerRow.cells).forEach((cell, index) => {
    const name = cell.textContent.trim().toLowerCase();
    if (name in columns) {
      columns[name] = index;
    }
  });
  return columns;
};

/** True when the table is one of the problem tables: a Problem column plus a Time or Updated column. */
const isFilterable = (table) => {
  const columns = columnMap(table);
  return (
    columns.problem !== -1 &&
    (columns.time !== -1 || columns.updated !== -1)
  );
};

/** Trimmed text of the row's cell at the column index. */
const cellText = (row, columnIndex) => row.cells[columnIndex].textContent.trim();

/** Difficulty label for a row: its Difficulty cell, or the estimate derived from its Time cell. */
const difficultyOf = (row, columns) => {
  if (columns.difficulty !== -1) {
    return cellText(row, columns.difficulty);
  }
  return TIME_TO_DIFFICULTY[cellText(row, columns.time)] ?? UNKNOWN_DIFFICULTY;
};

/** Builds the case-insensitive problem-name text input. */
const buildTextInput = () => {
  const input = document.createElement("input");
  input.type = "text";
  input.className = "md-input";
  input.placeholder = "Filter by problem";
  input.setAttribute("aria-label", "Filter problems by name");
  input.style.width = PROBLEM_INPUT_WIDTH;
  return input;
};

/** Builds a filter select: an all-option with an empty value followed by one option per label. */
const buildSelect = (label, allOptionLabel, optionLabels) => {
  const select = document.createElement("select");
  select.className = "md-input";
  select.setAttribute("aria-label", label);
  for (const optionLabel of [allOptionLabel, ...optionLabels]) {
    const option = document.createElement("option");
    option.value = optionLabel === allOptionLabel ? ALL_OPTION_VALUE : optionLabel;
    option.textContent = optionLabel;
    select.append(option);
  }
  return select;
};

/** Builds the aria-live span announcing how many rows are visible. */
const buildCount = () => {
  const count = document.createElement("span");
  count.setAttribute("aria-live", "polite");
  return count;
};

/** Builds a compact toolbar button: Material's md-button at md-typeset scale. */
const buildToolbarButton = (label) => {
  const button = document.createElement("button");
  button.type = "button";
  button.className = "md-button";
  button.textContent = label;
  button.style.padding = BUTTON_COMPACT_PADDING;
  return button;
};

/** Builds the compact clear button that empties every control without touching sort state. */
const buildClearButton = (table, controls) => {
  const button = buildToolbarButton("Clear filters");
  button.setAttribute("aria-controls", table.id);
  button.addEventListener("click", () => {
    controls.text.value = "";
    for (const select of controls.selects) {
      select.value = ALL_OPTION_VALUE;
    }
    applyFilters(table, controls);
  });
  return button;
};

/** Builds the compact reset control restoring default row order and sort state; null when the sort module is absent. */
const buildResetButton = (table) => {
  if (typeof resetTablesortState !== "function") {
    return null;
  }
  const button = buildToolbarButton("Reset sort");
  button.setAttribute("aria-controls", table.id);
  button.addEventListener("click", () => resetTablesortState(table));
  return button;
};

/** Removes tablesort-init's standalone reset button; the toolbar's reset control supersedes it here. */
const removeStandaloneReset = (table) => {
  const standalone = table.previousElementSibling;
  if (standalone?.matches("button[data-tablesort-reset]")) {
    standalone.remove();
  }
};

/** Hides non-matching rows and updates the live count. */
const applyFilters = (table, controls) => {
  const query = controls.text.value.trim().toLowerCase();
  const difficulty = controls.difficulty ? controls.difficulty.value : "";
  const track = controls.tracks ? controls.tracks.value : "";
  let visible = 0;
  for (const body of table.tBodies) {
    for (const row of body.rows) {
      const matches =
        (!query ||
          cellText(row, controls.columns.problem).toLowerCase().includes(query)) &&
        (!difficulty || difficultyOf(row, controls.columns) === difficulty) &&
        (!track ||
          cellText(row, controls.columns.tracks).toLowerCase().includes(track.toLowerCase()));
      row.style.display = matches ? "" : "none";
      if (matches) {
        visible += 1;
      }
    }
  }
  controls.count.textContent = `${visible} of ${controls.total} problems`;
};

/** Inserts the filter toolbar in one row above the table and wires the control events. */
const installFilterControls = (table) => {
  const columns = columnMap(table);
  let total = 0;
  for (const body of table.tBodies) {
    total += body.rows.length;
  }
  const controls = {
    columns,
    total,
    text: buildTextInput(),
    difficulty: null,
    tracks: null,
    selects: [],
    count: buildCount(),
  };
  const toolbar = document.createElement("div");
  toolbar.style.display = "flex";
  toolbar.style.flexWrap = "wrap";
  toolbar.style.alignItems = "center";
  toolbar.style.gap = TOOLBAR_GAP;
  toolbar.style.marginBottom = "0.6rem";
  toolbar.append(controls.text);
  if (columns.difficulty !== -1 || columns.time !== -1) {
    const optionLabels =
      columns.difficulty === -1 ? [...DIFFICULTY_OPTIONS, UNKNOWN_DIFFICULTY] : DIFFICULTY_OPTIONS;
    controls.difficulty = buildSelect(
      "Filter by difficulty",
      "All difficulties",
      optionLabels
    );
    controls.selects.push(controls.difficulty);
    toolbar.append(controls.difficulty);
  }
  if (columns.tracks !== -1) {
    controls.tracks = buildSelect("Filter by tracks", "All tracks", TRACK_OPTIONS);
    controls.selects.push(controls.tracks);
    toolbar.append(controls.tracks);
  }
  toolbar.append(controls.count, buildClearButton(table, controls));
  const resetButton = buildResetButton(table);
  if (resetButton) {
    toolbar.append(resetButton);
  }
  removeStandaloneReset(table);
  controls.text.addEventListener("input", () => applyFilters(table, controls));
  for (const select of controls.selects) {
    select.addEventListener("change", () => applyFilters(table, controls));
  }
  applyFilters(table, controls);
  table.before(toolbar);
};

if (typeof document$ !== "undefined") {
  document$.subscribe(() => {
    for (const table of document.querySelectorAll(
      "article table:not([data-table-filter])"
    )) {
      if (!isFilterable(table)) {
        continue;
      }
      table.setAttribute("data-table-filter", "");
      installFilterControls(table);
    }
  });
}
