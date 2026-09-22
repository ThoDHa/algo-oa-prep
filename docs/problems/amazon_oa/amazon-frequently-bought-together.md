# [Frequently Bought Together](https://www.fastprep.io/problems/amazon-frequently-bought-together)

**Medium** | **NN minutes** | **Array, String, Hash Table, Sorting**

Amazon's Retail Analytics team wants to discover which pairs of items are most often bought together so they can create Frequently Bought Together bundles.During a short observation window, each customer order is recorded as a space-separated list of SKU strings, for example "B07 B08 B09". Within a single order, the same SKU may repeat, but repeats count only once toward a bundle.Your task is to find the pair of distinct SKUs that appears in the highest number of orders. If several pairs tie for first place, return the lexicographically smallest pair, comparing the first SKU and then the second SKU.

## Examples

### Example 1

**Input:** `orders = ["B07 B08 B09", "B07 B08", "B08 B09"]`

**Output:** `["B07", "B08"]`

**Explanation:** Order-level pairs:{B07, B08}, {B07, B09}, {B08, B09}{B07, B08}{B08, B09}The global counts are {B07, B08} -> 2, {B07, B09} -> 1, and {B08, B09} -> 2. The highest count is tied between {B07, B08} and {B08, B09}, so the lexicographic tie-break gives {B07, B08}.

## Constraints

<!-- Constraints not parseable from FastPrep for amazon-frequently-bought-together; fill them in. -->

## Solutions

<!-- Scaffold placeholder: the worked derivation and solutions land
     on the solutions branch later. See ../_TEMPLATE.md for the
     expected layout, naming, and ordering conventions. -->
