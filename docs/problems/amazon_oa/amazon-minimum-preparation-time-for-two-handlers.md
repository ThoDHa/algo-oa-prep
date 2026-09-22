# [Minimum Preparation Time for Two Handlers](https://www.fastprep.io/problems/amazon-minimum-preparation-time-for-two-handlers)

**Medium** | **NN minutes** | **Dynamic Programming, Array**

$23

## Examples

### Example 1

**Input:** `workList = [1, 2, 2]`
**Input:** `longPrepTime = [4, 5]`
**Input:** `shortPrepTime = [2, 3]`

**Output:** `12`

**Explanation:** Assign work type 1 to the first handler, then assign both type-2 jobs to the second handler. The total cost is 4 + 5 + 3 = 12.

### Example 2

**Input:** `workList = [1, 1, 1]`
**Input:** `longPrepTime = [4]`
**Input:** `shortPrepTime = [2]`

**Output:** `8`

**Explanation:** Use the same handler for all three jobs to pay one long preparation and two short preparations.

## Constraints

- `workList[i] identifies a work type between 1 and mlongPrepTime and shortPrepTime contain one entry per work type.Jobs must be processed in order.`

## Solutions

<!-- Scaffold placeholder: the worked derivation and solutions land
     on the solutions branch later. See ../_TEMPLATE.md for the
     expected layout, naming, and ordering conventions. -->
