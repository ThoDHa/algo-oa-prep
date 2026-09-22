# [Search in a Rotated Sorted Array](https://www.fastprep.io/problems/amazon-search-rotated-sorted-array)

**Medium** | **NN minutes** | **Array, Binary Search**

Given an integer array nums that was sorted in strictly increasing order and then rotated at an unknown pivot, and an integer target, return the index of target.Return -1 when target does not appear in nums.All values in nums are distinct. Your solution must run in O(log n) time.

## Examples

### Example 1

**Input:** `nums = [4,5,6,7,0,1,2]`
**Input:** `target = 0`

**Output:** `4`

**Explanation:** The target 0 appears at index 4.

### Example 2

**Input:** `nums = [4,5,6,7,0,1,2]`
**Input:** `target = 3`

**Output:** `-1`

**Explanation:** The target 3 is absent, so the result is -1.

### Example 3

**Input:** `nums = [1]`
**Input:** `target = 0`

**Output:** `-1`

**Explanation:** The only array value is 1, so 0 is absent.

## Constraints

- `1 <= nums.length <= 10^5-10^9 <= nums[i] <= 10^9nums contains distinct values.nums was sorted in strictly increasing order and rotated at an unknown pivot.-10^9 <= target <= 10^9`

## Solutions

<!-- Scaffold placeholder: the worked derivation and solutions land
     on the solutions branch later. See ../_TEMPLATE.md for the
     expected layout, naming, and ordering conventions. -->
