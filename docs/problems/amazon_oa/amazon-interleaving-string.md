# [Interleaving String](https://www.fastprep.io/problems/amazon-interleaving-string)

**Medium** | **NN minutes** | **Dynamic Programming, String**

Given strings s1, s2, and s3, return whether s3 can be formed by interleaving s1 and s2.

An interleaving uses every character from both source strings exactly once while preserving the left-to-right order within each source. Characters chosen from the two sources may alternate in groups of any positive length.

## Examples

### Example 1

**Input:** `s1 = "aabcc"`, `s2 = "dbbca"`, `s3 = "aadbbcbcac"`

**Output:** `true`

**Explanation:** The target can choose characters from both source strings while retaining each source's internal order.

### Example 2

**Input:** `s1 = "aabcc"`, `s2 = "dbbca"`, `s3 = "aadbbbaccc"`

**Output:** `false`

**Explanation:** Every possible choice eventually needs to reverse or skip a character from one source, so the target is not an interleaving.

### Example 3

**Input:** `s1 = ""`, `s2 = ""`, `s3 = ""`

**Output:** `true`

**Explanation:** The empty target uses every character from both empty source strings.

## Constraints

- `0 <= s1.length, s2.length <= 100.`
- `0 <= s3.length <= 200.`
- `All three strings contain only lowercase English letters.`

## Solutions

<!-- Scaffold placeholder: the worked derivation and solutions land
     on the solutions branch later. See ../_TEMPLATE.md for the
     expected layout, naming, and ordering conventions. -->
