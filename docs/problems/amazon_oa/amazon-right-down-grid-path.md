# [Path Through an O/X Grid Using Only Right and Down](https://www.fastprep.io/problems/amazon-right-down-grid-path)

**Medium** | **NN minutes** | **Array, Matrix, Dynamic Programming, Breadth First Search**

Given a rectangular array of strings grid, a zero-based coordinate source = [row, col], and a zero-based coordinate destination = [row, col], return whether the destination is reachable.The character O is open and X is blocked. From an open cell you may move exactly one cell right or one cell down. A blocked endpoint is unreachable, and a destination above or left of the source is also unreachable.

## Examples

### Example 1

**Input:** `grid = ["OOO","OXO","OOO"]`
**Input:** `source = [0,0]`
**Input:** `destination = [2,2]`

**Output:** `true`

**Explanation:** Move right twice and then down twice while avoiding the center obstacle.

### Example 2

**Input:** `grid = ["OX","XO"]`
**Input:** `source = [0,0]`
**Input:** `destination = [1,1]`

**Output:** `false`

**Explanation:** Both first moves enter blocked cells.

### Example 3

**Input:** `grid = ["OOO"]`
**Input:** `source = [0,2]`
**Input:** `destination = [0,0]`

**Output:** `false`

**Explanation:** Reaching the destination would require moving left.

## Constraints

- `1 <= grid.length, grid[i].length <= 500.Every row has the same length, and the grid has at most 250000 cells.Every cell is O or X.source and destination each contain exactly two valid grid coordinates.`

## Solutions

<!-- Scaffold placeholder: the worked derivation and solutions land
     on the solutions branch later. See ../_TEMPLATE.md for the
     expected layout, naming, and ordering conventions. -->
