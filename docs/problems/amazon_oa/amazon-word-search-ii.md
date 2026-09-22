# [Word Search II](https://www.fastprep.io/problems/amazon-word-search-ii)

**Hard** | **NN minutes** | **Trie, Backtracking, Matrix, Depth First Search**

Given an m x n board of lowercase English letters and an array of distinct lowercase words, return every word that can be formed on the board.A word is formed by starting at any cell and repeatedly moving one cell horizontally or vertically. A board cell may be used at most once while forming one word.Return found words in the same order in which they appear in words.

## Examples

### Example 1

**Input:** `board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]`
**Input:** `words = ["oath","pea","eat","rain"]`

**Output:** `["oath","eat"]`

**Explanation:** The paths o-a-t-h and e-a-t use horizontal or vertical neighbors without reusing a cell.

### Example 2

**Input:** `board = [["a","b"],["c","d"]]`
**Input:** `words = ["abcb","abcd","acdb"]`

**Output:** `["acdb"]`

**Explanation:** acdb follows the path down, right, then up. The other words require a reused cell or a diagonal move.

## Constraints

- `1 <= m, n <= 12.1 <= words.length <= 30000.1 <= words[i].length <= 10.The board and every word contain only lowercase English letters.All words are distinct.`

## Solutions

<!-- Scaffold placeholder: the worked derivation and solutions land
     on the solutions branch later. See ../_TEMPLATE.md for the
     expected layout, naming, and ordering conventions. -->
