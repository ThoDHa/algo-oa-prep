# [Nodes at a Given N-ary Tree Level](https://www.fastprep.io/problems/amazon-nary-tree-nodes-at-level)

**Easy** | **NN minutes** | **Tree, Breadth First Search**

An N-ary tree uses node IDs from 0 through children.length - 1, with root ID 0. For each node ID, children[id] lists its child IDs from left to right.

Return the node IDs at zero-based level in left-to-right breadth-first order. Return an empty array when no nodes exist at that level.

## Examples

### Example 1

**Input:** `children = [[1,2,3],[4,5],[],[],[],[]]`, `level = 2`

**Output:** `[4,5]`

**Explanation:** Only nodes 4 and 5 are two edges from the root.

### Example 2

**Input:** `children = [[]]`, `level = 0`

**Output:** `[0]`

**Explanation:** Level zero contains the root.

### Example 3

**Input:** `children = [[1],[2],[3],[]]`, `level = 3`

**Output:** `[3]`

**Explanation:** The skewed tree has one node at level three.

## Constraints

- `1 ≤ children.length ≤ 100000.`
- `The child lists describe one valid rooted tree containing every node exactly once.`
- `0 ≤ level ≤ 100000.`

## Solutions

<!-- Scaffold placeholder: the worked derivation and solutions land
     on the solutions branch later. See ../_TEMPLATE.md for the
     expected layout, naming, and ordering conventions. -->
