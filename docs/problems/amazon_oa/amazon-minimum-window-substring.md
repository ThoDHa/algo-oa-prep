# [Minimum Window Substring](https://www.fastprep.io/problems/amazon-minimum-window-substring)

**Hard** | **NN minutes** | **String, Hash Table, Sliding Window**

Given non-empty strings s and t, return the shortest contiguous substring of s that contains every character of t, including duplicate occurrences.

If no window exists, return the empty string. If several shortest windows exist, return the one with the smallest starting index.

## Examples

### Example 1

**Input:** `s = "ADOBECODEBANC"`, `t = "ABC"`

**Output:** `"BANC"`

**Explanation:** BANC is the shortest window containing A, B, and C.

### Example 2

**Input:** `s = "a"`, `t = "a"`

**Output:** `"a"`

**Explanation:** The whole one-character string is the answer.

### Example 3

**Input:** `s = "a"`, `t = "aa"`

**Output:** `""`

**Explanation:** The source does not contain enough copies of a.

## Constraints

- `1 ≤ s.length, t.length ≤ 100000.`
- `s and t contain printable ASCII characters.`
- `The total input length fits in memory.`

## Solutions

<!-- Scaffold placeholder: the worked derivation and solutions land
     on the solutions branch later. See ../_TEMPLATE.md for the
     expected layout, naming, and ordering conventions. -->
