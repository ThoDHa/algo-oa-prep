# [Replace Values and Return Sums](https://www.fastprep.io/problems/amazon-replace-values-and-return-sums)

**unknown difficulty** | **NN minutes** | **unknown categories**

You are given an integer array entries and a 2D integer array transactions. Each transaction is a pair [oldValue, newValue].

For each transaction, replace every occurrence of oldValue in entries with newValue. After applying the transaction, record the sum of all values in entries.

Return an array containing the recorded sums after each transaction.

The sums may exceed the range of a 32-bit integer.

## Examples

### Example 1

**Input:** `entries = [1, 2, 1, 3]`, `transactions = [[1, 4], [2, 1], [4, 2]]`

**Output:** `[13, 12, 8]`

**Explanation:** After replacing 1 with 4, the array is [4,2,4,3] with sum 13. After replacing 2 with 1, the sum is 12. After replacing 4 with 2, the sum is 8.

### Example 2

**Input:** `entries = [5, 5]`, `transactions = [[1, 2], [5, 1]]`

**Output:** `[10, 2]`

**Explanation:** The first transaction has no matching value, so the sum stays 10. The second transaction changes both values to 1, so the sum becomes 2.

## Constraints

- `transactions[i].length == 2`
- `The returned sums may require 64-bit integers.`

## Solutions

<!-- Scaffold placeholder: the worked derivation and solutions land
     on the solutions branch later. See ../_TEMPLATE.md for the
     expected layout, naming, and ordering conventions. -->
