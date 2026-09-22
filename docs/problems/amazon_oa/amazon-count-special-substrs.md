# [Count Special Substrings](https://www.fastprep.io/problems/amazon-count-special-substrs)

**Medium** | **NN minutes** | **String, Prefix Sum, Hash Table**

$23

## Examples

### Example 1

**Input:** `s = "010001"`

**Output:** `3`

**Explanation:** The special binary substrings are s[0,1] ("10"), s[2,3] ("01"), and s[3,4] ("10"). Each has 1 significant action ('1') and 1 insignificant action ('0'), satisfying cnt0 = cnt1 * cnt1 (1 = 1 * 1).

### Example 2

**Input:** `s = "10010"`

**Output:** `3`

**Explanation:** The special binary substrings are s[0,1] ("10"), s[2,3] ("01"), and s[3,4] ("10"). Each has 1 significant action ('1') and 1 insignificant action ('0'), satisfying cnt0 = cnt1 * cnt1 (1 = 1 * 1).

## Constraints

- `1 ≤ |s| ≤ 10^5s consists of '0' and '1' only.`

## Solutions

<!-- Scaffold placeholder: the worked derivation and solutions land
     on the solutions branch later. See ../_TEMPLATE.md for the
     expected layout, naming, and ordering conventions. -->
