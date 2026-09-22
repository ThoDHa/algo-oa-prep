# [Longest Arithmetic Subarray After One Change](https://www.fastprep.io/problems/amazon-longest-arithmetic-subarray-after-one-change)

**unknown difficulty** | **NN minutes** | **unknown categories**

You are given an integer array deviation.

You may change at most one element of the array to any integer value. After making at most one change, find the maximum possible length of a contiguous subarray that forms an arithmetic progression.

The changed element stays at its original index and may be used to connect the unchanged elements before it and after it into one longer arithmetic subarray.

A contiguous subarray forms an arithmetic progression if the difference between every pair of consecutive elements in that subarray is the same.

## Examples

### Example 1

**Input:** `deviation = [8, 5, 2, 1, 100]`

**Output:** `4`

**Explanation:** Change 1 to -1. The contiguous subarray [8,5,2,-1] has common difference -3, so its length is 4.

### Example 2

**Input:** `deviation = [1, 2, 3, 4, 100, 6, 7, 8, 9, 10]`

**Output:** `10`

**Explanation:** Change 100 to 5. The entire array becomes an arithmetic progression with common difference 1.

## Constraints

- `Constraints:`
- `1 <= deviation.length <= 105`
- `-109 <= deviation[i] <= 109`
- `You may change at most one element, and the changed value may be any integer.`

## Solutions

<!-- Scaffold placeholder: the worked derivation and solutions land
     on the solutions branch later. See ../_TEMPLATE.md for the
     expected layout, naming, and ordering conventions. -->
