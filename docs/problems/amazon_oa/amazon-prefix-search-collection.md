# [Dynamic Prefix Search Collection](https://www.fastprep.io/problems/amazon-prefix-search-collection)

**Medium** | **NN minutes** | **Trie, String, Design**

Implement a dynamic collection of lowercase words. Process the finite array operations from left to right.Each operation has one of these forms:INSERT word: add word to the collection. Inserting a word that is already present does not create a duplicate.SEARCH prefix: return up to three stored words that begin with prefix, ordered lexicographically.The collection starts empty. Return one row for every SEARCH operation, in command order. INSERT operations do not produce output.

## Examples

### Example 1

**Input:** `operations = ["INSERT mouse","INSERT mobile","INSERT moneypot","INSERT monitor","INSERT mousepad","SEARCH mo","SEARCH mou"]`

**Output:** `[["mobile","moneypot","monitor"],["mouse","mousepad"]]`

**Explanation:** The first search keeps the three lexicographically smallest matches for mo. The longer prefix mou has only two matches.

### Example 2

**Input:** `operations = ["INSERT app","INSERT apple","SEARCH ap","INSERT apex","INSERT app","SEARCH ap","SEARCH z"]`

**Output:** `[["app","apple"],["apex","app","apple"],[]]`

**Explanation:** The second insertion of app is idempotent. After apex is added, it is first lexicographically. No stored word begins with z.

## Constraints

- `1 <= operations.length <= 100000.Every operation is exactly one documented command with one separating space.Every word and prefix contains 1 to 100 lowercase English letters.The total number of characters across all operations is at most 1000000.At least one operation is SEARCH.`

## Solutions

<!-- Scaffold placeholder: the worked derivation and solutions land
     on the solutions branch later. See ../_TEMPLATE.md for the
     expected layout, naming, and ordering conventions. -->
