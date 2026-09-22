# [All Anagram Start Indices](https://www.fastprep.io/problems/amazon-anagram-start-indices)

**Medium** | **NN minutes** | **String, Hash Table, Sliding Window**

Given lowercase strings s and p, return every starting index where a substring of s is an anagram of p.

Return indices in increasing order. Overlapping matches are included.

## Examples

### Example 1

**Input:** `s = "acbadabcaa"`, `p = "aabc"`

**Output:** `[0,5,6]`

**Explanation:** The length-four substrings at 0, 5, and 6 have exactly the pattern frequencies.

### Example 2

**Input:** `s = "cbaebabacd"`, `p = "abc"`

**Output:** `[0,6]`

**Explanation:** cba and bac are anagrams of abc.

### Example 3

**Input:** `s = "abab"`, `p = "ab"`

**Output:** `[0,1,2]`

**Explanation:** All three length-two windows match, including overlaps.

## Constraints

- `1 ≤ s.length, p.length ≤ 100000.`
- `s and p contain only lowercase English letters.`

## Solutions

<!-- Scaffold placeholder: the worked derivation and solutions land
     on the solutions branch later. See ../_TEMPLATE.md for the
     expected layout, naming, and ordering conventions. -->
