# [Maximum Score With Non-Adjacent Values](https://www.fastprep.io/problems/amazon-maximum-score-with-non-adjacent-values)

**unknown difficulty** | **NN minutes** | **unknown categories**

You are given a list of integers nums. You may choose any set of values from the list.If you choose a value x, then you cannot choose x - 1 or x + 1. When you choose x, your score increases by x * frequency(x), where frequency(x) is the number of times x appears in nums.Return the maximum score you can obtain.

## Examples

### Example 1

**Input:** `nums = [3,4,2]`

**Output:** `6`

**Explanation:** Choose values 2 and 4 for score 2 + 4 = 6. Choosing 3 would block both.

### Example 2

**Input:** `nums = [2,2,3,3,3,4]`

**Output:** `9`

**Explanation:** Choosing value 3 gives score 3 * 3 = 9, which is better than choosing 2 and 4 for score 8.

## Constraints

- `nums.length >= 1`

## Solutions

<!-- Scaffold placeholder: the worked derivation and solutions land
     on the solutions branch later. See ../_TEMPLATE.md for the
     expected layout, naming, and ordering conventions. -->
