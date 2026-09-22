# [Get The Most Out Of The Data](https://www.fastprep.io/problems/amazon-get-most-out-of-the-data)

**Medium** | **NN minutes** | **Array, Greedy, Sorting**

$23

## Examples

### Example 1

**Input:** `data = [2, 1, 2]`

**Output:** `[2, 1, 3]`

**Explanation:** Permutation   | Information Gain
       [1, 2, 3] | 1 * 2 + 2 * 1 + 3 * 2 = 10
       [2, 1, 3] | 1 * 1 + 2 * 2 + 3 * 2 = 11
       [1, 3, 2] | 1 * 2 + 2 * 2 + 3 * 1 = 9
       [3, 1, 2] | 1 * 2 + 2 * 2 + 3 * 1 = 9
       [2, 3, 1] | 1 * 1 + 2 * 2 + 3 * 2 = 11
       [3, 2, 1] | 1 * 2 + 2 * 1 + 3 * 2 = 10
      
      The maximum information is gained for permutations [2, 1, 3] and [2, 3, 1], but [2, 1, 3] is the lexicographically smallest permutation.
      

      More than happy to modify the explanation if found to be incorrect or misleading. Thanks for the feedback :)

## Constraints

- `:)`

## Solutions

<!-- Scaffold placeholder: the worked derivation and solutions land
     on the solutions branch later. See ../_TEMPLATE.md for the
     expected layout, naming, and ordering conventions. -->
