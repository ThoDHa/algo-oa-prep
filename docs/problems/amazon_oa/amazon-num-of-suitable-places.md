# [Number of Suitable Locations](https://www.fastprep.io/problems/amazon-num-of-suitable-places)

**Medium** | **NN minutes** | **Sorting, Binary Search, Prefix Sum**

$23

## Examples

### Example 1

**Input:** `center = [-2, 1, 0]`
**Input:** `d = 8`

**Output:** `3`

**Explanation:** $24

### Example 2

**Input:** `center = [2, 0, 3, -4]`
**Input:** `d = 22`

**Output:** `5`

**Explanation:** The suitable locations are {-1, 0, 1, 2, 3}, giving a count of 5.At x = -1: total distance is 2*|-1-2| + 2*|-1-0| + 2*|-1-3| + 2*|-1-(-4)| = 22 <= d.At x = 0: total distance is 2*|0-2| + 2*|0-0| + 2*|0-3| + 2*|0-(-4)| = 18 <= d.At x = 1: total distance is 2*|1-2| + 2*|1-0| + 2*|1-3| + 2*|1-(-4)| = 18 <= d.At x = 2: total distance is 2*|2-2| + 2*|2-0| + 2*|2-3| + 2*|2-(-4)| = 18 <= d.At x = 3: total distance is 2*|3-2| + 2*|3-0| + 2*|3-3| + 2*|3-(-4)| = 22 <= d.Since there are 5 such points, the answer is 5.

### Example 3

**Input:** `center = [-3, 2, 2]`
**Input:** `d = 8`

**Output:** `0`

**Explanation:** There are no suitable locations. For example, placing a warehouse at x = 2 gives a total distance of 2*|2-(-3)| + 2*|2-2| + 2*|2-2| = 10 > d. No integer point achieves a total distance of at most d = 8, so the answer is 0.

## Constraints

- `1 <= n <= 10^5-10^9 <= center[i] <= 10^90 <= d <= 10^9Only integer locations x with -10^9 <= x <= 10^9 are counted.`

## Solutions

<!-- Scaffold placeholder: the worked derivation and solutions land
     on the solutions branch later. See ../_TEMPLATE.md for the
     expected layout, naming, and ordering conventions. -->
