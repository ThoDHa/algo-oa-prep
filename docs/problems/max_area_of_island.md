# [Max Area of Island](https://leetcode.com/problems/max-area-of-island/)

**Medium** | **NN minutes** | **Array, Depth-First Search, Breadth-First Search, Union Find, Matrix**

You are given a matrix `grid` where `grid[i]` is either a `0` (representing water) or `1` (representing land).

An island is defined as a group of `1`'s connected horizontally or vertically. You may assume all four edges of the grid are surrounded by water.

The **area** of an island is defined as the number of cells within the island.

Return the maximum **area** of an island in `grid`. If no island exists, return `0`.

## Examples

### Example 1

**Input:**

```
grid = [
  [0,1,1,0,1],
  [1,0,1,0,1],
  [0,1,1,0,1],
  [0,1,0,0,1]
]
```

**Output:**

```
6
```

**Explanation:** `1`'s cannot be connected diagonally, so the maximum area of the island is `6`.

## Constraints

- `1 <= grid.length, grid[i].length <= 50`

## Solutions

<!-- Scaffold placeholder: the worked derivation and solutions land
     on the solutions branch later. See _TEMPLATE.md for the
     expected layout, naming, and ordering conventions. -->
