# [Buy Servers](https://www.fastprep.io/problems/amazon-purchase-servers)

**Medium** | **NN minutes** | **Greedy, Sorting**

$23

## Examples

### Example 1

**Input:** `power = [4, 4, 6, 7]`
**Input:** `cost = [1, 1, 2, 2]`
**Input:** `target = 7`

**Output:** `2`

**Explanation:** Given efficiency = [4, 4, 6, 7], cost = [1, 1, 2, 2], k = 7. Choosing server indices [0, 1] gives cost 1 + 1 = 2 and efficiency 4 + 4 = 8 >= 7. Choosing [0, 2] gives cost 1 + 2 = 3 and efficiency 4 + 6 = 10. Choosing [1, 2] gives cost 1 + 2 = 3 and efficiency 4 + 6 = 10, and so on. Among all valid selections, indices [0, 1] yield the minimum total cost of 2 while satisfying total efficiency >= k (=7).

## Constraints

- `Each server's cost is either 1 or 2.Each server can be purchased at most once.If no selection of servers achieves a total efficiency greater than or equal to k, the answer is -1.`

## Solutions

<!-- Scaffold placeholder: the worked derivation and solutions land
     on the solutions branch later. See ../_TEMPLATE.md for the
     expected layout, naming, and ordering conventions. -->
