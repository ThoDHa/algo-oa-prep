# [Count Islands with Eight-Direction Adjacency](https://www.fastprep.io/problems/amazon-islands-eight-direction)

**Medium** | **NN minutes** | **Array, Matrix, Depth First Search, Breadth First Search**

Given a rectangular binary matrix grid, return the number of islands.

An island is a maximal group of cells containing 1. Two land cells belong to the same island when they share an edge or a corner, so each cell can connect in any of the eight horizontal, vertical, or diagonal directions.

## Examples

### Example 1

**Input:** `grid = [[1,0,1],[0,1,0],[1,0,1]]`

**Output:** `1`

**Explanation:** Every land cell connects to the center diagonally, so all five cells form one island.

### Example 2

**Input:** `grid = [[1,1,0],[0,0,0],[0,1,1]]`

**Output:** `2`

**Explanation:** The upper-left and lower-right land groups do not touch, even at a corner.

### Example 3

**Input:** `grid = [[0,0],[0,0]]`

**Output:** `0`

**Explanation:** There are no land cells.

## Constraints

- `1 <= grid.length, grid[i].length <= 500.`
- `Every row has the same length.`
- `grid[i][j] is either 0 or 1.`
- `The matrix contains at most 100000 cells.`

## Solutions

<!-- Scaffold placeholder: the worked derivation and solutions land
     on the solutions branch later. See ../_TEMPLATE.md for the
     expected layout, naming, and ordering conventions. -->
