# [Longest Happy Prefix](https://www.fastprep.io/problems/amazon-longest-happy-prefix)

**Hard** | **NN minutes** | **String**

A string is a happy prefix of s when it is a non-empty proper prefix of s and is also a suffix of s.

Return the longest happy prefix. If none exists, return the empty string.

## Examples

### Example 1

**Input:** `s = "level"`

**Output:** `"l"`

**Explanation:** The prefix l is also the suffix, and no longer proper prefix matches.

### Example 2

**Input:** `s = "ababab"`

**Output:** `"abab"`

**Explanation:** The first four characters equal the last four characters.

### Example 3

**Input:** `s = "a"`

**Output:** `""`

**Explanation:** A one-character string has no non-empty proper prefix.

## Constraints

- `1 <= s.length <= 100000.`
- `s contains only lowercase English letters.`

## Solutions

<!-- Scaffold placeholder: the worked derivation and solutions land
     on the solutions branch later. See ../_TEMPLATE.md for the
     expected layout, naming, and ordering conventions. -->
