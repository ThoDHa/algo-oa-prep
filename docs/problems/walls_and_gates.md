# [Walls And Gates](https://leetcode.com/problems/walls-and-gates/)

**Medium** | **NN minutes** | **Array, Breadth-First Search, Matrix**

> This problem is locked behind [LeetCode Premium](https://leetcode.com/problems/walls-and-gates/); read it free on [NeetCode](https://neetcode.io/problems/islands-and-treasure).

You are given a $m \times n$ 2D `grid` initialized with these three possible values:

1. `-1` - A water cell that *can not* be traversed.
2. `0` - A treasure chest.
3. `INF` - A land cell that *can* be traversed. We use the integer `2^31 - 1 = 2147483647` to represent `INF`.

Fill each land cell with the distance to its nearest treasure chest. If a land cell cannot reach a treasure chest then the value should remain `INF`.

Assume the grid can only be traversed up, down, left, or right.

Modify the `grid` **in-place**.

## Examples

### Example 1

**Input:**

```
[
  [2147483647,-1,0,2147483647],
  [2147483647,2147483647,2147483647,-1],
  [2147483647,-1,2147483647,-1],
  [0,-1,2147483647,2147483647]
]
```

**Output:**

```
[
  [3,-1,0,1],
  [2,2,1,-1],
  [1,-1,2,-1],
  [0,-1,3,4]
]
```

### Example 2

**Input:**

```
[
  [0,-1],
  [2147483647,2147483647]
]
```

**Output:**

```
[
  [0,-1],
  [1,2]
]
```

## Constraints

- `m == grid.length`
- `n == grid[i].length`
- `1 <= m, n <= 100`
- `grid[i][j]` is one of `{-1, 0, 2147483647}`

## Solutions

<!-- Scaffold placeholder: the worked derivation and solutions land
     on the solutions branch later. See ../_TEMPLATE.md for the
     expected layout, naming, and ordering conventions. -->
