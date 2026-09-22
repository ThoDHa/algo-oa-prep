# [Pacific Atlantic Water Flow](https://leetcode.com/problems/pacific-atlantic-water-flow/)

**Medium** | **NN minutes** | **Array, Depth-First Search, Breadth-First Search, Matrix**

You are given a rectangular island `heights` where `heights[r][c]` represents the **height above sea level** of the cell at coordinate `(r, c)`.

The islands borders the **Pacific Ocean** from the top and left sides, and borders the **Atlantic Ocean** from the bottom and right sides.

Water can flow in **four directions** (up, down, left, or right) from a cell to a neighboring cell with **height equal or lower**. Water can also flow into the ocean from cells adjacent to the ocean.

Find all cells where water can flow from that cell to **both** the Pacific and Atlantic oceans. Return it as a **2D list** where each element is a list `[r, c]` representing the row and column of the cell. You may return the answer in **any order**.

## Examples

### Example 1

**Input:**

```
heights = [
  [4,2,7,3,4],
  [7,4,6,4,7],
  [6,3,5,3,6]
]
```

**Output:**

```
[[0,2],[0,4],[1,0],[1,1],[1,2],[1,3],[1,4],[2,0]]
```

### Example 2

**Input:** `heights = [[1],[1]]`

**Output:** `[[0,0],[1,0]]`

## Constraints

- `1 <= heights.length, heights[r].length <= 100`
- `0 <= heights[r][c] <= 1000`

## Solutions

<!-- Scaffold placeholder: the worked derivation and solutions land
     on the solutions branch later. See _TEMPLATE.md for the
     expected layout, naming, and ordering conventions. -->
