# [Valid Parenthesis String](https://leetcode.com/problems/valid-parenthesis-string/)

**Medium** | **NN minutes** | **String, Dynamic Programming, Stack, Greedy**

You are given a string `s` which contains only three types of characters: `'('`, `')'` and `'*'`.

Return `true` if `s` is **valid**, otherwise return `false`.

A string is valid if it follows all of the following rules:

* Every left parenthesis `'('` must have a corresponding right parenthesis `')'`.
* Every right parenthesis `')'` must have a corresponding left parenthesis `'('`.
* Left parenthesis `'('` must go before the corresponding right parenthesis `')'`.
* A `'*'` could be treated as a right parenthesis `')'` character or a left parenthesis `'('` character, or as an empty string `""`.

## Examples

### Example 1

**Input:** `s = "((**)"`

**Output:** `true`

**Explanation:** One of the `'*'` could be a `')'` and the other could be an empty string.

### Example 2

**Input:** `s = "(((*)"`

**Output:** `false`

**Explanation:** The string is not valid because there is an extra `'('` at the beginning, regardless of the extra `'*'`.

## Constraints

- `1 <= s.length <= 100`

## Solutions

<!-- Scaffold placeholder: the worked derivation and solutions land
     on the solutions branch later. See ../_TEMPLATE.md for the
     expected layout, naming, and ordering conventions. -->
