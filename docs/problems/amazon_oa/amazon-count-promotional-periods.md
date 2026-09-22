# [Count Promotional Periods](https://www.fastprep.io/problems/amazon-count-promotional-periods)

**unknown difficulty** | **NN minutes** | **unknown categories**

Data analysts at Amazon are studying product order patterns. They classify a period of at least three consecutive days as a promotional period when the order counts on the first and last days are both greater than every order count on the days between them.

More formally, for an array orders, a subarray from index i to index j is a promotional period if j - i + 1 >= 3 and min(orders[i], orders[j]) > max(orders[i + 1], orders[i + 2], ..., orders[j - 1]).

Given the order statistics for n consecutive days, return the number of promotional periods.

Function Description Complete the function countPromotionalPeriods.

countPromotionalPeriods has the following parameter:

int orders[n]: the order statistics for each dayReturns long: the number of promotional periods.

## Examples

### Example 1

**Input:** `orders = [3, 2, 8, 6]`

**Output:** `1`

**Explanation:** Using 1-based indexing, the candidate periods of length at least 3 are [1, 3], [1, 4], and [2, 4]. Period [1, 3] is valid because min(3, 8) = 3 and the only middle value is 2. The other two periods are invalid because their middle maximum is 8. Therefore, the answer is 1.

### Example 2

**Input:** `orders = [5, 1, 4, 2, 6]`

**Output:** `3`

**Explanation:** The promotional periods are [5, 1, 4], [4, 2, 6], and [5, 1, 4, 2, 6].

## Constraints

- `3 <= n <= 2 x 10^5`
- `1 <= orders[i] <= 10^9`
- `All integers in orders are distinct.`

## Solutions

<!-- Scaffold placeholder: the worked derivation and solutions land
     on the solutions branch later. See ../_TEMPLATE.md for the
     expected layout, naming, and ordering conventions. -->
