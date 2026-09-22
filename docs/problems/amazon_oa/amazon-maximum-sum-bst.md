# [Maximum Sum BST in a Binary Tree](https://www.fastprep.io/problems/amazon-maximum-sum-bst)

**Hard** | **NN minutes** | **Tree, Depth First Search, Dynamic Programming**

Given the root of a binary tree, find the maximum sum of node values among all subtrees that are valid binary search trees.

A valid BST has every left-subtree value strictly smaller than its root and every right-subtree value strictly larger. Return 0 when every valid non-empty BST subtree has a negative sum.

## Examples

### Example 1

**Input:** `root = [1,4,3,2,4,2,5,null,null,null,null,null,null,4,6]`

**Output:** `20`

**Explanation:** The subtree rooted at 3 is a BST with sum 20.

### Example 2

**Input:** `root = [4,3,null,1,2]`

**Output:** `2`

**Explanation:** The leaf with value 2 is the best valid BST subtree.

### Example 3

**Input:** `root = [-4,-2,-5]`

**Output:** `0`

**Explanation:** All valid BST sums are negative, so zero is returned.

## Constraints

- `The tree contains between 0 and 5000 nodes.`
- `-10000 ≤ Node.val ≤ 10000.`

## Solutions

<!-- Scaffold placeholder: the worked derivation and solutions land
     on the solutions branch later. See ../_TEMPLATE.md for the
     expected layout, naming, and ordering conventions. -->
