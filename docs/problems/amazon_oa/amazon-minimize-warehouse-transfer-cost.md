# [Minimize Warehouse Transfer Cost](https://www.fastprep.io/problems/amazon-minimize-warehouse-transfer-cost)

**Hard** | **NN minutes** | **Array, Prefix Sum, Greedy**

$23

## Examples

### Example 1

**Input:** `warehouses = [6, 6, 6, 3, 4]`

**Output:** `7`

**Explanation:** The source compares two possible routes with costs 7 and 8. Since the problem asks for the minimum cost, the example output is 7.
We can optimally start from the first warehouse and collect 1 item, repeat the same for the following 2 warehouses and deliver 2 to the 4th warehouse and 1 to the 5th warehouse. In the end, each warehouse has 5 items and the total cost is 1 + 2 + 3 + 1 = 7. This is just a possible clockwise move, the optimal cost should consider the anti-clockwise direction as well and return the minimum cost.

## Constraints

<!-- Constraints not parseable from FastPrep for amazon-minimize-warehouse-transfer-cost; fill them in. -->

## Solutions

<!-- Scaffold placeholder: the worked derivation and solutions land
     on the solutions branch later. See ../_TEMPLATE.md for the
     expected layout, naming, and ordering conventions. -->
