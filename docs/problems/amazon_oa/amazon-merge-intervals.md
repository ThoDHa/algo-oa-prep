# [Merge Intervals](https://www.fastprep.io/problems/amazon-merge-intervals)

**Easy** | **NN minutes** | **Intervals, Sorting**

Given an array of closed intervals where intervals[i] = [start_i, end_i], merge every pair of overlapping intervals.Return the non-overlapping intervals that cover every interval in the input, sorted by start time. Intervals that share an endpoint are considered overlapping.

## Examples

### Example 1

**Input:** `intervals = [[1,3],[2,6],[8,10],[15,18]]`

**Output:** `[[1,6],[8,10],[15,18]]`

**Explanation:** Intervals [1,3] and [2,6] overlap, so they merge into [1,6].

### Example 2

**Input:** `intervals = [[1,4],[4,5]]`

**Output:** `[[1,5]]`

**Explanation:** The intervals share endpoint 4, so they merge into [1,5].

### Example 3

**Input:** `intervals = [[8,10],[1,4],[2,3],[15,18],[6,9],[3,7],[17,20],[12,12]]`

**Output:** `[[1,10],[12,12],[15,20]]`

**Explanation:** The intervals are intentionally unsorted. After sorting by start time, [1,4], [2,3], [3,7], [6,9], and [8,10] form one connected overlap chain and merge into [1,10]. Interval [12,12] remains separate, while [15,18] and [17,20] merge into [15,20].

## Constraints

- `1 <= intervals.length <= 10^4intervals[i].length == 20 <= start_i <= end_i <= 10^4`

## Solutions

<!-- Scaffold placeholder: the worked derivation and solutions land
     on the solutions branch later. See ../_TEMPLATE.md for the
     expected layout, naming, and ordering conventions. -->
