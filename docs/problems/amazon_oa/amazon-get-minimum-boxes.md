# [Get Minimum Boxes](https://www.fastprep.io/problems/amazon-get-minimum-boxes)

**Medium** | **NN minutes** | **Array, Sorting, Sliding Window**

$23

## Examples

### Example 1

**Input:** `boxes = [1, 4, 3, 2]`
**Input:** `capacity = 2`

**Output:** `1`

**Explanation:** Here boxes = [1, 4, 3, 2] and capacity = 2.With all boxes loaded, max = 4 and min = 1, so max ≤ capacity * min becomes 4 ≤ 2 * 1 = 2, which is false.Unload the box of size 1. The remaining boxes are [4, 3, 2] with max = 4 and min = 2, so 4 ≤ 2 * 2 = 4, which is true.Only one box must be unloaded, so the answer is 1.

## Constraints

- `1 ≤ n ≤ 10^51 ≤ boxes[i] ≤ 5 * 10^51 ≤ capacity`

## Solutions

<!-- Scaffold placeholder: the worked derivation and solutions land
     on the solutions branch later. See ../_TEMPLATE.md for the
     expected layout, naming, and ordering conventions. -->
