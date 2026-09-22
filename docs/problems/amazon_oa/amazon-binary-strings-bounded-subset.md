# [Largest Binary-String Subset Within Bit Budgets](https://www.fastprep.io/problems/amazon-binary-strings-bounded-subset)

**Medium** | **NN minutes** | **Array, String, Dynamic Programming**

Given an array of binary strings strs and two budgets, maxOnes and maxZeroes, return the maximum number of strings you can select.The selected strings must contain at most maxOnes ones in total and at most maxZeroes zeroes in total. Each array position may be selected at most once, including when two positions contain equal strings.

## Examples

### Example 1

**Input:** `strs = ["100","10","1","11","111"]`
**Input:** `maxOnes = 3`
**Input:** `maxZeroes = 0`

**Output:** `2`

**Explanation:** Select "1" and "11". They use exactly three ones and no zeroes.

### Example 2

**Input:** `strs = ["10","0001","111001","1","0"]`
**Input:** `maxOnes = 3`
**Input:** `maxZeroes = 5`

**Output:** `4`

**Explanation:** The strings "10", "0001", "1", and "0" use three ones and five zeroes.

### Example 3

**Input:** `strs = ["10","0","1"]`
**Input:** `maxOnes = 1`
**Input:** `maxZeroes = 1`

**Output:** `2`

**Explanation:** Selecting "0" and "1" uses both budgets and yields two strings.

## Constraints

- `1 <= strs.length <= 600.1 <= strs[i].length <= 100.Every strs[i] contains only 0 and 1.0 <= maxOnes, maxZeroes <= 100.`

## Solutions

<!-- Scaffold placeholder: the worked derivation and solutions land
     on the solutions branch later. See ../_TEMPLATE.md for the
     expected layout, naming, and ordering conventions. -->
