# [Remove Duplicate Letters for the Largest Result](https://www.fastprep.io/problems/amazon-largest-lexicographic-unique-letters)

**Hard** | **NN minutes** | **String, Stack, Greedy**

Given a lowercase string s, remove characters so that every distinct letter appears exactly once. The remaining characters must preserve their original relative order.

Return the lexicographically largest possible result.

## Examples

### Example 1

**Input:** `s = "bcabc"`

**Output:** `"cab"`

**Explanation:** The subsequence cab contains each distinct letter once and is lexicographically largest.

### Example 2

**Input:** `s = "cbacdcbc"`

**Output:** `"cbad"`

**Explanation:** Keeping the early c and b allows the largest valid prefix.

### Example 3

**Input:** `s = "bbcaac"`

**Output:** `"bca"`

**Explanation:** The best unique-letter subsequence is bca.

## Constraints

- `1 ≤ s.length ≤ 100000.`
- `s contains only lowercase English letters.`

## Solutions

<!-- Scaffold placeholder: the worked derivation and solutions land
     on the solutions branch later. See ../_TEMPLATE.md for the
     expected layout, naming, and ordering conventions. -->
