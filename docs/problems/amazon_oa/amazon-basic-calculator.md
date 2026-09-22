# [Basic Calculator](https://www.fastprep.io/problems/amazon-basic-calculator)

**Hard** | **NN minutes** | **String, Stack, Recursion**

Given a valid arithmetic expression s, return its evaluated integer value.The expression may contain:Non-negative integer literals.The binary operators + and -.Parentheses ( and ).Spaces.Unary + or - where a signed expression is valid.Integer division is not needed because the expression contains no multiplication or division operators.

## Examples

### Example 1

**Input:** `s = "1 + 1"`

**Output:** `2`

**Explanation:** The two operands sum to 2.

### Example 2

**Input:** `s = " 2-1 + 2 "`

**Output:** `3`

**Explanation:** Evaluate from left to right: 2 - 1 + 2 = 3.

### Example 3

**Input:** `s = "(1+(4+5+2)-3)+(6+8)"`

**Output:** `23`

**Explanation:** The first parenthesized group evaluates to 9, and 6 + 8 = 14, for a total of 23.

## Constraints

- `1 <= s.length <= 3 * 10^5s is a valid expression containing digits, +, -, (, ), and spaces.Every intermediate and final result fits in a signed 32-bit integer.`

## Solutions

<!-- Scaffold placeholder: the worked derivation and solutions land
     on the solutions branch later. See ../_TEMPLATE.md for the
     expected layout, naming, and ordering conventions. -->
