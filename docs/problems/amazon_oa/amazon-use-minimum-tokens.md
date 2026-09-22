# [Use Minimum Tokens](https://www.fastprep.io/problems/amazon-use-minimum-tokens)

**Hard** | **NN minutes** | **Sorting, Prefix Sum, Binary Search**

$23

## Examples

### Example 1

**Input:** `warehouse = [2, 4, 1, 3]`
**Input:** `catalog = [[5, 7]]`

**Output:** `[2]`

**Explanation:** $24

### Example 2

**Input:** `warehouse = [5, 1, 1, 4]`
**Input:** `catalog = [[5, 7], [4, 10], [7, 9]]`

**Output:** `[1, 3, 5]`

**Explanation:** For the first shipment, the optimal selection is warehouse number four. You’ll need to spend one token to extend the capacity of the fourth warehouse to accommodate the shipment and no tokens on the other warehouses. The total tokens spent equal one for capacity augmentation + zero for backup storage = 1.

For the second shipment, the optimal selection is either the second or third warehouse. You’ll spend three tokens to extend the capacity of the selected warehouse and no tokens on the remaining warehouses. Hence, the total tokens spent equal three for augmentation + zero for backup storage = 3.

This explanation is incomplete. Will enhance it later.

## Constraints

- `2 ≤ n ≤ 10^5`
- `1 ≤ warehouse[i] ≤ 10^9`
- `1 ≤ q ≤ 10^5`
- `1 ≤ catalog[i][0] ≤ 10^9`
- `1 ≤ catalog[i][1] ≤ 10^15`

## Solutions

<!-- Scaffold placeholder: the worked derivation and solutions land
     on the solutions branch later. See ../_TEMPLATE.md for the
     expected layout, naming, and ordering conventions. -->
