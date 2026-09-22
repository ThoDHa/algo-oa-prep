# [Smallest Number With a Given Digit Sum](https://www.fastprep.io/problems/amazon-smallest-number-with-digit-sum)

**Medium** | **NN minutes** | **Greedy, Math, String**

Given integers digitSum and numberOfDigits, construct the smallest non-negative decimal number that:

has exactly numberOfDigits digits, andhas digits whose sum is exactly digitSum.Return the number as a string. The first digit cannot be zero unless numberOfDigits is 1. The input is guaranteed to admit at least one valid number.

## Examples

### Example 1

**Input:** `digitSum = 20`, `numberOfDigits = 3`

**Output:** `"299"`

**Explanation:** The smallest three-digit number with digit sum 20 is 299. Any smaller hundreds digit would leave more than 18 for the final two digits.

### Example 2

**Input:** `digitSum = 1`, `numberOfDigits = 4`

**Output:** `"1000"`

**Explanation:** The leading digit must be nonzero, so 1000 is the smallest four-digit number with digit sum 1.

## Constraints

- `1 <= numberOfDigits.`
- `0 <= digitSum <= 9 * numberOfDigits.`
- `If numberOfDigits is greater than 1, then digitSum is positive.`
- `The returned string has exactly numberOfDigits characters and no leading zero.`

## Solutions

<!-- Scaffold placeholder: the worked derivation and solutions land
     on the solutions branch later. See ../_TEMPLATE.md for the
     expected layout, naming, and ordering conventions. -->
