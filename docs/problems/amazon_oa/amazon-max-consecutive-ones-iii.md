# [Max Consecutive Ones III](https://www.fastprep.io/problems/amazon-max-consecutive-ones-iii)

**Medium** | **NN minutes** | **Array, Sliding Window, Two Pointers**

Given a binary array nums and an integer k, return the maximum number of consecutive ones obtainable by flipping at most k zeros to ones.

## Examples

### Example 1

**Input:** `nums = [1,1,1,0,0,0,1,1,1,1,0]`
**Input:** `k = 2`

**Output:** `6`

**Explanation:** Flipping two zeros creates a six-element run.

### Example 2

**Input:** `nums = [0,0,1,1,1,0,0]`
**Input:** `k = 0`

**Output:** `3`

**Explanation:** Without flips, the central run has length three.

### Example 3

**Input:** `nums = [0,0,0]`
**Input:** `k = 3`

**Output:** `3`

**Explanation:** All three zeros can be flipped.

## Constraints

- `0 &le; nums.length &le; 100000.Every value in nums is 0 or 1.0 &le; k &le; nums.length.`

## Solutions

<!-- Scaffold placeholder: the worked derivation and solutions land
     on the solutions branch later. See ../_TEMPLATE.md for the
     expected layout, naming, and ordering conventions. -->
