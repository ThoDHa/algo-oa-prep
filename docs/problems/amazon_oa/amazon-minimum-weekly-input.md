# [Planning the Campaign](https://www.fastprep.io/problems/amazon-minimum-weekly-input)

**Medium** | **NN minutes** | **Dynamic Programming, Array**

$23

## Examples

### Example 1

**Input:** `costs = [1000, 500, 2000, 8000, 1500]`
**Input:** `weeks = 3`

**Output:** `9500`

**Explanation:** The company can organize the first campaign in the first week, the second campaign in the second week, and the remaining campaigns in the third week. The sum of weekly inputs in this planning is 1000 + 500 + max(2000, 8000, 1500) = 9500, which is the minimum possible input. Return 9500.

## Constraints

- `1 ≤ n ≤ 300`
- `1 ≤ weeks ≤ n ≤ 300`
- `1 ≤ costs[i] ≤ 10^5`

## Solutions

<!-- Scaffold placeholder: the worked derivation and solutions land
     on the solutions branch later. See ../_TEMPLATE.md for the
     expected layout, naming, and ordering conventions. -->
