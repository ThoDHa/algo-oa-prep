# [Cet Mean Rank Count](https://www.fastprep.io/problems/get-mean-rank-count)

**Hard** | **NN minutes** | **Array, Hash Table, Prefix Sum**

$23

## Examples

### Example 1

**Input:** `rank = [1, 2, 3, 4, 5]`

**Output:** `[1, 2, 3, 2, 1]`

**Explanation:** Read the above as 'For the mean x = 1, the group [1] has mean value 1. There is 1 group'. and so on. The full answer is [1, 2, 3, 2, 1].

### Example 2

**Input:** `rank = [4, 3, 2, 1]`

**Output:** `[1, 2, 2, 1]`

**Explanation:** x = 1 -> [1] x = 2 -> [3, 2, 1], [2] x = 3 -> [3], [4, 3, 2] x = 4 -> [4]

### Example 3

**Input:** `rank = [4, 7, 3, 6, 5, 2, 1]`

**Output:** `[1, 1, 1, 4, 4, 1, 1]`

**Explanation:** x = 1 -> [1] x = 2 -> [2] x = 3 -> [3] x = 4 -> [4], [3, 6, 5, 2], [7, 3, 6, 5, 2, 1], [4, 7, 3, 6, 5, 2 ,1] x = 5 -> [5], [7, 3], [4, 7, 3, 6] and [4, 7, 3, 6, 5] x = 6 -> [6] x = 7 -> [7]

## Constraints

- `1 <= n <= 1031 <= rank[i] <= nThe array rank contains all distinct elemens, and thus, is a permutation of {1..n}.`

## Solutions

<!-- Scaffold placeholder: the worked derivation and solutions land
     on the solutions branch later. See ../_TEMPLATE.md for the
     expected layout, naming, and ordering conventions. -->
