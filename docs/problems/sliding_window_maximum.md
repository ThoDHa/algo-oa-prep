# [Sliding Window Maximum](https://leetcode.com/problems/sliding-window-maximum/)

**Hard** | **NN minutes** | **Array, Queue, Sliding Window, Heap (Priority Queue), Monotonic Queue**

You are given an array of integers `nums` and an integer `k`. There is a sliding window of size `k` that starts at the left edge of the array. The window slides one position to the right until it reaches the right edge of the array.

Return a list that contains the maximum element in the window at each step.

## Examples

### Example 1

**Input:** `nums = [1,2,1,0,4,2,6], k = 3`

**Output:** `[2,2,4,4,6]`

**Explanation:** Window position            Max
---------------           -----
[1  2  1] 0  4  2  6        2
 1 [2  1  0] 4  2  6        2
 1  2 [1  0  4] 2  6        4
 1  2  1 [0  4  2] 6        4
 1  2  1  0 [4  2  6]       6

## Constraints

- `1 <= nums.length <= 100,000`
- `-10,000 <= nums[i] <= 10,000`
- `1 <= k <= nums.length`

## Solutions

<!-- Scaffold placeholder: the worked derivation and solutions land
     on the solutions branch later. See _TEMPLATE.md for the
     expected layout, naming, and ordering conventions. -->
