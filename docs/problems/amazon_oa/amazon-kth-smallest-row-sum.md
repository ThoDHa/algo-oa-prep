# [Kth Smallest Sum from Sorted Matrix Rows](https://www.fastprep.io/problems/amazon-kth-smallest-row-sum)

**Hard** | **NN minutes** | **Array, Matrix, Heap**

Given an integer matrix mat whose rows are sorted in nondecreasing order, choose exactly one value from each row and add the chosen values.Return the kth smallest obtainable sum. Distinct choices occupy distinct ranks even when they produce equal sums.

## Examples

### Example 1

**Input:** `mat = [[1,3,11],[2,4,6]]`
**Input:** `k = 5`

**Output:** `7`

**Explanation:** The ordered sums begin 3, 5, 5, 7, 7, so the fifth sum is 7.

### Example 2

**Input:** `mat = [[1,3,11],[2,4,6]]`
**Input:** `k = 9`

**Output:** `17`

**Explanation:** There are nine selections, and the largest and ninth ordered sum is 11 + 6 = 17.

### Example 3

**Input:** `mat = [[1,10,10],[1,4,5],[2,3,6]]`
**Input:** `k = 7`

**Output:** `9`

**Explanation:** Counting equal sums from different selections separately, the seventh ordered sum is 9.

## Constraints

- `1 <= mat.length, mat[i].length <= 40.All rows have the same length and are sorted in nondecreasing order.1 <= mat[i][j] <= 5000.1 <= k <= min(200, mat[i].length^mat.length).`

## Solutions

<!-- Scaffold placeholder: the worked derivation and solutions land
     on the solutions branch later. See ../_TEMPLATE.md for the
     expected layout, naming, and ordering conventions. -->
