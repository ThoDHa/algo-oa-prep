# [Next Smaller Ticket Price](https://www.fastprep.io/problems/amazon-next-smaller-ticket-price)

**Medium** | **NN minutes** | **Array, Stack**

You are given an integer array prices, where prices[i] is the price of ticket i.For each ticket, find the next strictly smaller price to its right. If no later ticket is cheaper, the answer for that ticket is -1.Return an array of the same length as prices containing those answers in index order.

## Examples

### Example 1

**Input:** `prices = [8,4,6,2,3]`

**Output:** `[4,2,2,-1,-1]`

**Explanation:** Ticket 8 is followed by cheaper 4. Ticket 4 is followed by cheaper 2. Ticket 6 is followed by cheaper 2. Tickets 2 and 3 have no later cheaper price.

### Example 2

**Input:** `prices = [5,4,3,2,1]`

**Output:** `[4,3,2,1,-1]`

**Explanation:** Each ticket is immediately followed by a cheaper ticket except the last.

### Example 3

**Input:** `prices = [1,2,3]`

**Output:** `[-1,-1,-1]`

**Explanation:** Every later ticket is more expensive, so every answer is -1.

## Constraints

- `1 <= prices.length <= 10^5.1 <= prices[i] <= 10^9.`

## Solutions

<!-- Scaffold placeholder: the worked derivation and solutions land
     on the solutions branch later. See ../_TEMPLATE.md for the
     expected layout, naming, and ordering conventions. -->
