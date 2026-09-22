# [Find Minimum Machine Sizes](https://www.fastprep.io/problems/amazon-find-minimum-machines-size)

**Medium** | **NN minutes** | **Array, Greedy**

$23

## Examples

### Example 1

**Input:** `machineCapacity = [1, 2, 2, 1, 1]`

**Output:** `3`

**Explanation:** Efficiency initially for [1, 2, 2, 1, 1]: |1-2| + |2-2| + |2-1| + |1-1| = 1 + 0 + 1 + 0 = 2. After removing the machines at positions [2] and [3] (0-indexed), the remaining subsequence is [1, 2, 1] (relative order preserved), whose efficiency is |1-2| + |2-1| = 1 + 1 = 2, which equals the original efficiency. No smaller efficiency-preserving subsequence exists, so the minimum number of machines is 3.

## Constraints

- `1 ≤ n ≤ 2×10^50 ≤ machineCapacity[i] ≤ 10^9`

## Solutions

<!-- Scaffold placeholder: the worked derivation and solutions land
     on the solutions branch later. See ../_TEMPLATE.md for the
     expected layout, naming, and ordering conventions. -->
