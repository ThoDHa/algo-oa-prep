# [Cousins in Binary Tree II](https://www.fastprep.io/problems/amazon-cousins-in-binary-tree-ii)

**Medium** | **NN minutes** | **Tree, Breadth First Search, Depth First Search**

You are given a non-empty binary tree serialized as a level-order string array levelOrder. Each non-null token is a decimal integer, and "null" denotes a missing child.Replace every node's value with the sum of the original values of all its cousins. Two nodes are cousins when they are at the same depth and have different parents. If a node has no cousins, its replacement value is 0.All replacements are conceptually simultaneous. Return the updated tree using the same level-order array shape, preserving every "null" marker from the input.

## Examples

### Example 1

**Input:** `levelOrder = ["5","4","9","1","10","null","7"]`

**Output:** `["0","0","0","7","7","null","11"]`

**Explanation:** At depth 2, nodes 1 and 10 are siblings, so their only cousin has value 7. Node 7 has cousins with original values 1 and 10, whose sum is 11.

### Example 2

**Input:** `levelOrder = ["3","1","2"]`

**Output:** `["0","0","0"]`

**Explanation:** The root has no cousins, and the two nodes at depth 1 are siblings, so every replacement is 0.

### Example 3

**Input:** `levelOrder = ["1","2","3","4","null","5","6"]`

**Output:** `["0","0","0","11","null","4","4"]`

**Explanation:** At depth 2, node 4 receives 5 + 6 = 11, while sibling nodes 5 and 6 each receive the cousin value 4.

## Constraints

<!-- Constraints not parseable from FastPrep for amazon-cousins-in-binary-tree-ii; fill them in. -->

## Solutions

<!-- Scaffold placeholder: the worked derivation and solutions land
     on the solutions branch later. See ../_TEMPLATE.md for the
     expected layout, naming, and ordering conventions. -->
