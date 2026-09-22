# [Non Overlapping Intervals](https://leetcode.com/problems/non-overlapping-intervals/)

**Medium** | **NN minutes** | **Array, Dynamic Programming, Greedy, Sorting**

Given an array of intervals `intervals` where `intervals[i] = [start_i, end_i]`, return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

Note: Intervals are *non-overlapping* even if they have a common point. For example, `[1, 3]` and `[2, 4]` are overlapping, but `[1, 2]` and `[2, 3]` are non-overlapping.

## Examples

### Example 1

**Input:** `intervals = [[1,2],[2,4],[1,4]]`

**Output:** `1`

**Explanation:** After [1,4] is removed, the rest of the intervals are non-overlapping.

### Example 2

**Input:** `intervals = [[1,2],[2,4]]`

**Output:** `0`

## Constraints

- `1 <= intervals.length <= 100,000`
- `intervals[i].length == 2`
- `-50000 <= starti < endi <= 50000`

## Solutions

<!-- Scaffold placeholder: the worked derivation and solutions land
     on the solutions branch later. See _TEMPLATE.md for the
     expected layout, naming, and ordering conventions. -->
