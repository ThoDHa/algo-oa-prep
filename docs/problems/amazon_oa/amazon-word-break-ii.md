# [Word Break II](https://www.fastprep.io/problems/amazon-word-break-ii)

**Hard** | **NN minutes** | **Array, Hash Table, String, Dynamic Programming, Backtracking, Trie**

Given a string s and an array of unique dictionary words wordDict, insert spaces into s so that every resulting token is a dictionary word.

Return every valid sentence in lexicographic order. A dictionary word may be reused any number of times.

## Examples

### Example 1

**Input:** `s = "catsanddog"`, `wordDict = ["cat","cats","and","sand","dog"]`

**Output:** `["cat sand dog","cats and dog"]`

**Explanation:** The string can be segmented as cat sand dog or cats and dog. The two sentences are returned in lexicographic order.

### Example 2

**Input:** `s = "pineapplepenapple"`, `wordDict = ["apple","pen","applepen","pine","pineapple"]`

**Output:** `["pine apple pen apple","pine applepen apple","pineapple pen apple"]`

**Explanation:** All three sentences concatenate to pineapplepenapple, and dictionary words such as apple may be reused.

### Example 3

**Input:** `s = "catsandog"`, `wordDict = ["cats","dog","sand","and","cat"]`

**Output:** `[]`

**Explanation:** No sequence of dictionary words concatenates to the entire string.

## Constraints

- `1 <= s.length <= 20`
- `1 <= wordDict.length <= 1000`
- `1 <= wordDict[i].length <= 10`
- `s and every wordDict[i] contain only lowercase English letters.`
- `All strings in wordDict are unique.`
- `The total length of all valid output sentences does not exceed 10^5.`

## Solutions

<!-- Scaffold placeholder: the worked derivation and solutions land
     on the solutions branch later. See ../_TEMPLATE.md for the
     expected layout, naming, and ordering conventions. -->
