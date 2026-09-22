# [Jump Game II](https://leetcode.com/problems/jump-game-ii/)

**Medium** | **NN minutes** | **Array, Dynamic Programming, Greedy**

You are given an array of integers `nums`, where `nums[i]` represents the maximum length of a jump towards the right from index `i`. For example, if you are at `nums[i]`, you can jump to any index `i + j` where:

* `j <= nums[i]`
* `i + j < nums.length`

You are initially positioned at `nums[0]`.

Return the minimum number of jumps to reach the last position in the array (index `nums.length - 1`). You may assume there is always a valid answer.

## Examples

### Example 1

**Input:** `nums = [2,4,1,1,1,1]`

**Output:** `2`

**Explanation:** Jump from index `0` to index `1`, then jump from index `1` to the last index.

### Example 2

**Input:** `nums = [2,1,2,1,0]`

**Output:** `2`

## Constraints

- `1 <= nums.length <= 1000`
- `0 <= nums[i] <= 100`

## Solutions

<!-- Scaffold placeholder: the worked derivation and solutions land
     on the solutions branch later. See ../_TEMPLATE.md for the
     expected layout, naming, and ordering conventions. -->
