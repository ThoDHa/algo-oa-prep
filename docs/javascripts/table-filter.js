// Header-integrated filtering for the problem tables.
//
// Companion to tablesort-init.js: the two problem tables on the problems
// landing get their filters folded into their header cells - a search icon
// in the Problem header expanding an inline case-insensitive text input, a
// caret-styled native select on the Difficulty header (the Time header on
// the Amazon OA table, whose Time cell is the difficulty source) and on
// Tracks where that column exists, a small caption line under the table
// announcing the visible row count, an icon clear button in the Problem
// header shown only while a filter is active, and the reset-sort action
// folded in as an icon in the last header. A table counts as filterable
// when its header row has a Problem column and a Difficulty or Time column
// - the columns the filters can actually work on - so every other article
// table (pattern guides, sources, the Amazon OA bank index, whose
// Problem/Updated/Companies header offers no difficulty source) stays
// untouched. Like tablesort-init.js, per-page work subscribes to document$
// for instant navigation: each swap delivers fresh tables, and the data
// attribute guard keeps repeat emissions from stacking duplicate controls
// over the same DOM. Because the controls live inside the table's header
// cells and its caption, a swap replaces them together with the table, so
// filter state resets on navigation instead of persisting.
//
// Tablesort binds its sort toggle to clicks on the header cell itself, so
// every interactive element added to a header stops click propagation from
// itself only; clicks on the header text still sort, and the cells are
// augmented in place, never reordered or removed, leaving the sort cycle
// and aria-sort handling alone.
//
// Filterable tables supersede tablesort-init's standalone "Reset sort"
// button: at install time that button is still the table's previous sibling
// (the sort module's subscription runs first), so it is removed by its
// marker attribute and rebuilt as a header icon bound to the same
// resetTablesortState. Tables without filters keep the standalone button,
// and both files degrade independently when the other is absent.
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
const ALL_OPTION_LABEL = "All";
const PROBLEM_INPUT_WIDTH = "14rem";
const HEADER_CONTROL_GAP = "0.15rem";
const CAPTION_TOP_PADDING = "0.4rem";
const CAPTION_FONT_SIZE = "0.64rem";
const CAPTION_OPACITY = "0.75";
const SVG_NAMESPACE = "http://www.w3.org/2000/svg";

// Feather icon geometry (MIT-licensed set), drawn through createElementNS so
// the headers gain icons without an icon font dependency or CSP-hostile
// markup.
const SEARCH_ICON = [
  ["circle", { cx: "11", cy: "11", r: "8" }],
  ["line", { x1: "21", y1: "21", x2: "16.65", y2: "16.65" }],
];
const CLOSE_ICON = [
  ["line", { x1: "18", y1: "6", x2: "6", y2: "18" }],
  ["line", { x1: "6", y1: "6", x2: "18", y2: "18" }],
];
const RESET_ICON = [
  ["polyline", { points: "1 4 1 10 7 10" }],
  ["path", { d: "M3.51 15a9 9 0 1 0 2.13-9.36L1 10" }],
];

/** First header row of a table, whether or not it has a thead. */
const headerRowOf = (table) => (table.tHead ? table.tHead.rows[0] : table.rows[0]);

/** Maps each filterable column's header text to its cell index. */
const columnMap = (table) => {
  const columns = {
    problem: -1,
    difficulty: -1,
    tracks: -1,
    time: -1,
  };
  Array.from(headerRowOf(table).cells).forEach((cell, index) => {
    const name = cell.textContent.trim().toLowerCase();
    if (name in columns) {
      columns[name] = index;
    }
  });
  return columns;
};

/** True when the column map has the problem-table shape: a Problem column plus a Difficulty or Time column. */
const isFilterable = (columns) =>
  columns.problem !== -1 && (columns.difficulty !== -1 || columns.time !== -1);

/** Indices applyFilters reads from a row; a short row missing any of them degrades to unfiltered. */
const requiredColumns = (columns) => {
  const indices = [columns.problem];
  if (columns.difficulty !== -1) {
    indices.push(columns.difficulty);
  } else if (columns.time !== -1) {
    indices.push(columns.time);
  }
  if (columns.tracks !== -1) {
    indices.push(columns.tracks);
  }
  return indices;
};

/** True when the row has a cell at every index applyFilters reads. */
const rowCoversColumns = (row, requiredIndices) =>
  requiredIndices.every((index) => index < row.cells.length);

/** Trimmed text of the row's cell at the column index. */
const cellText = (row, columnIndex) => row.cells[columnIndex].textContent.trim();

/** Difficulty label for a row: its Difficulty cell, or the estimate derived from its Time cell. */
const difficultyOf = (row, columns) => {
  if (columns.difficulty !== -1) {
    return cellText(row, columns.difficulty);
  }
  return TIME_TO_DIFFICULTY[cellText(row, columns.time)] ?? UNKNOWN_DIFFICULTY;
};

