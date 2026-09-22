# [Regular Expression Matching](https://leetcode.com/problems/regular-expression-matching/)

**Hard** | **NN minutes** | **String, Dynamic Programming, Recursion**

You are given an input string `s` consisting of lowercase english letters, and a pattern `p` consisting of lowercase english letters, as well as `'.'`, and `'*'` characters.

Return `true` if the pattern matches the **entire** input string, otherwise return `false`.

* `'.'` Matches any single character
* `'*'` Matches zero or more of the preceding element.

## Examples

### Example 1

**Input:** `s = "aa", p = ".b"`

**Output:** `false`

**Explanation:** Regardless of which character we choose for the `'.'` in the pattern, we cannot match the second character in the input string.

### Example 2

**Input:** `s = "nnn", p = "n*"`

**Output:** `true`

**Explanation:** `'*'` means zero or more of the preceding element, `'n'`. We choose `'n'` to repeat three times.

### Example 3

**Input:** `s = "xyz", p = ".*z"`

**Output:** `true`

**Explanation:** The pattern `".*"` means zero or more of any character, so we choose `".."` to match `"xy"` and `"z"` to match `"z"`.

## Constraints

- `1 <= s.length <= 20`
- `1 <= p.length <= 20`
- Each appearance of `'*'`, will be preceded by a valid character or `'.'`.

## Solutions

<!-- Scaffold placeholder: the worked derivation and solutions land
     on the solutions branch later. See _TEMPLATE.md for the
     expected layout, naming, and ordering conventions. -->
