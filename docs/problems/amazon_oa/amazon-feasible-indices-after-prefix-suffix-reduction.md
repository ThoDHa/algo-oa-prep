# [Feasible Indices After Prefix/Suffix Reduction](https://www.fastprep.io/problems/amazon-feasible-indices-after-prefix-suffix-reduction)

**Medium** | **NN minutes** | **Array, Greedy**

Note: This problem is a duplicate of Feasible Indices After Reduction. The sighting dates have been merged into that version.

You are given an integer array arr of size n, where all elements are distinct.

You can perform the following operations any number of times:

Choose a non-empty prefix of the array and delete all elements except the minimum element of that prefix.Choose a non-empty suffix of the array and delete all elements except the maximum element of that suffix.After each operation, the remaining elements are concatenated to form a new array.

An index i is called feasible if it is possible to reduce the array to a single element [arr[i]] using the above operations.

Return a binary string of length n where:

1 means the index is feasible.0 means the index is not feasible.

## Examples

### Example 1

**Input:** `arr = [1, 3, 2, 5, 4]`

**Output:** `"10011"`

## Constraints

- `1 <= n <= 2 * 10^5`
- `1 <= arr[i] <= 10^6`
- `All elements are distinct.`

## Solutions

<!-- Scaffold placeholder: the worked derivation and solutions land
     on the solutions branch later. See ../_TEMPLATE.md for the
     expected layout, naming, and ordering conventions. -->