/** Builds an inline CSP-safe icon from Feather geometry via createElementNS. */
const buildIcon = (drawing) => {
  const svg = document.createElementNS(SVG_NAMESPACE, "svg");
  for (const [attribute, value] of Object.entries({
    viewBox: "0 0 24 24",
    width: "1em",
    height: "1em",
    fill: "none",
    stroke: "currentColor",
    "stroke-width": "2",
    "stroke-linecap": "round",
    "stroke-linejoin": "round",
    "aria-hidden": "true",
  })) {
    svg.setAttribute(attribute, value);
  }
  for (const [tag, attributes] of drawing) {
    const shape = document.createElementNS(SVG_NAMESPACE, tag);
    for (const [attribute, value] of Object.entries(attributes)) {
      shape.setAttribute(attribute, value);
    }
    svg.append(shape);
  }
  return svg;
};

/** Builds a borderless header icon button; its clicks stop at the button so tablesort's header-click sort never fires from a filter control. */
const buildHeaderIconButton = (label, drawing) => {
  const button = document.createElement("button");
  button.type = "button";
  button.setAttribute("aria-label", label);
  button.append(buildIcon(drawing));
  button.style.backgroundColor = "transparent";
  button.style.border = "none";
  button.style.color = "inherit";
  button.style.cursor = "pointer";
  button.style.padding = "0";
  button.style.display = "inline-flex";
  button.style.alignItems = "center";
  button.addEventListener("click", (event) => {
    event.stopPropagation();
  });
  return button;
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
  select.setAttribute("aria-label", label);
  for (const optionLabel of [allOptionLabel, ...optionLabels]) {
    const option = document.createElement("option");
    option.value = optionLabel === allOptionLabel ? ALL_OPTION_VALUE : optionLabel;
    option.textContent = optionLabel;
    select.append(option);
  }
  return select;
};

/** Builds the caption-style line attached under the table announcing how many rows are visible. */
const buildCountCaption = () => {
  const caption = document.createElement("caption");
  caption.style.captionSide = "bottom";
  caption.style.textAlign = "left";
  caption.style.paddingTop = CAPTION_TOP_PADDING;
  caption.style.fontSize = CAPTION_FONT_SIZE;
  caption.style.opacity = CAPTION_OPACITY;
  caption.setAttribute("aria-live", "polite");
  return caption;
};

/** True when tablesort-init stamped the rows with their default order. */
const isDefaultOrderStamped = (table) => {
  const firstRow = table.tBodies[0]?.rows[0];
  return firstRow !== undefined && firstRow.dataset.defaultIndex !== undefined;
};

/** Builds the reset-sort header icon restoring default row order and sort state; null when the sort module is absent or the table carries no default-order stamps (unstamped rows would be reordered into a scrambled, NaN-driven order). */
const buildResetButton = (table) => {
  if (
    typeof resetTablesortState !== "function" ||
    !isDefaultOrderStamped(table)
  ) {
    return null;
  }
  const button = buildHeaderIconButton("Reset sort", RESET_ICON);
  button.setAttribute("aria-controls", table.id);
  button.addEventListener("click", () => resetTablesortState(table));
  return button;
};

/** Removes tablesort-init's standalone reset button; the header icon supersedes it here. */
const removeStandaloneReset = (table) => {
  const standalone = table.previousElementSibling;
  if (standalone?.matches("button[data-tablesort-reset]")) {
    standalone.remove();
  }
};

/** True when any control holds a non-default value, judged the way applyFilters judges it (trimmed). */
const isFilterActive = (controls) =>
  controls.text.value.trim() !== "" ||
  controls.selects.some((select) => select.value !== ALL_OPTION_VALUE);

/** Hides non-matching rows, updates the live count, and mirrors the clear icon's visibility. */
const applyFilters = (table, controls) => {
  const query = controls.text.value.trim().toLowerCase();
  const difficulty = controls.difficulty ? controls.difficulty.value : "";
  const track = controls.tracks ? controls.tracks.value.toLowerCase() : "";
  const requiredIndices = requiredColumns(controls.columns);
  let visible = 0;
  for (const body of table.tBodies) {
    for (const row of body.rows) {
      if (!rowCoversColumns(row, requiredIndices)) {
        continue;
      }
      const matches =
        (!query ||
          cellText(row, controls.columns.problem).toLowerCase().includes(query)) &&
        (!difficulty || difficultyOf(row, controls.columns) === difficulty) &&
        (!track ||
          cellText(row, controls.columns.tracks).toLowerCase().includes(track));
      row.style.display = matches ? "" : "none";
      if (matches) {
        visible += 1;
      }
    }
  }
  controls.count.textContent = `${visible} of ${controls.total} problems`;
  controls.clearButton.style.display = isFilterActive(controls)
    ? "inline-flex"
    : "none";
};

/** Reveals the problem input, marks the search toggle expanded, and focuses the input. */
const expandInput = (controls) => {
  controls.text.style.display = "";
  controls.searchButton.setAttribute("aria-expanded", "true");
  controls.text.focus();
};

