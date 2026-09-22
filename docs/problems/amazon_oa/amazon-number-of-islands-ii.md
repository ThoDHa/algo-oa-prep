# [Number of Islands II](https://www.fastprep.io/problems/amazon-number-of-islands-ii)

**Hard** | **NN minutes** | **Array, Matrix, Graph, Union Find**

Start with an m by n grid containing only water. For each distinct position [row, col] in positions, turn that cell into land and append the current number of islands to the result.An island is a maximal group of land cells connected vertically or horizontally. Diagonal cells are not connected.Interview follow-upThe rest of the discussion covered the DSU approach, how union-find works, edge cases, and the time and space complexity.

## Examples

### Example 1

**Input:** `m = 3`
**Input:** `n = 3`
**Input:** `positions = [[0,0],[0,1],[1,2],[2,1]]`

**Output:** `[1,1,2,3]`

**Explanation:** The second cell joins the first island. The final two additions are not four-directionally adjacent to existing land.

### Example 2

**Input:** `m = 2`
**Input:** `n = 2`
**Input:** `positions = [[0,0],[1,1],[0,1]]`

**Output:** `[1,2,1]`

**Explanation:** The third addition connects the two existing islands into one.

## Constraints

<!-- Constraints not parseable from FastPrep for amazon-number-of-islands-ii; fill them in. -->

## Solutions

<!-- Scaffold placeholder: the worked derivation and solutions land
     on the solutions branch later. See ../_TEMPLATE.md for the
     expected layout, naming, and ordering conventions. -->
