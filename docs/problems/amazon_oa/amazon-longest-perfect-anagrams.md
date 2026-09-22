# [Longest Perfect Anagrams](https://www.fastprep.io/problems/amazon-longest-perfect-anagrams)

**Hard** | **NN minutes** | **String, Hash Table, Sliding Window**

$23

## Examples

### Example 1

**Input:** `s = "abcacb"`

**Output:** `4`

**Explanation:** The string s = "abcacbab",
      
        Pairs of substrings such as ("ca", "ac"), ("abc", "acb"), ("bca", "acb"), ("bcac", "cacb"), etc. are perfect anagrams.
        Among these, the longest are ("bcac", "cacb").
      
      It can be proven that no two substrings of length greater than 4 in the given string are perfect anagrams. Return 4.

### Example 2

**Input:** `s = "cabcab"`

**Output:** `3`

**Explanation:** ("cab","bca") , ('abc,'bca'') are two such 3 length substrings

### Example 3

**Input:** `s = "aabbcc"`

**Output:** `-1`

**Explanation:** There are no perfect anagram. a & a , b&b , c& c are exctly same.

## Constraints

- `1 ≤ |s| ≤ 10^5`
- `string s contains lowercase English characters only.`

## Solutions

<!-- Scaffold placeholder: the worked derivation and solutions land
     on the solutions branch later. See ../_TEMPLATE.md for the
     expected layout, naming, and ordering conventions. -->
