# [Remove K Digits](https://www.fastprep.io/problems/amazon-remove-k-digits)

**Medium** | **NN minutes** | **Stack, Greedy, String**

You are given a string num that represents a non-negative integer, and an integer k.Remove exactly k digits from num so the remaining digits stay in their original relative order and form the smallest possible integer.Return that integer as a string. Do not keep leading zeros, except for the integer 0 itself.

## Examples

### Example 1

**Input:** `num = "1432219"`
**Input:** `k = 3`

**Output:** `"1219"`

**Explanation:** Removing the digits 4, 3, and 2 from 1432219 leaves 1219, which is the smallest remaining integer.

### Example 2

**Input:** `num = "10200"`
**Input:** `k = 1`

**Output:** `"200"`

**Explanation:** Removing the leading 1 leaves 0200, which becomes 200 after leading zeros are stripped.

### Example 3

**Input:** `num = "10"`
**Input:** `k = 2`

**Output:** `"0"`

**Explanation:** Every digit is removed, so the result is 0.

## Constraints

- `1 <= num.length <= 10^5.1 <= k <= num.length.num consists of digits only.num has no leading zeros except when num is "0".`

## Solutions

<!-- Scaffold placeholder: the worked derivation and solutions land
     on the solutions branch later. See ../_TEMPLATE.md for the
     expected layout, naming, and ordering conventions. -->
