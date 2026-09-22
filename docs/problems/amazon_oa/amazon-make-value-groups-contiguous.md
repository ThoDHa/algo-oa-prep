# [Make Value Groups Contiguous](https://www.fastprep.io/problems/amazon-make-value-groups-contiguous)

**Medium** | **NN minutes** | **Array, Hash Table, Greedy**

You are given an integer array arr. In one operation, choose two values x and y (where y may be any value, including an existing value in the array), and replace every occurrence of x in the array with y.An array is called contiguous by value if, for every distinct value present, all occurrences of that value appear in one uninterrupted block with no other values in between.Return the minimum number of operations needed to make the array contiguous by value.Function Description Complete the function minOperationsToMakeValuesContiguous in the editor below.minOperationsToMakeValuesContiguous has the following parameter:int[] arr: the input arrayReturns int: the minimum number of replacement operations

## Examples

### Example 1

**Input:** `arr = [1, 2, 1]`

**Output:** `1`

**Explanation:** Replace every 2 with 1 to get [1, 1, 1]. Now the only distinct value, 1, appears in one contiguous block. This requires 1 operation.

### Example 2

**Input:** `arr = [1, 2, 3]`

**Output:** `0`

**Explanation:** Every value already occupies a single contiguous block: 1 appears once, 2 appears once, 3 appears once. No operations are needed.

## Constraints

- `1 <= arr.length <= 1051 <= arr[i] <= 105Each operation replaces all occurrences of one chosen value x globally with any chosen value y.After all operations are complete, each distinct value remaining in the array must appear in a single contiguous block.The minimum number of operations equals the total number of distinct values minus the maximum number of distinct values that can simultaneously remain unmerged (i.e., each already occupies a single contiguous block in the original array independently of the others).`

## Solutions

<!-- Scaffold placeholder: the worked derivation and solutions land
     on the solutions branch later. See ../_TEMPLATE.md for the
     expected layout, naming, and ordering conventions. -->
