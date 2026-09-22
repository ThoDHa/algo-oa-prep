# [Get Smaller Items](https://www.fastprep.io/problems/amazon-get-smaller-items)

**Hard** | **NN minutes** | **Prefix Sum, Binary Search, Sorting**

$23

## Examples

### Example 1

**Input:** `items = [1, 2, 5, 4, 5]`
**Input:** `start = [0, 0, 1]`
**Input:** `end = [1, 2, 2]`
**Input:** `query = [2, 4]`

**Output:** `[2, 5]`

**Explanation:** Over the 3 orders, the picked items are [1, 2], [1, 2, 5], and [2, 5].
      
      For the first query, 2 picked items have values less than 2.
      
      5 picked items have values less than 4.
      
      Hence the answer is [2, 5].

### Example 2

**Input:** `items = [1, 2, 3, 2, 4, 1]`
**Input:** `start = [2, 0]`
**Input:** `end = [4, 0]`
**Input:** `query = [5, 3]`

**Output:** `[4, 2]`

**Explanation:** In the first move, pick items from index 2 to 4, items = [3, 2, 4]

In the second move, pick the items from index 0, items = [1]

The picked items are [3, 2, 4, 1] -

For the first query, all items have values strictly less than 5.
For the second query, 2 items have values strictly less than 3.

## Constraints

- `1 ≤ n ≤ 10^5`
- `1 ≤ items[i] ≤ 10^9, where 0 ≤ i < n`
- `0 < m ≤ 10^5`
- `0 ≤ start[i] ≤ end[i] < n, where 0 ≤ i < m`
- `1 ≤ q ≤ 10^5`
- `1 ≤ query[i] ≤ 10^9, where 0 ≤ i < q`

## Solutions

<!-- Scaffold placeholder: the worked derivation and solutions land
     on the solutions branch later. See ../_TEMPLATE.md for the
     expected layout, naming, and ordering conventions. -->
