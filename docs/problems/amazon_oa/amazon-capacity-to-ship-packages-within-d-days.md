# [Capacity To Ship Packages Within D Days](https://www.fastprep.io/problems/amazon-capacity-to-ship-packages-within-d-days)

**Medium** | **NN minutes** | **Array, Binary Search**

A conveyor belt has packages that must be shipped from one port to another within days days.The i-th package has weight weights[i]. Packages are loaded in the given order: you may not rearrange them. Each day, you load the conveyor with packages whose total weight does not exceed the ship's capacity, then ship that day's load.Return the least ship capacity that can move every package within days days.

## Examples

### Example 1

**Input:** `weights = [1,2,3,4,5,6,7,8,9,10]`
**Input:** `days = 5`

**Output:** `15`

**Explanation:** Capacity 15 ships as [1,2,3,4,5], [6,7], [8], [9], and [10]. Capacity 14 needs more than 5 days.

### Example 2

**Input:** `weights = [3,2,2,4,1,4]`
**Input:** `days = 3`

**Output:** `6`

**Explanation:** Capacity 6 ships as [3,2], [2,4], and [1,4].

## Constraints

- `1 <= weights.length <= 5 * 10^4.1 <= weights[i] <= 500.1 <= days <= weights.length.`

## Solutions

<!-- Scaffold placeholder: the worked derivation and solutions land
     on the solutions branch later. See ../_TEMPLATE.md for the
     expected layout, naming, and ordering conventions. -->
