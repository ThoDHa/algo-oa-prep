# [Number of Connected Components In An Undirected Graph](https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/)

**Medium** | **NN minutes** | **Depth-First Search, Breadth-First Search, Union Find, Graph Theory**

> This problem is locked behind [LeetCode Premium](https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/); read it free on [NeetCode](https://neetcode.io/problems/count-connected-components).

You have an undirected graph of `n` nodes labeled from `0` to `n - 1`. You are given an integer `n` and an array `edges` where `edges[i] = [aᵢ, bᵢ]` indicates that there is an edge between `aᵢ` and `bᵢ` in the graph.

Return the number of connected components in the graph.

## Examples

### Example 1

**Input:** `n = 5, edges = [[0,1],[1,2],[3,4]]`

**Output:** `2`

### Example 2

**Input:** `n = 5, edges = [[0,1],[1,2],[2,3],[3,4]]`

**Output:** `1`

## Constraints

- `1 <= n <= 2000`
- `1 <= edges.length <= 5000`
- `edges[i].length == 2`
- `0 <= aᵢ < n`
- `0 <= bᵢ < n`
- `aᵢ != bᵢ`
- There are no repeated edges.

## Solutions

<!-- Scaffold placeholder: the worked derivation and solutions land
     on the solutions branch later. See ../_TEMPLATE.md for the
     expected layout, naming, and ordering conventions. -->
