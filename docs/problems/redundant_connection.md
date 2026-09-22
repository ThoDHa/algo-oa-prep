# [Redundant Connection](https://leetcode.com/problems/redundant-connection/)

**Medium** | **NN minutes** | **Depth-First Search, Breadth-First Search, Union Find, Graph Theory**

You are given a connected **undirected graph** with `n` nodes labeled from `1` to `n`. Initially, it contained no cycles and consisted of `n-1` edges.

We have now added one additional edge to the graph. The edge has two **different** vertices chosen from `1` to `n`, and was not an edge that previously existed in the graph.

The graph is represented as an array `edges` of length `n` where `edges[i] = [ai, bi]` represents an edge between nodes `ai` and `bi` in the graph.

Return an edge that can be removed so that the graph is still a connected non-cyclical graph. If there are multiple answers, return the edge that appears last in the input `edges`.

## Examples

### Example 1

**Input:** `edges = [[1,2],[1,3],[3,4],[2,4]]`

**Output:** `[2,4]`

### Example 2

**Input:** `edges = [[1,2],[1,3],[1,4],[3,4],[4,5]]`

**Output:** `[3,4]`

## Constraints

- `n == edges.length`
- `3 <= n <= 1000`
- `1 <= edges[i][0] < edges[i][1] <= edges.length`
- There are no repeated edges and no self-loops in the input.

## Solutions

<!-- Scaffold placeholder: the worked derivation and solutions land
     on the solutions branch later. See ../_TEMPLATE.md for the
     expected layout, naming, and ordering conventions. -->
