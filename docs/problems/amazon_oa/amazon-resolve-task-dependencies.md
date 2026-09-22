# [Resolve Task Dependencies](https://www.fastprep.io/problems/amazon-resolve-task-dependencies)

**Hard** | **NN minutes** | **Graph, Topological Sort, Heap**

There are n tasks numbered from 0 through n - 1. A dependency [u, v] means task u must be completed before task v.

The array mandatory contains dependencies that cannot be removed. Each row [u, v, cost] in optional contains a removable dependency u -> v and its cost.

If the graph containing every dependency is acyclic, return its lexicographically smallest topological order without removing anything.If it is cyclic, consider removing exactly one optional dependency. Among the optional dependencies whose removal makes the entire graph acyclic, remove the one with the smallest cost. If costs tie, remove the one appearing earlier in optional. Return the lexicographically smallest topological order of the resulting graph.If no single optional dependency can make the graph acyclic, return an empty array.

## Examples

### Example 1

**Input:** `n = 4`, `mandatory = [[0,1],[2,3]]`, `optional = [[1,2,7]]`

**Output:** `[0,1,2,3]`

**Explanation:** All dependencies are already acyclic, so none is removed. The only valid order is [0,1,2,3].

### Example 2

**Input:** `n = 3`, `mandatory = [[0,1]]`, `optional = [[1,2,5],[2,0,2]]`

**Output:** `[0,1,2]`

**Explanation:** The dependencies form the cycle 0 -> 1 -> 2 -> 0. Removing 2 -> 0 costs 2, which is cheaper than removing 1 -> 2.

### Example 3

**Input:** `n = 2`, `mandatory = [[0,1],[1,0]]`, `optional = []`

**Output:** `[]`

**Explanation:** The mandatory dependencies form a cycle, and there is no optional dependency that can be removed.

## Constraints

- `1 <= n <= 500`
- `0 <= mandatory.length, optional.length`
- `mandatory.length + optional.length <= 2000`
- `Every dependency endpoint is in [0, n - 1], and no dependency is repeated.`
- `0 <= cost <= 1000000000`

## Solutions

<!-- Scaffold placeholder: the worked derivation and solutions land
     on the solutions branch later. See ../_TEMPLATE.md for the
     expected layout, naming, and ordering conventions. -->
