# [Binary Tree Cameras](https://www.fastprep.io/problems/amazon-binary-tree-cameras)

**Hard** | **NN minutes** | **Tree, Depth First Search, Dynamic Programming, Greedy**

You are given the root of a binary tree. You may install cameras on its nodes.A camera installed at a node monitors that node, its parent if one exists, and its immediate children.Return the minimum number of cameras needed so that every node in the tree is monitored.

## Examples

### Example 1

**Input:** `root = [0,0,null,0,0]`

**Output:** `1`

**Explanation:** Place one camera on the second node in the level-order representation. It monitors its parent, itself, and both of its children, so every node is covered.

### Example 2

**Input:** `root = [0,0,null,0,null,0,null,null,0]`

**Output:** `2`

**Explanation:** No single camera can monitor the entire chain-like tree. Two cameras placed at suitable internal nodes are sufficient.

### Example 3

**Input:** `root = [0]`

**Output:** `1`

**Explanation:** The only node must be monitored, so installing one camera on the root is optimal.

## Constraints

- `The tree contains between 1 and 1000 nodes.Every node has value 0.`

## Solutions

<!-- Scaffold placeholder: the worked derivation and solutions land
     on the solutions branch later. See ../_TEMPLATE.md for the
     expected layout, naming, and ordering conventions. -->
