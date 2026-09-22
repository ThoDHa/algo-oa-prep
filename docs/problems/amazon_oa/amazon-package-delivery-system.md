# [Package Delivery System](https://www.fastprep.io/problems/amazon-package-delivery-system)

**Medium** | **NN minutes** | **Greedy, Sorting, Heap**

Each shipment scenario has a list of truck capacities and a list of package weights.

A truck may deliver any package whose weight does not exceed its current capacity. After a successful delivery, that truck's capacity becomes floor(capacity / 2). Determine whether every package in each scenario can be delivered using the available trucks.

Return an int[] where each entry is 1 if the corresponding scenario is feasible and 0 otherwise.

## Examples

### Example 1

**Input:** `truckCapacities = [[7]]`, `packageWeights = [[4, 3]]`

**Output:** `[1]`

**Explanation:** The single truck delivers package 4, its capacity drops to 3, and it can still deliver package 3. The scenario is feasible.

## Constraints

- `The number of scenarios and the lengths of the nested arrays can be large, so the solution should avoid brute-force backtracking over all assignments.`

## Solutions

<!-- Scaffold placeholder: the worked derivation and solutions land
     on the solutions branch later. See ../_TEMPLATE.md for the
     expected layout, naming, and ordering conventions. -->