/** Collapses the problem input and marks the search toggle collapsed. */
const condenseInput = (controls) => {
  controls.text.style.display = "none";
  controls.searchButton.setAttribute("aria-expanded", "false");
};

/** Empties every filter control, collapses the input, and reapplies, leaving sort state untouched. */
const clearFilters = (table, controls) => {
  controls.text.value = "";
  condenseInput(controls);
  for (const select of controls.selects) {
    select.value = ALL_OPTION_VALUE;
  }
  applyFilters(table, controls);
};

/** Augments the Problem th with the search toggle, the expanding input, and the conditional clear icon. */
const installProblemControls = (table, headerRow, controls) => {
  const searchButton = buildHeaderIconButton("Search problems", SEARCH_ICON);
  searchButton.setAttribute("aria-expanded", "false");
  searchButton.setAttribute("aria-controls", table.id);
  const clearButton = buildHeaderIconButton("Clear filters", CLOSE_ICON);
  clearButton.setAttribute("aria-controls", table.id);
  clearButton.style.display = "none";
  controls.text.style.display = "none";
  const cluster = document.createElement("span");
  cluster.style.display = "inline-flex";
  cluster.style.alignItems = "center";
  cluster.style.gap = HEADER_CONTROL_GAP;
  // Filter chrome, not header text: clicks anywhere in the cluster,
  // including the gap strip between controls, must not reach the header's
  // sort toggle.
  cluster.addEventListener("click", (event) => {
    event.stopPropagation();
  });
  cluster.append(searchButton, controls.text, clearButton);
  headerRow.cells[controls.columns.problem].append(cluster);

  searchButton.addEventListener("click", () => expandInput(controls));
  controls.text.addEventListener("input", () => applyFilters(table, controls));
  controls.text.addEventListener("blur", () => {
    if (controls.text.value) {
      return;
    }
    // Deferred past the in-flight click: collapsing synchronously on blur
    // shrinks the cluster between mousedown and mouseup, which can retarget
    // the click onto the header and fire a sort from the gap strip.
    window.setTimeout(() => {
      if (!controls.text.value) {
        condenseInput(controls);
      }
    }, 0);
  });
  controls.text.addEventListener("keydown", (event) => {
    if (event.key === "Escape") {
      clearFilters(table, controls);
      searchButton.focus();
    }
  });
  clearButton.addEventListener("click", () => clearFilters(table, controls));
  controls.searchButton = searchButton;
  controls.clearButton = clearButton;
};

/** Folds a filter select into its header cell, styled to read as header text plus the native caret. */
const installHeaderSelect = (table, headerRow, controls, select, columnIndex) => {
  select.style.font = "inherit";
  select.style.color = "inherit";
  select.style.backgroundColor = "transparent";
  select.style.border = "none";
  select.style.padding = "0";
  select.style.cursor = "pointer";
  headerRow.cells[columnIndex].append(select);
  select.addEventListener("click", (event) => {
    event.stopPropagation();
  });
  select.addEventListener("change", () => applyFilters(table, controls));
  select.addEventListener("keydown", (event) => {
    if (event.key === "Escape") {
      clearFilters(table, controls);
    }
  });
};

/** Inserts the header controls, the count caption, and the event wiring. */
const installFilterControls = (table, columns) => {
  const headerRow = headerRowOf(table);
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
    count: buildCountCaption(),
    searchButton: null,
    clearButton: null,
  };
  installProblemControls(table, headerRow, controls);
  if (columns.difficulty !== -1 || columns.time !== -1) {
    const optionLabels =
      columns.difficulty === -1 ? [...DIFFICULTY_OPTIONS, UNKNOWN_DIFFICULTY] : DIFFICULTY_OPTIONS;
    const difficultyColumnIndex =
      columns.difficulty !== -1 ? columns.difficulty : columns.time;
    controls.difficulty = buildSelect(
      "Filter by difficulty",
      ALL_OPTION_LABEL,
      optionLabels
    );
    controls.selects.push(controls.difficulty);
    installHeaderSelect(table, headerRow, controls, controls.difficulty, difficultyColumnIndex);
  }
  if (columns.tracks !== -1) {
    controls.tracks = buildSelect("Filter by tracks", ALL_OPTION_LABEL, TRACK_OPTIONS);
    controls.selects.push(controls.tracks);
    installHeaderSelect(table, headerRow, controls, controls.tracks, columns.tracks);
  }
  const resetButton = buildResetButton(table);
  if (resetButton) {
    headerRow.cells[headerRow.cells.length - 1].append(resetButton);
  }
  removeStandaloneReset(table);
  // Content model order: a table's caption belongs first, even when styled
  // to render along the bottom edge.
  table.prepend(controls.count);
  applyFilters(table, controls);
};

if (typeof document$ !== "undefined") {
  document$.subscribe(() => {
    for (const table of document.querySelectorAll(
      "article table:not([data-table-filter])"
    )) {
      const columns = columnMap(table);
      if (!isFilterable(columns)) {
        continue;
      }
      table.setAttribute("data-table-filter", "");
      installFilterControls(table, columns);
    }
  });
}
