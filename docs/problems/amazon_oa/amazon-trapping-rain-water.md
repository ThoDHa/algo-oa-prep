# [Trapping Rain Water](https://www.fastprep.io/problems/amazon-trapping-rain-water)

**Hard** | **NN minutes** | **Array, Two Pointers, Stack**

You are given an integer array height of length n. n vertical bars stand on the x-axis. The i-th bar has width 1 and height height[i].Compute how many units of water the bars can trap after rain.Water sits above a bar only when both a strictly taller left boundary and a strictly taller right boundary exist. The water depth at index i is max(0, min(leftMax[i], rightMax[i]) - height[i]), where leftMax[i] is the tallest bar at an index < i and rightMax[i] is the tallest bar at an index > i.

## Examples

### Example 1

**Input:** `height = [0,1,0,2,1,0,1,3,2,1,2,1]`

**Output:** `6`

**Explanation:** The bars trap 1 + 1 + 2 + 1 + 1 = 6 units of water.

### Example 2

**Input:** `height = [4,2,0,3,2,5]`

**Output:** `9`

**Explanation:** The valley between the height-4 and height-5 bars traps 2 + 4 + 1 + 2 = 9 units.

## Constraints

- `1 <= height.length <= 2 * 10^4.0 <= height[i] <= 10^5.`

## Solutions

<!-- Scaffold placeholder: the worked derivation and solutions land
     on the solutions branch later. See ../_TEMPLATE.md for the
     expected layout, naming, and ordering conventions. -->
