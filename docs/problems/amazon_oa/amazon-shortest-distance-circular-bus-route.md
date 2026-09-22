# [Shortest Distance on a Circular Bus Route](https://www.fastprep.io/problems/amazon-shortest-distance-circular-bus-route)

**Easy** | **NN minutes** | **Array, Prefix Sum**

For this exercise, assume a bus route has n stops arranged in a circle. The array distance contains the distance from stop i to stop (i + 1) mod n.

Given two distinct stops, start and destination, return the shorter travel distance between them. A bus may travel clockwise or counterclockwise around the circle.

## Examples

### Example 1

**Input:** `distance = [1,2,3,4]`, `start = 0`, `destination = 2`

**Output:** `3`

**Explanation:** Clockwise travel from stop 0 to stop 2 costs 1 + 2 = 3. The other direction costs 4 + 3 = 7, so the answer is 3.

### Example 2

**Input:** `distance = [7,10,1,12]`, `start = 1`, `destination = 3`

**Output:** `11`

**Explanation:** Travel through stops 1 -> 2 -> 3 costs 10 + 1 = 11. The opposite direction costs 12 + 7 = 19.

## Constraints

- `2 <= distance.length <= 100000`
- `1 <= distance[i] <= 10000`
- `0 <= start, destination < distance.length`
- `start != destination`

## Solutions

<!-- Scaffold placeholder: the worked derivation and solutions land
     on the solutions branch later. See ../_TEMPLATE.md for the
     expected layout, naming, and ordering conventions. -->
