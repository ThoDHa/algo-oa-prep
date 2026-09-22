# [Optimal Utilization](https://www.fastprep.io/problems/amazon-optimal-utilization)

**Medium** | **NN minutes** | **Two Pointers, Sorting**

$23

## Examples

### Example 1

**Input:** `deviceCapacity = 7`
**Input:** `foregroundAppList = [[1, 2], [2, 4], [3, 6]]`
**Input:** `backgroundAppList = [[1, 2]]`

**Output:** `[[2, 1]]`

**Explanation:** The possible pairs are:

[1, 1] uses 2 + 2 = 4 memory.
[2, 1] uses 4 + 2 = 6 memory.
[3, 1] uses 6 + 2 = 8 memory (exceeds the device capacity).

Since 6 is the largest usage within capacity, [2, 1] is the only optimal pair.

### Example 2

**Input:** `deviceCapacity = 10`
**Input:** `foregroundAppList = [[1, 3], [2, 5], [3, 7], [4, 10]]`
**Input:** `backgroundAppList = [[1, 2], [2, 3], [3, 4], [4, 5]]`

**Output:** `[[2, 4], [3, 2]]`

**Explanation:** There are two optimal pairs:

Pair [2, 4]: Foreground app 2 uses 5 memory, background app 4 uses 5 memory; combined = 10.

Pair [3, 2]: Foreground app 3 uses 7 memory, background app 2 uses 3 memory; combined = 10.

### Example 3

**Input:** `deviceCapacity = 16`
**Input:** `foregroundAppList = [[2, 7], [3, 14]]`
**Input:** `backgroundAppList = [[2, 10], [3, 14]]`

**Output:** `[[]]`

**Explanation:** No combination of one foreground and one background application fits within the device capacity. Hence, the output is a list with an empty pair.

## Constraints

- `TO-DO`

## Solutions

<!-- Scaffold placeholder: the worked derivation and solutions land
     on the solutions branch later. See ../_TEMPLATE.md for the
     expected layout, naming, and ordering conventions. -->
