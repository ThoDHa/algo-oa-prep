# [Minimum Time to Spread Through a Grid](https://www.fastprep.io/problems/amazon-rotting-oranges-variation)

**Medium** | **NN minutes** | **Array, Breadth First Search, Matrix**

You are given a rectangular grid whose cells contain 0, 1, or 2. A zero is empty, a one is fresh, and a two is already active.After each minute, every active cell makes each orthogonally adjacent fresh cell active. Return the minimum number of minutes until no fresh cell remains. Return -1 when this is impossible.

## Examples

### Example 1

**Input:** `grid = [[2,1,1],[1,1,0],[0,1,1]]`

**Output:** `4`

**Explanation:** The wave reaches the lower-right fresh cell after four minutes.

### Example 2

**Input:** `grid = [[2,1,1],[0,1,1],[1,0,1]]`

**Output:** `-1`

**Explanation:** The isolated fresh cell in the lower-left corner is unreachable.

### Example 3

**Input:** `grid = [[0,2]]`

**Output:** `0`

**Explanation:** There are no fresh cells, so no minute needs to pass.

## Constraints

- `1 <= grid.length, grid[r].length <= 200Every row has the same length.grid[r][c] is 0, 1, or 2.`

## Solutions

<!-- Scaffold placeholder: the worked derivation and solutions land
     on the solutions branch later. See ../_TEMPLATE.md for the
     expected layout, naming, and ordering conventions. -->
