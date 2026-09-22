# [Count Uni-Valued Subtrees](https://www.fastprep.io/problems/amazon-count-univalued-subtrees)

**Medium** | **NN minutes** | **Tree, Depth First Search, Recursion**

Given the root of a binary tree, return the number of subtrees whose nodes all have the same value.

Every node defines one subtree consisting of that node and all of its descendants. A leaf is therefore always a uni-valued subtree.

## Examples

### Example 1

**Input:** `root = [5,1,5,5,5,null,5]`

**Output:** `4`

**Explanation:** The three leaf fives and the right subtree rooted at five are uni-valued.

### Example 2

**Input:** `root = [1]`

**Output:** `1`

**Explanation:** A leaf is uni-valued.

### Example 3

**Input:** `root = []`

**Output:** `0`

**Explanation:** An empty tree contains no subtree.

## Constraints

- `The tree contains between 0 and 500 nodes.`
- `-1000 ≤ Node.val ≤ 1000.`

## Solutions

<!-- Scaffold placeholder: the worked derivation and solutions land
     on the solutions branch later. See ../_TEMPLATE.md for the
     expected layout, naming, and ordering conventions. -->
