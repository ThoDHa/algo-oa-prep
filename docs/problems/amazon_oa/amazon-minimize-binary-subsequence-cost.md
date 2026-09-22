# [Minimize Binary Subsequence Cost](https://www.fastprep.io/problems/amazon-minimize-binary-subsequence-cost)

**unknown difficulty** | **NN minutes** | **unknown categories**

You are given a string binaryString consisting only of '0', '1', and '!', and two integers x and y.Replace every '!' with either '0' or '1'. After replacement, every subsequence equal to "01" contributes cost x, and every subsequence equal to "10" contributes cost y.Return the minimum possible total cost modulo 1_000_000_007.

## Examples

### Example 1

**Input:** `binaryString = "101!1"`
**Input:** `x = 2`
**Input:** `y = 3`

**Output:** `9`

**Explanation:** Replacing '!' with '0' gives cost 15. Replacing it with '1' gives cost 9, which is optimal.

### Example 2

**Input:** `binaryString = "!!!!!"`
**Input:** `x = 2`
**Input:** `y = 3`

**Output:** `0`

**Explanation:** Replace all characters with the same bit, so there are no "01" or "10" subsequences.

## Constraints

- `1 <= binaryString.length <= 10^50 <= x, y <= 10^5binaryString contains only '0', '1', and '!'.`

## Solutions

<!-- Scaffold placeholder: the worked derivation and solutions land
     on the solutions branch later. See ../_TEMPLATE.md for the
     expected layout, naming, and ordering conventions. -->
