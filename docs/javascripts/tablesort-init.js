// Sortable problem tables.
//
// Material 9.7.6 free ships no table sorting, so the problem tables use
// tristen/tablesort, loaded from the unpkg entry above this file in
// mkdocs.yml. Per the theme's customization guidance, per-page JavaScript
// subscribes to the document$ observable so it re-runs on every page swap
// under navigation.instant.
//
// Tablesort's default type detection handles the table contents: the Time
// column's "15 minutes" cells sort numerically (the number comparator
// strips non-numeric text), with "-" cells clustering at one end.
//
// The data attribute keeps repeat document$ emissions from re-initializing
// an already-sorted table, which would stack duplicate click handlers.
document$.subscribe(() => {
  if (typeof Tablesort === "undefined") {
    return;
  }
  for (const table of document.querySelectorAll("article table:not([data-tablesort])")) {
    table.setAttribute("data-tablesort", "");
    new Tablesort(table);
  }
});
