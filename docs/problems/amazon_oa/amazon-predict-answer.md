# [Predict Answer](https://www.fastprep.io/problems/amazon-predict-answer)

**Medium** | **NN minutes** | **Array, Binary Search, Sorting, Stack**

$23

## Examples

### Example 1

**Input:** `stockData = [5, 6, 8, 4, 9, 10, 8, 3, 6, 4]`
**Input:** `queries = [6, 5, 4]`

**Output:** `[5, 4, 8]`

**Explanation:** On day 6, the stock price is 10. Both 9 and 8 are lower prices one day away. Choose 9 (day 5) because it is before day 6.

On day 5, the stock price is 9. 4 is the closest lower price on day 4.

On day 4, the stock price is 4. The only lower price is on day 8.

So, the output is [5, 4, 8].

### Example 2

**Input:** `stockData = [2,1,3]`
**Input:** `queries = [2,1]`

**Output:** `[-1,2]`

**Explanation:** Day 2 has no lower stock price. For day 1, day 2 has a lower price.

## Constraints

- `1 ≤ n ≤ 10^51 ≤ stockData[i] ≤ 10^91 ≤ q ≤ 10^51 ≤ queries[j] ≤ n`

## Solutions

<!-- Scaffold placeholder: the worked derivation and solutions land
     on the solutions branch later. See ../_TEMPLATE.md for the
     expected layout, naming, and ordering conventions. -->
