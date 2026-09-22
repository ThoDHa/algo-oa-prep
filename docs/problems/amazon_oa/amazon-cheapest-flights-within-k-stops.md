# [Cheapest Flights Within K Stops](https://www.fastprep.io/problems/amazon-cheapest-flights-within-k-stops)

**Medium** | **NN minutes** | **Graph, Breadth First Search, Shortest Path, Heap**

There are n cities numbered from 0 to n - 1. You are given an array flights where flights[i] = [from_i, to_i, price_i] means there is a directed flight from city from_i to city to_i with cost price_i.You are also given integers src, dst, and k. Return the cheapest price from src to dst with at most k stops. If no such route exists, return -1.

## Examples

### Example 1

**Input:** `n = 4`
**Input:** `flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]]`
**Input:** `src = 0`
**Input:** `dst = 3`
**Input:** `k = 1`

**Output:** `700`

**Explanation:** The route 0 -> 1 -> 3 costs 700 and uses 1 stop. The cheaper route 0 -> 1 -> 2 -> 3 costs 400 but uses 2 stops, which exceeds k.

### Example 2

**Input:** `n = 3`
**Input:** `flights = [[0,1,100],[1,2,100],[0,2,500]]`
**Input:** `src = 0`
**Input:** `dst = 2`
**Input:** `k = 1`

**Output:** `200`

**Explanation:** The route 0 -> 1 -> 2 costs 200 with 1 stop, which is cheaper than the direct flight of 500.

## Constraints

- `1 <= n <= 100.0 <= flights.length <= n * (n - 1).flights[i].length == 3.0 <= from_i, to_i < n.from_i != to_i.1 <= price_i <= 10^4.There are no duplicate flights and no self-flights.0 <= src, dst, k < n.src != dst.`

## Solutions

<!-- Scaffold placeholder: the worked derivation and solutions land
     on the solutions branch later. See ../_TEMPLATE.md for the
     expected layout, naming, and ordering conventions. -->
