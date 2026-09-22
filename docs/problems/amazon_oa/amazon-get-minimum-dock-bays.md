# [Min Dock Bays](https://www.fastprep.io/problems/amazon-get-minimum-dock-bays)

**Medium** | **NN minutes** | **Array, Binary Search, Heap**

$23

## Examples

### Example 1

**Input:** `truckCargoSize = [3, 4, 3, 2, 3]`
**Input:** `maxTurnaroundTime = 8`

**Output:** `3`

**Explanation:** Attempting with two dock bays (d = 2): the trucks are distributed in arrival order between the two bays. Dock bay 1 unloads trucks 1, 3, and 5 (3 + 3 + 3 = 9 minutes) and dock bay 2 unloads trucks 2 and 4 (4 + 2 = 6 minutes). All trucks are unloaded in 9 minutes, which exceeds the maxTurnaroundTime of 8 minutes. Attempting with three dock bays (d = 3): the bays finish in 5, 7, and 3 minutes respectively, so all trucks are unloaded in 7 minutes, which is within the maxTurnaroundTime of 8 minutes. Therefore, the minimum number of dock bays required is 3.

### Example 2

**Input:** `truckCargoSize = [2, 3, 1]`
**Input:** `maxTurnaroundTime = 7`

**Output:** `1`

**Explanation:** With only one dock bay, all trucks can be unloaded in 2 + 3 + 1 = 6 minutes, which is within the maxTurnaroundTime of 7 minutes. Therefore, the minimum number of dock bays required is 1.

## Constraints

- `1 ≤ n ≤ 5 * 10^41 ≤ maxTurnaroundTime ≤ 10^151 ≤ truckCargoSize[i] ≤ min(maxTurnaroundTime, 10^9)`

## Solutions

<!-- Scaffold placeholder: the worked derivation and solutions land
     on the solutions branch later. See ../_TEMPLATE.md for the
     expected layout, naming, and ordering conventions. -->
