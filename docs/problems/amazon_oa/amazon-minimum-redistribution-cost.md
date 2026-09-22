# [Minimum Redistribution Cost](https://www.fastprep.io/problems/amazon-minimum-redistribution-cost)

**Medium** | **NN minutes** | **Array, Prefix Sum, Greedy**

There are n warehouses arranged in a circle. Warehouse i initially stores products[i] items.You may redistribute items around the circle, but all moved items must travel in one fixed direction: either clockwise or counter-clockwise. Moving one item across one edge costs 1.Return the minimum total cost needed to make every warehouse contain the same number of products. You may choose the better of the two directions.Function Description Complete getMinimumRedistributionCost.int products[n]: product counts around the circleReturns long: the minimum redistribution cost.

## Examples

### Example 1

**Input:** `products = [1,11,1,1,1]`

**Output:** `20`

**Explanation:** The average is 3. The extra 8 products at the second warehouse must fill deficits of 2 at four other warehouses. In either direction, the total edge-crossing cost is 20.

### Example 2

**Input:** `products = [0,6,0]`

**Output:** `6`

**Explanation:** The average is 2. Four items move out of the middle warehouse: two cross one edge and two cross two edges.

## Constraints

- `1 <= products.length <= 10^50 <= products[i] <= 10^9The total number of products is divisible by products.length.`

## Solutions

<!-- Scaffold placeholder: the worked derivation and solutions land
     on the solutions branch later. See ../_TEMPLATE.md for the
     expected layout, naming, and ordering conventions. -->
