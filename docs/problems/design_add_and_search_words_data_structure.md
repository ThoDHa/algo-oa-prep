# [Design Add And Search Words Data Structure](https://leetcode.com/problems/design-add-and-search-words-data-structure/)

**Medium** | **NN minutes** | **String, Depth-First Search, Design, Trie**

Design a data structure that supports adding new words and searching for existing words.

Implement the `WordDictionary` class:

* `void addWord(word)` Adds `word` to the data structure.
* `bool search(word)` Returns `true` if there is any string in the data structure that matches `word` or `false` otherwise. `word` may contain dots `'.'` where dots can be matched with any letter.

## Examples

### Example 1

**Input:**

```
["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
[[],["day"],["bay"],["may"],["say"],["day"],[".ay"],["b.."]]
```

**Output:**

```
[null, null, null, null, false, true, true, true]
```

**Explanation:** WordDictionary wordDictionary = new WordDictionary();
wordDictionary.addWord("day");
wordDictionary.addWord("bay");
wordDictionary.addWord("may");
wordDictionary.search("say"); // return false
wordDictionary.search("day"); // return true
wordDictionary.search(".ay"); // return true
wordDictionary.search("b.."); // return true

## Constraints

- `1 <= word.length <= 25`
- `word` in `addWord` consists of lowercase English letters.
- `word` in `search` consist of `'.'` or lowercase English letters.
- There will be at most `2` dots in `word` for `search` queries.
- At most `10,000` calls will be made to `addWord` and `search`.

## Solutions

<!-- Scaffold placeholder: the worked derivation and solutions land
     on the solutions branch later. See ../_TEMPLATE.md for the
     expected layout, naming, and ordering conventions. -->
