# [K Closest Elements in a Sorted Array](https://www.fastprep.io/problems/amazon-k-closest-elements-in-sorted-array)

**Medium** | **NN minutes** | **Array, Binary Search, Two Pointers**

Given an integer array arr sorted in nondecreasing order, an integer k, and a target x, return the k values closest to x in ascending order.A value a is closer than a value b when |a - x| < |b - x|. When the distances are equal, the smaller value is considered closer.

## Examples

### Example 1

**Input:** `arr = [-10,-4,-1,3,8,12]`
**Input:** `k = 4`
**Input:** `x = 2`

**Output:** `[-4,-1,3,8]`

**Explanation:** Values -4 and 8 are equally distant from 2; the smaller value wins the boundary tie.

### Example 2

**Input:** `arr = [2,4,6,8]`
**Input:** `k = 1`
**Input:** `x = 5`

**Output:** `[4]`

**Explanation:** Values 4 and 6 are both one unit away, so the smaller value 4 is selected.

### Example 3

**Input:** `arr = [5,6,7]`
**Input:** `k = 2`
**Input:** `x = 100`

**Output:** `[6,7]`

**Explanation:** The target lies to the right of every array value, so the last two values are closest.

## Constraints

- `1 <= arr.length <= 100000.1 <= k <= arr.length.arr is sorted in nondecreasing order.-1000000000 <= arr[i], x <= 1000000000.`

## Solutions

<!-- Scaffold placeholder: the worked derivation and solutions land
     on the solutions branch later. See ../_TEMPLATE.md for the
     expected layout, naming, and ordering conventions. -->
