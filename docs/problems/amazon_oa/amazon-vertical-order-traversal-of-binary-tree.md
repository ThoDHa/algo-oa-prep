# [Vertical Order Traversal of a Binary Tree](https://www.fastprep.io/problems/amazon-vertical-order-traversal-of-binary-tree)

**Medium** | **NN minutes** | **Tree, Breadth First Search, Hash Table, Sorting**

You are given a binary tree serialized as a level-order array levelOrder. Each non-null token is a signed decimal integer, and the token "null" denotes a missing child.Place the root at row 0, column 0. For a node at row r, column c:Its left child is at row r + 1, column c - 1.Its right child is at row r + 1, column c + 1.Return the node values grouped by column from the smallest column to the largest. Within one column, order nodes by increasing row. When multiple nodes share the same row and column, preserve their breadth-first left-to-right encounter order; do not sort them by value.If the tree is empty, return an empty list.

## Examples

### Example 1

**Input:** `levelOrder = ["3","9","20","null","null","15","7"]`

**Output:** `[[9],[3,15],[20],[7]]`

**Explanation:** The columns from left to right are -1, 0, 1, and 2.

### Example 2

**Input:** `levelOrder = ["1","2","3","4","6","5","7"]`

**Output:** `[[4],[2],[1,6,5],[3],[7]]`

**Explanation:** Nodes 6 and 5 share row 2 and column 0. Breadth-first left-to-right encounter order places 6 before 5.

### Example 3

**Input:** `levelOrder = []`

**Output:** `[]`

**Explanation:** An empty tree has no columns.

## Constraints

- `0 <= non-null node count <= 10^5.Every non-null token represents a signed 32-bit integer.levelOrder is a valid level-order serialization using "null" markers.`

## Solutions

<!-- Scaffold placeholder: the worked derivation and solutions land
     on the solutions branch later. See ../_TEMPLATE.md for the
     expected layout, naming, and ordering conventions. -->
