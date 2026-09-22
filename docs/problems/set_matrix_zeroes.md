# [Set Matrix Zeroes](https://leetcode.com/problems/set-matrix-zeroes/)

**Medium** | **NN minutes** | **Array, Hash Table, Matrix**

Given an `m x n` matrix of integers `matrix`, if an element is `0`, set its entire row and column to `0`'s.

You must update the matrix *in-place*.

## Examples

### Example 1

**Input:**

```
matrix = [
  [0,1],
  [1,0]
]
```

**Output:**

```
[
  [0,0],
  [0,0]
]
```

### Example 2

**Input:**

```
matrix = [
  [1,2,3],
  [4,0,5],
  [6,7,8]
]
```

**Output:**

```
[
  [1,0,3],
  [0,0,0],
  [6,0,8]
]
```

## Constraints

- `m == matrix.length`
- `n == matrix[0].length`
- `1 <= m, n <= 200`
- `-2^31 <= matrix[i][j] <= (2^31) - 1`

## Follow-up

Could you solve it using `O(1)` space?

## Solutions

<!-- Scaffold placeholder: the worked derivation and solutions land
     on the solutions branch later. See _TEMPLATE.md for the
     expected layout, naming, and ordering conventions. -->
