# [Construct a Tree from Level-Order and Inorder Traversals](https://www.fastprep.io/problems/amazon-construct-tree-level-inorder)

**Hard** | **NN minutes** | **Array, Hash Table, Tree, Recursion, Stack**

Given the levelOrder and inorder traversals of the same binary tree, reconstruct and return its root.All node values are distinct. Both arrays contain the same values, and together they describe exactly one valid binary tree.

## Examples

### Example 1

**Input:** `levelOrder = [3,9,20,15,7]`
**Input:** `inorder = [9,3,15,20,7]`

**Output:** `[3,9,20,null,null,15,7]`

**Explanation:** The root 3 appears first in level order; the inorder split places 9 left and the remaining nodes right.

### Example 2

**Input:** `levelOrder = [1]`
**Input:** `inorder = [1]`

**Output:** `[1]`

**Explanation:** Both traversals describe a one-node tree.

### Example 3

**Input:** `levelOrder = [1,2,3,4,5]`
**Input:** `inorder = [4,2,5,1,3]`

**Output:** `[1,2,3,4,5]`

**Explanation:** The traversals reconstruct the shown complete upper levels.

## Constraints

- `1 <= levelOrder.length == inorder.length <= 1200.-10^9 <= levelOrder[i], inorder[i] <= 10^9.Each traversal contains distinct values, and both contain the same set of values.The arrays are valid traversals of one binary tree.`

## Solutions

<!-- Scaffold placeholder: the worked derivation and solutions land
     on the solutions branch later. See ../_TEMPLATE.md for the
     expected layout, naming, and ordering conventions. -->
