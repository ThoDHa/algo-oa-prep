# [Maximum Concurrent Processes (Bar Raiser Round)](https://www.fastprep.io/problems/amazon-max-concurrent-processes)

**Medium** | **NN minutes** | **Intervals, Sorting**

🍇 FastPrep match note: This version is based on a reported Amazon SDE2 full-time onsite Bar Raiser round prompt and should match the core task about 90-95%: given process running intervals, return the maximum number running at the same time.

The main uncertainty is whether the original wording explicitly counted endpoints as running; the reported example only reaches 3 if time 3 belongs to both [1, 3] and [3, 6], so we make the inclusive endpoint rule explicit and add a few practice examples and constraints for clarity.

You are given a list of processes. Each process has a running interval represented as [start, end].

A process is considered running at every integer time from start through end, inclusive.

Return the maximum number of processes running at the same time.

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

- `1 <= intervals.length <= 100000`
- `0 <= start <= end <= 1000000000`
- `All start and end values are integers.`
- `Intervals are inclusive: [start, end].`

## Solutions

<!-- Scaffold placeholder: the worked derivation and solutions land
     on the solutions branch later. See ../_TEMPLATE.md for the
     expected layout, naming, and ordering conventions. -->
