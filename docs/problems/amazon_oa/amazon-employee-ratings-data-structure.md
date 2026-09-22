# [Employee Ratings Management System](https://www.fastprep.io/problems/amazon-employee-ratings-data-structure)

**Hard** | **NN minutes** | **Array, Segment Tree, Binary Search, Design**

Process a sequence of operations on an initially empty ordered list of employee ratings. Operation [1, rating] appends a rating. Operation [2, index] deletes the rating at the current zero-based index, shifting later indices left. Operation [3] queries the maximum rating and its earliest current index.Return one row [maximumRating, earliestIndex] for every query operation. Every deletion index is valid, and every query occurs while at least one rating exists.

## Examples

### Example 1

**Input:** `operations = [[1,5],[1,7],[1,7],[3],[2,1],[3]]`

**Output:** `[[7,1],[7,1]]`

**Explanation:** The first maximum is at index 1; after deleting it, the remaining 7 shifts to index 1.

### Example 2

**Input:** `operations = [[1,-2],[3],[1,4],[3]]`

**Output:** `[[-2,0],[4,1]]`

**Explanation:** Queries reflect both negative and later positive ratings.

### Example 3

**Input:** `operations = [[1,3],[1,1],[2,0],[3]]`

**Output:** `[[1,0]]`

**Explanation:** Deleting index zero shifts the remaining rating to zero.

## Constraints

- `1 &le; operations.length &le; 100000.Each operation is exactly one of [1, rating], [2, index], or [3].-10^9 &le; rating &le; 10^9.Deletion indices and non-empty query preconditions are valid.`

## Solutions

<!-- Scaffold placeholder: the worked derivation and solutions land
     on the solutions branch later. See ../_TEMPLATE.md for the
     expected layout, naming, and ordering conventions. -->
