# [Decode an Encoded String](https://www.fastprep.io/problems/amazon-decode-encoded-string)

**Medium** | **NN minutes** | **String, Stack, Parsing**

An encoded string uses positive repeat counts followed by bracketed segments. Decode it using these rules:

k[segment] means the decoded segment is repeated exactly k times.Segments may be nested.Letters outside brackets appear once and remain in order.Return the fully decoded string.

## Examples

### Example 1

**Input:** `s = "3[a2[c]]"`

**Output:** `"accaccacc"`

**Explanation:** The inner block becomes acc, then the outer count repeats it three times.

### Example 2

**Input:** `s = "2[ab]3[c]"`

**Output:** `"ababccc"`

**Explanation:** The two adjacent encoded blocks decode independently and are concatenated.

## Constraints

- `1 <= s.length <= 10^4`
- `s is a well-formed encoding made of lowercase English letters, digits, and brackets.`
- `Every repeat count is between 1 and 300.`
- `The decoded string has at most 10^5 characters.`

## Solutions

<!-- Scaffold placeholder: the worked derivation and solutions land
     on the solutions branch later. See ../_TEMPLATE.md for the
     expected layout, naming, and ordering conventions. -->
