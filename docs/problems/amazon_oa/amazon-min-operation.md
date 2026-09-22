# [Min Operation](https://www.fastprep.io/problems/amazon-min-operation)

**Easy** | **NN minutes** | **Array, Greedy, Hash Table**

$23

## Examples

### Example 1

**Input:** `m = 5`
**Input:** `locations = [1, 8, 6, 7, 7]`

**Output:** `3`

**Explanation:** One optimal sequence is to ship products from different locations together whenever possible. For [1, 8, 6, 7, 7], pair locations 1 and 8, then pair 6 and one 7, then ship the remaining 7 alone. This takes 3 operations.

### Example 2

**Input:** `m = 4`
**Input:** `locations = [1, 3, 1, 2]`

**Output:** `2`

**Explanation:** Pair the products at locations 1 and 3, then pair the remaining products at locations 1 and 2. This ships all products in 2 operations.

## Constraints

- `1 <= m <= 105locations.length == m1 <= locations[i] <= 109`

## Solutions

<!-- Scaffold placeholder: the worked derivation and solutions land
     on the solutions branch later. See ../_TEMPLATE.md for the
     expected layout, naming, and ordering conventions. -->
