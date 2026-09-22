# [Get Operations](https://www.fastprep.io/problems/amazon-get-operations)

**Hard** | **NN minutes** | **Array, Greedy, Sorting**

$23

## Examples

### Example 1

**Input:** `resource = [6, 4, 3, 5, 2, 1]`

**Output:** `[2, 3, 4, 6]`

**Explanation:** There MIGHT be something wrong in this explanation. I am not quite sure about it.
      If you found anything wrong, pls feel free to lmk! Many thanks in advance! 🐳 Happy Coding! 
      
      CPU can achieve the minimum number of operations in the following way (underlined elements denote the processes that have less than x resources):
      
      Choose x=2: [6,4,3,5,2,1] -> [1, 6,4,3,5,2]
      
      Choose x=3: [1, 6,4,3,5,2] -> [1, 2, 6,4,3,5]
      
      Choose x=4: [1, 2, 6,4,3,5] -> [1, 2, 3, 6,4,5]
      
      Choose x=6: [1, 2, 3, 6,4,5] -> [1, 2, 3, 4, 5, 6]
      
      Minimum number of operations = 4, and the answer is [2, 3, 4, 6].

### Example 2

**Input:** `resource = [10, 5, 14, 12, 13]`

**Output:** `[14, 15]`

**Explanation:** The optimal way is:
      
      Choose x = 14: [15, 10, 14, 12, 13] -> [10, 12, 13, 15, 14]
      
      Choose x = 15: [10, 12, 13, 15, 14] -> [10, 12, 13, 14, 15]
      
      So, the answer is [14, 15].

### Example 3

**Input:** `resource = [2, 4, 14, 10, 5, 3]`

**Output:** `[4, 10, 14]`

**Explanation:** The optimal way is:
      
      Choose x = 4: [2, 4, 14, 10, 5, 3] -> [2, 3, 4, 14, 10, 5]
      
      Choose x = 10: [2, 3, 4, 14, 10, 5] -> [2, 3, 4, 5, 14, 10]
      
      Choose x = 14: [2, 3, 4, 5, 14, 10] -> [2, 3, 4, 5, 10, 14]
      
      So, the answer is [4, 10, 14].

## Constraints

- `1 ≤ n ≤ 501 ≤ resource[i] ≤ 10^9All resource[i] are distinct`

## Solutions

<!-- Scaffold placeholder: the worked derivation and solutions land
     on the solutions branch later. See ../_TEMPLATE.md for the
     expected layout, naming, and ordering conventions. -->
