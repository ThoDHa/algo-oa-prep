# [Dropped Requests](https://www.fastprep.io/problems/amazon-dropped-requests)

**Medium** | **NN minutes** | **Sliding Window, Array**

$23

## Examples

### Example 1

**Input:** `requestTime = [1, 1, 1, 1, 2]`

**Output:** `1`

**Explanation:** Request 1 - Not Dropped.Request 1 - Not Dropped.Request 1 - Not Dropped.Request 1 - Dropped. At most 3 requests are allowed in one second.Request 2 - Not Dropped.

### Example 2

**Input:** `requestTime = [1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7]`

**Output:** `2`

**Explanation:** Request 1 - Not Dropped.Request 1 - Not Dropped.Request 1 - Not Dropped.Request 1 - Dropped. At most 3 requsts are allowed in one second.Request 2 - Not Dropped.Request 2 - Not Dropped.Request 2 - Not Dropped.Request 3 - Not Dropped.Request 3 - Not Dropped.Request 3 - Not Dropped.Request 4 - Not Dropped.Request 4 - Not Dropped.Request 4 - Not Dropped.Request 5 - Not Dropped.Request 5 - Not Dropped.Request 5 - Not Dropped.Request 6 - Not Dropped.Request 6 - Not Dropped.Request 6 - Not Dropped.Request 7 - Not Dropped.

The total count of requests in the 10-second period from the first to the seventh second is 21, which exceeds the limit (21 > 20), so 1 request is dropped.Request 7 - Dropped.

### Example 3

**Input:** `requestTime = [1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 7, 11, 11, 11, 11]`

**Output:** `7`

**Explanation:** $24

## Constraints

- `1 ≤ n ≤ 106`
- `1 ≤ requestTime[i] ≤ 109`

## Solutions

<!-- Scaffold placeholder: the worked derivation and solutions land
     on the solutions branch later. See ../_TEMPLATE.md for the
     expected layout, naming, and ordering conventions. -->
