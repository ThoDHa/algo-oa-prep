# [Get Success Value](https://www.fastprep.io/problems/get-success-value)

**Easy** | **NN minutes** | **Sorting, Prefix Sum**

$23

## Examples

### Example 1

**Input:** `num_viewers = [2, 5, 6, 3, 5]`
**Input:** `queries = [2, 3, 5]`

**Output:** `[11, 16, 21]`

**Explanation:** The viewership in 5 regions is num_viewers = [2, 5, 6, 3, 5], and we want to find the success value for 3 queries that are queries = [2, 3, 5].

For the first query, k = 2, the viewership of the top 2 regions is [6, 5]. The success value is 6 + 5 = 11.

For the second query, k = 3, the viewership of the top 3 regions is [6, 5, 5] and 6 + 5 + 5 = 16.

For the third query, k = 5, all the 5 regions are used for the success value and 6 + 5 + 5 + 3 + 2 = 21.

Return [11, 16, 21].

### Example 2

**Input:** `num_viewers = [7, 3, 5, 2]`
**Input:** `queries = [1, 4]`

**Output:** `[7, 17]`

**Explanation:** For the first query, k = 1, only the top region is used for the success value.

For the second query, k = 4, all 4 regions are used.


Return [7, 17].

### Example 3

**Input:** `num_viewers = [7, 5, 6]`
**Input:** `queries = [1, 2, 3]`

**Output:** `[7, 13, 18]`

**Explanation:** For the first query, k = 1, only the top region is used for the success value.

For the second query, k = 2, only the top 2 regions are used.

For the third query, k = 3, all 3 regions are used.


Return [7, 13, 18].

## Constraints

- `1 <= n <= 1051 <= q <= 1051 <= num_viewers[i] <= 1091 <= queries[i] <= nEach success value is at most 1014 and requires a 64-bit integer.`

## Solutions

<!-- Scaffold placeholder: the worked derivation and solutions land
     on the solutions branch later. See ../_TEMPLATE.md for the
     expected layout, naming, and ordering conventions. -->
