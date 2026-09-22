# [Count Connected Components](https://www.fastprep.io/problems/amazon-count-connected-components)

**Easy** | **NN minutes** | **Graph, Union Find, Depth First Search**

You are given an undirected graph with n nodes and a list of edges. Each edge connects two nodes in the graph.Return the number of connected components in the graph. A connected component is a maximal group of nodes where every pair of nodes is connected by some path.Function Description Complete the function countConnectedComponents in the editor.countConnectedComponents has the following parameters:int n: the number of nodes, labeled from 0 to n - 1int edges[][]: an array where each element [u, v] represents an undirected edge between nodes u and vReturns int: the number of connected components in the graph

## Examples

### Example 1

**Input:** `n = 5`
**Input:** `edges = [[0, 1], [1, 2], [3, 4]]`

**Output:** `2`

**Explanation:** Nodes 0, 1, and 2 form one connected component. Nodes 3 and 4 form another connected component. Therefore, there are 2 connected components.

### Example 2

**Input:** `n = 5`
**Input:** `edges = [[0, 1], [1, 2], [2, 0], [3, 4]]`

**Output:** `2`

**Explanation:** The cycle among nodes 0, 1, and 2 is still one connected component. Nodes 3 and 4 form the second component.

### Example 3

**Input:** `n = 4`
**Input:** `edges = []`

**Output:** `4`

**Explanation:** With no edges, every node is isolated, so each node is its own connected component.

## Constraints

- `Nodes are labeled from 0 to n - 1.The graph is undirected.The input edges are valid node pairs.`

## Solutions

<!-- Scaffold placeholder: the worked derivation and solutions land
     on the solutions branch later. See ../_TEMPLATE.md for the
     expected layout, naming, and ordering conventions. -->
