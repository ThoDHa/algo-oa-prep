# [Minimum Contiguous Replacements](https://www.fastprep.io/problems/amazon-minimum-contiguous-replacements)

**Medium** | **NN minutes** | **Array, Hash Table, Union Find**

You are given an array arr of integers. In one operation, choose two distinct values x and y that currently appear in the array, then replace every occurrence of x with y.Return the minimum number of operations needed to make the array valid.An array is valid if every distinct value forms exactly one contiguous block. Values do not all need to become the same.For example, [1,1,2,2,3] is valid, while [1,2,1,3] is not valid because value 1 appears in two separated blocks.Function Description Complete minOperations.int arr[n]: the array to transformReturns int: the minimum number of replacement operations.

## Examples

### Example 1

**Input:** `arr = [1,2,1]`

**Output:** `1`

**Explanation:** Replace every occurrence of 2 with 1, producing [1,1,1].

### Example 2

**Input:** `arr = [1,2,3,1,2,3]`

**Output:** `2`

**Explanation:** One valid sequence is to replace all 2s with 1, then replace all 3s with 1.

### Example 3

**Input:** `arr = [1,2,1,2]`

**Output:** `1`

**Explanation:** Replacing every occurrence of either value with the other makes the array one contiguous block.

## Constraints

- `1 <= arr.length <= 10001 <= arr[i] <= 1000`

## Solutions

<!-- Scaffold placeholder: the worked derivation and solutions land
     on the solutions branch later. See ../_TEMPLATE.md for the
     expected layout, naming, and ordering conventions. -->
