# [Min Time to Create Beautiful Canvas](https://www.fastprep.io/problems/amazon-find-minimum-time-to-create-beautiful-canvas)

**Hard** | **NN minutes** | **Matrix, Binary Search, Prefix Sum**

$24

## Examples

### Example 1

**Input:** `n = 2`
**Input:** `m = 3`
**Input:** `k = 2`
**Input:** `paint = [[1, 2], [2, 3], [2, 1], [1, 3], [2, 2], [1, 1]]`

**Output:** `5`

**Explanation:** After the 5th and 6th minutes, the canvas has a square of size 2*2 with all black cells starting at position (1, 2) at minute 5, and two squares at (1,1) and (1,2) at minute 6, so the minimum time after which the canvas becomes beautiful is 5 minutes.

## Constraints

- `1 ≤ n, m ≤ 750`
- `1 ≤ k ≤ min(n, m)`
- `1 ≤ paint[i][0] ≤ n`
- `1 ≤ paint[i][1] ≤ m`
- `paint[i] ≠ paint[j] for any 1 ≤ i < j ≤ n*m`

## Solutions

<!-- Scaffold placeholder: the worked derivation and solutions land
     on the solutions branch later. See ../_TEMPLATE.md for the
     expected layout, naming, and ordering conventions. -->
