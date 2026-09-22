# [Find the Safest Path in a Grid](https://www.fastprep.io/problems/amazon-find-safest-path-in-grid)

**Hard** | **NN minutes** | **Array, Matrix, Breadth First Search, Binary Search, Heap, Shortest Path**

You are given an n x n binary matrix grid. A cell containing 1 contains a thief, and a cell containing 0 is empty.Start at (0, 0) and move to (n - 1, n - 1). Each move goes one cell up, down, left, or right, and a path may pass through a thief cell.The safeness factor of a path is the minimum Manhattan distance from any cell on that path to any thief in the grid. Return the maximum safeness factor among all paths from the start to the destination.The Manhattan distance between (r, c) and (x, y) is |r - x| + |c - y|.

## Examples

### Example 1

**Input:** `grid = [[1,0,0],[0,0,0],[0,0,1]]`

**Output:** `0`

**Explanation:** The start and destination both contain thieves, so every path has safeness factor 0.

### Example 2

**Input:** `grid = [[0,0,1],[0,0,0],[0,0,0]]`

**Output:** `2`

**Explanation:** A path through the left and bottom area stays at least Manhattan distance 2 from the thief at (0, 2), and no path can do better.

### Example 3

**Input:** `grid = [[0,0,0,1],[0,0,0,0],[0,0,0,0],[1,0,0,0]]`

**Output:** `2`

**Explanation:** A route through the central corridor remains at least distance 2 from both corner thieves.

## Constraints

- `1 <= grid.length == n <= 400grid[i].length == ngrid[i][j] is 0 or 1.The grid contains at least one thief.`

## Solutions

<!-- Scaffold placeholder: the worked derivation and solutions land
     on the solutions branch later. See ../_TEMPLATE.md for the
     expected layout, naming, and ordering conventions. -->
