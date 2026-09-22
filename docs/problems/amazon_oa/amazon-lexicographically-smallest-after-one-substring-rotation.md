# [Lexicographically Smallest After One Substring Rotation](https://www.fastprep.io/problems/amazon-lexicographically-smallest-after-one-substring-rotation)

**unknown difficulty** | **NN minutes** | **unknown categories**

You are given a string s. You must choose one non-empty contiguous substring of s and rotate that substring to the right by one position exactly once.

Rotating a substring to the right by one position moves its last character to the front of that substring, while every other character in the substring shifts one position to the right.

Return the lexicographically smallest string that can be obtained after performing the operation.

## Examples

### Example 1

**Input:** `s = "baca"`

**Output:** `"abac"`

**Explanation:** Choose the whole string baca. Rotating it right by one position moves the last character to the front, giving abac, which is the lexicographically smallest result obtainable.

### Example 2

**Input:** `s = "cba"`

**Output:** `"acb"`

**Explanation:** Choose the whole string "cba". Rotating it right gives "acb", which is the smallest possible result.

## Constraints

- `s is non-empty.`
- `The operation must be performed exactly once. Choosing a substring of length 1 leaves the string unchanged.`

## Solutions

<!-- Scaffold placeholder: the worked derivation and solutions land
     on the solutions branch later. See ../_TEMPLATE.md for the
     expected layout, naming, and ordering conventions. -->
