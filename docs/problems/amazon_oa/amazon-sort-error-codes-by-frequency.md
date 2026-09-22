# [Sort Error Codes by Frequency](https://www.fastprep.io/problems/amazon-sort-error-codes-by-frequency)

**Easy** | **NN minutes** | **Sorting, Hash Table**

You are given an integer array codes representing error codes.Sort the entire array using these priority rules:Error codes with lower frequency come first.If two error codes have the same frequency, the smaller numeric value comes first.Return the sorted array, keeping duplicate values in the result.Function Description Complete the function sortErrorCodesByFrequency in the editor below.sortErrorCodesByFrequency has the following parameter:int[] codes: the input error codesReturns int[]: the reordered array.

## Examples

### Example 1

**Input:** `codes = [4, 5, 6, 5, 4, 3]`

**Output:** `[3, 6, 4, 4, 5, 5]`

**Explanation:** 3 and 6 appear once, so they come first in numeric order. Then 4 and 5 each appear twice, so 4 comes before 5.

### Example 2

**Input:** `codes = [2, 2, 1, 1, 1, 3]`

**Output:** `[3, 2, 2, 1, 1, 1]`

**Explanation:** 3 has frequency 1, 2 has frequency 2, and 1 has frequency 3.

## Constraints

- `The output must contain the same multiset of values as the input.Order by increasing frequency, then by increasing numeric value.`

## Solutions

<!-- Scaffold placeholder: the worked derivation and solutions land
     on the solutions branch later. See ../_TEMPLATE.md for the
     expected layout, naming, and ordering conventions. -->
