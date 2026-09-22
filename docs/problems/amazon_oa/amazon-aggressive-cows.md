# [Aggressive Cows](https://www.fastprep.io/problems/amazon-aggressive-cows)

**Medium** | **NN minutes** | **Array, Sorting, Binary Search, Greedy**

Given distinct integer stall positions stalls and an integer cows, place exactly cows cows in different stalls.Return the largest possible value of the minimum distance between every pair of placed cows.

## Examples

### Example 1

**Input:** `stalls = [1,2,4,8,9]`
**Input:** `cows = 3`

**Output:** `3`

**Explanation:** Placing cows at 1, 4, and 8 gives a minimum distance of 3, which cannot be improved.

### Example 2

**Input:** `stalls = [10,1,2,7,5]`
**Input:** `cows = 3`

**Output:** `4`

**Explanation:** After sorting, positions 1, 5, and 10 achieve minimum distance 4.

### Example 3

**Input:** `stalls = [0,5]`
**Input:** `cows = 2`

**Output:** `5`

**Explanation:** Both stalls must be used, so their distance is the answer.

## Constraints

- `2 <= stalls.length <= 10^5.2 <= cows <= stalls.length.0 <= stalls[i] <= 10^9.All stall positions are distinct.`

## Solutions

<!-- Scaffold placeholder: the worked derivation and solutions land
     on the solutions branch later. See ../_TEMPLATE.md for the
     expected layout, naming, and ordering conventions. -->
