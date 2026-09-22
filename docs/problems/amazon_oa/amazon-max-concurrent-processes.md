# [Maximum Concurrent Processes (Bar Raiser Round)](https://www.fastprep.io/problems/amazon-max-concurrent-processes)

**Medium** | **NN minutes** | **Intervals, Sorting**

$23

## Examples

### Example 1

**Input:** `intervals = [[1, 3], [2, 5], [3, 6]]`

**Output:** `3`

**Explanation:** At time 3, all three processes are running. Since intervals are inclusive, both [1, 3] and [3, 6] include time 3.

### Example 2

**Input:** `intervals = [[1, 2], [3, 4], [5, 6]]`

**Output:** `1`

**Explanation:** No two processes overlap, so the maximum number of concurrent processes is 1.

### Example 3

**Input:** `intervals = [[1, 10], [2, 3], [4, 5], [6, 7]]`

**Output:** `2`

**Explanation:** The long-running process overlaps with each shorter process, but the shorter processes do not overlap with one another.

### Example 4

**Input:** `intervals = [[1, 4], [2, 6], [4, 8], [6, 9]]`

**Output:** `3`

**Explanation:** At time 4, [1, 4], [2, 6], and [4, 8] are all running because interval endpoints are inclusive.

## Constraints

- `1 <= intervals.length <= 1000000 <= start <= end <= 1000000000All start and end values are integers.Intervals are inclusive: [start, end].`

## Solutions

<!-- Scaffold placeholder: the worked derivation and solutions land
     on the solutions branch later. See ../_TEMPLATE.md for the
     expected layout, naming, and ordering conventions. -->
