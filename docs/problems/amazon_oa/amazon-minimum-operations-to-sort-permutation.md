# [Minimum Operations to Sort a Permutation](https://www.fastprep.io/problems/amazon-minimum-operations-to-sort-permutation)

**unknown difficulty** | **NN minutes** | **unknown categories**

You are given a permutation arr of size n, containing each integer from 1 to n exactly once.

In one operation, you may do either of the following:

Move the first element of the array to the end, shifting every other element one position to the left.Reverse the entire array.It is guaranteed that the array can be sorted into increasing order using these operations. Return the minimum number of operations needed to sort arr.

## Examples

### Example 1

**Input:** `arr = [3,1,2]`

**Output:** `1`

**Explanation:** Move the first element 3 to the end to get [1,2,3].

### Example 2

**Input:** `arr = [1,5,4,3,2]`

**Output:** `2`

**Explanation:** Move 1 to the end to get [5,4,3,2,1], then reverse the array to get [1,2,3,4,5].

### Example 3

**Input:** `arr = [1,2,3,4]`

**Output:** `0`

**Explanation:** The array is already sorted.

## Constraints

- `1 <= arr.length <= 10^5`
- `1 <= arr[i] <= arr.length`
- `arr is a permutation of integers from 1 to arr.length.`
- `It is guaranteed that arr can be sorted using the given operations.`

## Solutions

<!-- Scaffold placeholder: the worked derivation and solutions land
     on the solutions branch later. See ../_TEMPLATE.md for the
     expected layout, naming, and ordering conventions. -->
