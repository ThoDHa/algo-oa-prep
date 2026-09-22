# [Distinct Subsequences](https://leetcode.com/problems/distinct-subsequences/)

**Hard** | **NN minutes** | **String, Dynamic Programming**

You are given two strings `s` and `t`, both consisting of english letters.

Return the number of distinct **subsequences** of `s` which are equal to `t`.

## Examples

### Example 1

**Input:** `s = "caaat", t = "cat"`

**Output:** `3`

**Explanation:** There are 3 ways you can generate `"cat"` from `s`.
* (c)aa(at)
* (c)a(a)a(t)
* (ca)aa(t)

### Example 2

**Input:** `s = "xxyxy", t = "xy"`

**Output:** `5`

**Explanation:** There are 5 ways you can generate `"xy"` from `s`.
* (x)x(y)xy
* (x)xyx(y)
* x(x)(y)xy
* x(x)yx(y)
* xxy(x)(y)

## Constraints

- `1 <= s.length, t.length <= 1000`
- `s` and `t` consist of English letters.

## Solutions

<!-- Scaffold placeholder: the worked derivation and solutions land
     on the solutions branch later. See ../_TEMPLATE.md for the
     expected layout, naming, and ordering conventions. -->
