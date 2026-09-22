# [Meeting Rooms](https://leetcode.com/problems/meeting-rooms/)

**Easy** | **NN minutes** | **Array, Sorting**

> This problem is locked behind [LeetCode Premium](https://leetcode.com/problems/meeting-rooms/); read it free on [NeetCode](https://neetcode.io/problems/meeting-schedule).

Given an array of meeting time interval objects consisting of start and end times `[[start_1,end_1],[start_2,end_2],...] (start_i < end_i)`, determine if a person could add all meetings to their schedule without any conflicts. The intervals may be provided in any order.

**Note:** (0,8),(8,10) is not considered a conflict at 8

## Examples

### Example 1

**Input:** `intervals = [(0,30),(5,10),(15,20)]`

**Output:** `false`

**Explanation:** * `(0,30)` and `(5,10)` will conflict
* `(0,30)` and `(15,20)` will conflict

### Example 2

**Input:** `intervals = [(5,8),(9,15)]`

**Output:** `true`

## Constraints

- `0 <= intervals.length <= 500`
- `0 <= intervals[i].start < intervals[i].end <= 1,000,000`

## Solutions

<!-- Scaffold placeholder: the worked derivation and solutions land
     on the solutions branch later. See _TEMPLATE.md for the
     expected layout, naming, and ordering conventions. -->
