# [Word Search II](https://leetcode.com/problems/word-search-ii/)

**Hard** | **NN minutes** | **Array, String, Backtracking, Trie, Matrix**

Given a 2-D grid of characters `board` and a list of strings `words`, return all words that are present in the grid.

For a word to be present it must be possible to form the word with a path in the board with horizontally or vertically neighboring cells. The same cell may not be used more than once in a word.

## Examples

### Example 1

**Input:**

```
board = [
  ["a","b","c","d"],
  ["s","a","a","t"],
  ["a","c","k","e"],
  ["a","c","d","n"]
],
words = ["bat","cat","back","backend","stack"]
```

**Output:**

```
["cat","back","backend"]
```

### Example 2

**Input:**

```
board = [
  ["x","o"],
  ["x","o"]
],
words = ["xoxo"]
```

**Output:**

```
[]
```

## Constraints

- `1 <= board.length, board[i].length <= 12`
- `board[i]` consists only of lowercase English letter.
- `1 <= words.length <= 30,000`
- `1 <= words[i].length <= 10`
- `words[i]` consists only of lowercase English letters.
- All strings within `words` are distinct.

## Solutions

<!-- Scaffold placeholder: the worked derivation and solutions land
     on the solutions branch later. See ../_TEMPLATE.md for the
     expected layout, naming, and ordering conventions. -->
