# [Count the Number of Complete Components](https://www.fastprep.io/problems/amazon-count-complete-components)

**Medium** | **NN minutes** | **Graph, Depth First Search, Breadth First Search, Union Find**

You are given an integer n and an undirected graph whose vertices are numbered from 0 through n - 1. The array edges contains each undirected edge [u, v].

A connected component is complete when every pair of distinct vertices in that component is joined by an edge.

Return the number of complete connected components. A component containing one vertex is complete.

## Examples

### Example 1

**Input:** `n = 6`, `edges = [[0,1],[0,2],[1,2],[3,4]]`

**Output:** `3`

**Explanation:** The components are {0,1,2}, {3,4}, and {5}. Each contains every possible internal edge, so all three are complete.

### Example 2

**Input:** `n = 6`, `edges = [[0,1],[0,2],[1,2],[3,4],[3,5]]`

**Output:** `1`

**Explanation:** The component {0,1,2} is complete. The component {3,4,5} is missing edge [4,5], so it is not complete.

### Example 3

**Input:** `n = 1`, `edges = []`

**Output:** `1`

**Explanation:** The only vertex forms a one-vertex complete component.

## Constraints

<!-- Constraints not parseable from FastPrep for amazon-count-complete-components; fill them in. -->

## Solutions

<!-- Scaffold placeholder: the worked derivation and solutions land
     on the solutions branch later. See ../_TEMPLATE.md for the
     expected layout, naming, and ordering conventions. -->
