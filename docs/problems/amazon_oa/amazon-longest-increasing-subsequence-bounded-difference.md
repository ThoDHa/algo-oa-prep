# [Longest Increasing Subsequence With Bounded Adjacent Difference](https://www.fastprep.io/problems/amazon-longest-increasing-subsequence-bounded-difference)

**Hard** | **NN minutes** | **Array, Dynamic Programming, Segment Tree**

Given a non-empty integer array arr and a non-negative integer k, return the maximum length of a subsequence that satisfies all of the following:

The selected values are strictly increasing.The difference between every pair of consecutive selected values is at most k.The selected values preserve their relative order in arr.A subsequence may delete any number of elements without changing the order of the remaining elements.

## Examples

### Example 1

**Input:** `arr = [7,1,4,5,8,8,10,6,7,7,7,8]`, `k = 4`

**Output:** `6`

**Explanation:** One longest valid subsequence is [1,4,5,6,7,8]. It preserves input order, every adjacent difference is at most 4, and its length is 6.

### Example 2

**Input:** `arr = [3,1,2,6,10,11,4,5]`, `k = 3`

**Output:** `4`

**Explanation:** The subsequence [1,2,4,5] is strictly increasing, preserves input order, and has adjacent differences 1, 2, and 1.

### Example 3

**Input:** `arr = [5,4,3,2,1]`, `k = 2`

**Output:** `1`

**Explanation:** No two values form a strictly increasing pair in subsequence order, so every valid longest subsequence contains one value.

## Constraints

- `1 <= arr.length <= 2 * 10^5`
- `-10^9 <= arr[i] <= 10^9`
- `0 <= k <= 2 * 10^9`

## Solutions

<!-- Scaffold placeholder: the worked derivation and solutions land
     on the solutions branch later. See ../_TEMPLATE.md for the
     expected layout, naming, and ordering conventions. -->
