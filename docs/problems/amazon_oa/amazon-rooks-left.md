# [Rooks Left](https://www.fastprep.io/problems/amazon-rooks-left)

**Medium** | **NN minutes** | **Matrix, Union Find, Graph**

$23

## Examples

### Example 1

**Input:** `board = [[1, 0, 1, 0, 0], [1, 0, 1, 0, 0], [1, 0, 1, 1, 0]]`

**Output:** `1`

**Explanation:** All the rooks are connected either directly or indirectly in the same row or column, forming one single connected group.

### Example 2

**Input:** `board = [[0, 0, 1, 0, 0], [1, 0, 1, 0, 0], [1, 0, 0, 0, 1], [0, 0, 1, 1, 0]]`

**Output:** `1`

**Explanation:** All the rooks can reach each other, either directly or through a sequence of moves along rows or columns, resulting in one connected component.

### Example 3

**Input:** `board = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]`

**Output:** `3`

**Explanation:** There are 3 rooks, and none of them share the same row or column. Thus, each rook is isolated, resulting in 3 connected components.

### Example 4

**Input:** `board = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]`

**Output:** `1`

**Explanation:** All rooks are connected in both rows and columns, forming one single connected component.

### Example 5

**Input:** `board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]`

**Output:** `0`

**Explanation:** There are no rooks on the board.

### Example 6

**Input:** `board = [[1]]`

**Output:** `1`

**Explanation:** There is single rook, resulting in one connected component.

### Example 7

**Input:** `board = [[1, 0], [1, 0]]`

**Output:** `1`

**Explanation:** The two rooks are in the same row, forming one connected group.

### Example 8

**Input:** `board = [[1, 0, 0], [1, 0, 0], [0, 0, 1]]`

**Output:** `2`

**Explanation:** The two rooks in the first two rows share the sam column, forming one connected component.The rook in the third row is isolated, resulting in a total of two connected components.

## Constraints

- `The dimensions of the board are 1 <= n, m <= 1000.`
- `Each cell contains either 0 or 1.`

## Solutions

<!-- Scaffold placeholder: the worked derivation and solutions land
     on the solutions branch later. See ../_TEMPLATE.md for the
     expected layout, naming, and ordering conventions. -->
