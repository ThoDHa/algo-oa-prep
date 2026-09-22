# [Meeting Rooms II](https://leetcode.com/problems/meeting-rooms-ii/)

**Medium** | **NN minutes** | **Array, Two Pointers, Greedy, Sorting, Heap (Priority Queue), Prefix Sum**

> This problem is locked behind [LeetCode Premium](https://leetcode.com/problems/meeting-rooms-ii/); read it free on [NeetCode](https://neetcode.io/problems/meeting-schedule-ii).

Given an array of meeting time interval objects consisting of start and end times `[[start_1,end_1],[start_2,end_2],...] (start_i < end_i)`, find the minimum number of rooms required to schedule all meetings without any conflicts.

**Note:** `(0,8),(8,10)` is **NOT** considered a conflict at 8.

## Examples

### Example 1

**Input:** `intervals = [(0,40),(5,10),(15,20)]`

**Output:** `2`

**Explanation:** room1: `(0,40)`
room2: `(5,10),(15,20)`

### Example 2

**Input:** `intervals = [(4,9)]`

**Output:** `1`

## Constraints

- `0 <= intervals.length <= 100,000`
- `0 <= intervals[i].start < intervals[i].end <= 1,000,000`

## Solutions

<!-- Scaffold placeholder: the worked derivation and solutions land
     on the solutions branch later. See ../_TEMPLATE.md for the
     expected layout, naming, and ordering conventions. -->
