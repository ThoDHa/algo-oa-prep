# [Permutation Sorter](https://www.fastprep.io/problems/amazon-permutation-sorter)

**Medium** | **NN minutes** | **Array, Math, Greedy**

Amazon engineers are testing a new tool, the Permutation Sorter, built to reorder sequences using limited operations.Given a permutation of integers, the objective is to sort the permutation using only two specific operations:Reverse the entire permutation.Transfer the first element of the permutation to the last position, i.e., change arr[0], arr[1], ..., arr[n-1] to arr[1], arr[2], ..., arr[n-1], arr[0].Formally, given a permutation arr of size n, determine the minimum number of operations needed to sort the given permutation in increasing order. The permutation provided is guaranteed to be sorted using only these two operations.Note: A permutation of length n is a sequence of integers from 1 to n containing each number exactly once.Complete the function findMinimumOperations in the editor below.

## Examples

### Example 1

**Input:** `arr = [2, 3, 4, 5, 6, 7, 8, 9, 10, 1]`

**Output:** `3`

**Explanation:** For n = 10, the permutation can be sorted by performing the following operations:Reverse the permutation to get arr = [1, 10, 9, 8, 7, 6, 5, 4, 3, 2].Transfer the first element to the last position to get arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1].Reverse the permutation to get arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10].It can be shown that the given permutation can only be sorted using a minimum of 3 operations.

## Constraints

<!-- Constraints not parseable from FastPrep for amazon-permutation-sorter; fill them in. -->

## Solutions

<!-- Scaffold placeholder: the worked derivation and solutions land
     on the solutions branch later. See ../_TEMPLATE.md for the
     expected layout, naming, and ordering conventions. -->
