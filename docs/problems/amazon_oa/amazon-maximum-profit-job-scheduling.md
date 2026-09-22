# [Maximum Profit in Job Scheduling](https://www.fastprep.io/problems/amazon-maximum-profit-job-scheduling)

**Hard** | **NN minutes** | **Array, Sorting, Binary Search, Dynamic Programming, Intervals**

You are given equal-length arrays startTime, endTime, and profit. Job i runs on the half-open interval from its start time to its end time and earns its profit.

Select non-overlapping jobs to maximize total profit. A job that starts exactly when another ends does not overlap.

## Examples

### Example 1

**Input:** `startTime = [1,2,3,3]`, `endTime = [3,4,5,6]`, `profit = [50,10,40,70]`

**Output:** `120`

**Explanation:** Choose jobs [1,3) and [3,6) for profit 120.

### Example 2

**Input:** `startTime = [1,2,3,4,6]`, `endTime = [3,5,10,6,9]`, `profit = [20,20,100,70,60]`

**Output:** `150`

**Explanation:** Jobs [1,3), [4,6), and [6,9) earn 150.

### Example 3

**Input:** `startTime = [1,1,1]`, `endTime = [2,3,4]`, `profit = [5,6,4]`

**Output:** `6`

**Explanation:** All jobs overlap, so choose the highest-profit one.

## Constraints

- `1 ≤ startTime.length = endTime.length = profit.length ≤ 50000.`
- `0 ≤ startTime[i] < endTime[i] ≤ 10^9.`
- `1 ≤ profit[i] ≤ 10000.`

## Solutions

<!-- Scaffold placeholder: the worked derivation and solutions land
     on the solutions branch later. See ../_TEMPLATE.md for the
     expected layout, naming, and ordering conventions. -->
