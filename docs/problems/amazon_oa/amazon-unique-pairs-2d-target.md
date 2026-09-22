# [Unique Pairs in a 2D Matrix Summing to Target](https://www.fastprep.io/problems/amazon-unique-pairs-2d-target)

**Easy** | **NN minutes** | **Array, Matrix, Hash Table, Two Pointers**

Given a rectangular integer matrix matrix whose values are globally unique and an integer target, return the number of unordered pairs of values whose sum is target.

Each pair must use two different cells. Count a value pair once regardless of order.

## Examples

### Example 1

**Input:** `matrix = [[1,5],[7,-1]]`, `target = 6`

**Output:** `2`

**Explanation:** The unordered pairs are (1, 5) and (-1, 7).

### Example 2

**Input:** `matrix = [[1,2],[3,4]]`, `target = 5`

**Output:** `2`

**Explanation:** The pairs are (1, 4) and (2, 3).

### Example 3

**Input:** `matrix = [[4]]`, `target = 8`

**Output:** `0`

**Explanation:** The one value cannot be paired with its own cell.

## Constraints

- `1 <= matrix.length, matrix[i].length.`
- `The matrix is rectangular and contains at most 100000 cells.`
- `-10^9 <= matrix[i][j], target <= 10^9.`
- `All matrix values are distinct.`

## Solutions

<!-- Scaffold placeholder: the worked derivation and solutions land
     on the solutions branch later. See ../_TEMPLATE.md for the
     expected layout, naming, and ordering conventions. -->
