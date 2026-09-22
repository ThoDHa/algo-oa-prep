# [Minimum Cost to Convert Products to Variant A](https://www.fastprep.io/problems/amazon-minimum-cost-to-convert-products-to-variant-a)

**Medium** | **NN minutes** | **Array, Sliding Window, Greedy**

An inventory array product contains only 0 and 1, where 0 represents variant A and 1 represents variant B.

In one operation, choose a subarray of length k. The cost of that operation is the sum of the values inside the chosen subarray. Then choose one index inside that subarray whose value is 1 and change it to 0.

Return the minimum total cost needed to convert every product to variant A.

Function Description Complete the function minCostToConvertAllToVariantA in the editor below.

minCostToConvertAllToVariantA has the following parameters:

int[] product: the product variantsint k: the fixed operation window lengthReturns int: the minimum total cost.

## Examples

### Example 1

**Input:** `product = [1, 1, 1]`, `k = 2`

**Output:** `4`

**Explanation:** Use window [0, 1] twice, then window [1, 2] once. The costs are 2 + 1 + 1 = 4.

### Example 2

**Input:** `product = [1, 0, 1]`, `k = 2`

**Output:** `2`

**Explanation:** Choose the left window once to clear the first 1, and the right window once to clear the last 1.

## Constraints

- `product[i] is either 0 or 1`
- `1 <= k <= product.length`
- `Each operation must change exactly one 1 inside the chosen window to 0.`

## Solutions

<!-- Scaffold placeholder: the worked derivation and solutions land
     on the solutions branch later. See ../_TEMPLATE.md for the
     expected layout, naming, and ordering conventions. -->
