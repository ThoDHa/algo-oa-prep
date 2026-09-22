# [VM Rental Revenue](https://www.fastprep.io/problems/amazon-vm-rental-revenue)

**Medium** | **NN minutes** | **Heap, Greedy**

There are multiple VM types, each with an initial stock count. A sequence of customers rent one VM at a time.

Each customer always rents from the VM type with the highest remaining stock. The revenue from a rental equals the sum of the current highest stock and the current lowest non-zero stock across all VM types. After the rental, the chosen VM type loses one unit of stock.

Return the total revenue after serving customerRequests customers.

## Examples

### Example 1

**Input:** `vmStock = [1, 2, 4]`, `customerRequests = 4`

**Output:** `15`

**Explanation:** The rental costs are 5, 4, 3, and 3, for a total revenue of 15.

## Constraints

- `Stocks are non-negative integers.`
- `The number of requests may be as large as the total available stock.`

## Solutions

<!-- Scaffold placeholder: the worked derivation and solutions land
     on the solutions branch later. See ../_TEMPLATE.md for the
     expected layout, naming, and ordering conventions. -->
