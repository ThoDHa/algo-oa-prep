# [Word Break](https://www.fastprep.io/problems/amazon-word-break)

**Medium** | **NN minutes** | **Array, Hash Table, String, Dynamic Programming**

Given a string s and an array of distinct dictionary words wordDict, return true if s can be split into a sequence of one or more dictionary words.A dictionary word may be reused any number of times.

## Examples

### Example 1

**Input:** `s = "leetcode"`
**Input:** `wordDict = ["leet","code"]`

**Output:** `true`

**Explanation:** The string splits as leet + code.

### Example 2

**Input:** `s = "applepenapple"`
**Input:** `wordDict = ["apple","pen"]`

**Output:** `true`

**Explanation:** The word apple is reused in apple + pen + apple.

### Example 3

**Input:** `s = "catsandog"`
**Input:** `wordDict = ["cats","dog","sand","and","cat"]`

**Output:** `false`

**Explanation:** No sequence of dictionary words covers the entire string.

## Constraints

- `1 <= s.length <= 300.1 <= wordDict.length <= 1000.1 <= wordDict[i].length <= 20.s and every dictionary word contain only lowercase English letters.All dictionary words are distinct.`

## Solutions

<!-- Scaffold placeholder: the worked derivation and solutions land
     on the solutions branch later. See ../_TEMPLATE.md for the
     expected layout, naming, and ordering conventions. -->
