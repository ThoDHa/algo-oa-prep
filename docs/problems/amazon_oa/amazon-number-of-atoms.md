# [Number of Atoms](https://www.fastprep.io/problems/amazon-number-of-atoms)

**Hard** | **NN minutes** | **String, Stack, Hash Table, Parsing, Sorting**

You are given a valid chemical formula string. Return the count of each atom as one canonical string.

An atom name starts with an uppercase letter and may be followed by lowercase letters. A number after an atom or a parenthesized group multiplies that atom or group. If no number follows, the multiplier is 1. Parentheses may be nested.

The output must list atom names in lexicographic order. For each atom, write the atom name followed by its count only when the count is greater than 1.

## Examples

### Example 1

**Input:** `formula = "H2O"`

**Output:** `"H2O"`

**Explanation:** There are two hydrogen atoms and one oxygen atom. The count for oxygen is omitted because it is 1.

### Example 2

**Input:** `formula = "Mg(OH)2"`

**Output:** `"H2MgO2"`

**Explanation:** The group (OH) is multiplied by 2, so the total counts are H:2, Mg:1, and O:2. Atom names are emitted in lexicographic order.

## Constraints

- `The formula is valid and contains atom names, positive integer multipliers, and parentheses.`
- `Parentheses may be nested.`

## Solutions

<!-- Scaffold placeholder: the worked derivation and solutions land
     on the solutions branch later. See ../_TEMPLATE.md for the
     expected layout, naming, and ordering conventions. -->
