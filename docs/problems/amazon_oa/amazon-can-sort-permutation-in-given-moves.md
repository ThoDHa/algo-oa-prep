# [Sort Permutation](https://www.fastprep.io/problems/amazon-can-sort-permutation-in-given-moves)

**Medium** | **NN minutes** | **Math, Graph**

$23

## Examples

### Example 1

**Input:** `p = [2, 3, 1, 4]`
**Input:** `moves = [2, 3]`

**Output:** `"10"`

**Explanation:** The cycle (1, 2, 3) needs exactly two swaps, so query 2 succeeds. Every swap changes permutation parity, so an odd count of three cannot finish at the sorted permutation.

### Example 2

**Input:** `p = [4, 5, 1, 3, 2]`
**Input:** `moves = [1, 2, 3]`

**Output:** `"001"`

**Explanation:** The permutation consists of cycles of lengths three and two, so it needs at least (3 - 1) + (2 - 1) = 3 swaps. Therefore one and two moves fail, while three moves succeed; for example, swap indexes (0, 2), then (1, 4), then (2, 3).

## Constraints

- `1 <= n <= 10^5`
- `1 <= q <= 10^5`
- `1 <= moves[i] <= 10^9`
- `It is guaranteed that p forms a permutation.`

## Solutions

<!-- Scaffold placeholder: the worked derivation and solutions land
     on the solutions branch later. See ../_TEMPLATE.md for the
     expected layout, naming, and ordering conventions. -->
