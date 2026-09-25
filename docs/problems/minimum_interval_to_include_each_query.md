# [Minimum Interval to Include Each Query](https://leetcode.com/problems/minimum-interval-to-include-each-query/)

**Medium** | **25 minutes** | **Array, Binary Search, Sweep Line, Sorting, Heap (Priority Queue)**

You are given a 2D integer array `intervals`, where `intervals[i] = [left_i, right_i]` represents the `ith` interval starting at `left_i` and ending at `right_i` **(inclusive)**.

You are also given an integer array of query points `queries`. The result of `query[j]` is the **length of the shortest interval** `i` such that `left_i <= queries[j] <= right_i`. If no such interval exists, the result of this query is `-1`.

Return an array `output` where `output[j]` is the result of `query[j]`.

Note: The length of an interval is calculated as `right_i - left_i + 1`.

## Examples

### Example 1

**Input:** `intervals = [[1,3],[2,3],[3,7],[6,6]], queries = [2,3,1,7,6,8]`

**Output:** `[2,2,3,5,1,-1]`

**Explanation:** - Query = 2: The interval `[2,3]` is the smallest one containing 2, it's length is 2.
- Query = 3: The interval `[2,3]` is the smallest one containing 3, it's length is 2.
- Query = 1: The interval `[1,3]` is the smallest one containing 1, it's length is 3.
- Query = 7: The interval `[3,7]` is the smallest one containing 7, it's length is 5.
- Query = 6: The interval `[6,6]` is the smallest one containing 6, it's length is 1.
- Query = 8: There is no interval containing 8.

## Constraints

- `1 <= intervals.length <= 100000`
- `1 <= queries.length <= 100000`
- `1 <= left_i <= right_i <= 10000000`
- `1 <= queries[j] <= 10000000`

## Solutions

<!-- Scaffold placeholder: the worked derivation and solutions land
     on the solutions branch later. See _TEMPLATE.md for the
     expected layout, naming, and ordering conventions. -->
