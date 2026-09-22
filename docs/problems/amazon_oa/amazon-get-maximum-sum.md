# [Get Maximum Sum](https://www.fastprep.io/problems/amazon-get-maximum-sum)

**Easy** | **NN minutes** | **Hash Table, Sorting, Greedy**

$23

## Examples

### Example 1

**Input:** `health = [4, 5, 5, 6]`
**Input:** `serverType = [1, 2, 1, 2]`
**Input:** `k = 1`

**Output:** `11`

**Explanation:** Since k = 1, all selected servers must be the same type. The better option is to select type 2 servers. The maximum sum of health for type 2 servers is 5 + 6 = 11. Return 11.

### Example 2

**Input:** `health = [1, 2, 3, 10, 10]`
**Input:** `serverType = [3, 3, 1, 2, 5]`
**Input:** `k = 2`

**Output:** `20`

**Explanation:** With k = 2, the best option is to select servers of types 1 and 5. The maximum sum of health for these types is 2 + 3 + 10 = 15 for type 1 and 10 for type 5, which adds up to 20. Return 20.

## Constraints

- `1 ≤ k ≤ n ≤ 10^5`
- `1 ≤ health[i] ≤ 10^9`
- `1 ≤ serverType[i] ≤ n`

## Solutions

<!-- Scaffold placeholder: the worked derivation and solutions land
     on the solutions branch later. See ../_TEMPLATE.md for the
     expected layout, naming, and ordering conventions. -->
