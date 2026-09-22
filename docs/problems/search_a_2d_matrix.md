# [Search a 2D Matrix](https://leetcode.com/problems/search-a-2d-matrix/)

**Medium** | **NN minutes** | **Array, Binary Search, Matrix**

You are given an `m x n` 2-D integer array `matrix` and an integer `target`.

* Each row in `matrix` is sorted in *non-decreasing* order.
* The first integer of every row is greater than the last integer of the previous row.

Return `true` if `target` exists within `matrix` or `false` otherwise.

Can you write a solution that runs in `O(log(m * n))` time?

## Examples

### Example 1

**Input:** `matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]], target = 10`

**Output:** `true`

### Example 2

**Input:** `matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]], target = 15`

**Output:** `false`

## Constraints

- `m == matrix.length`
- `n == matrix[i].length`
- `1 <= m, n <= 100`
- `-10000 <= matrix[i][j], target <= 10000`

## Solutions

<!-- Scaffold placeholder: the worked derivation and solutions land
     on the solutions branch later. See _TEMPLATE.md for the
     expected layout, naming, and ordering conventions. -->
