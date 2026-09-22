# [Dynamic Kth Largest Queries](https://www.fastprep.io/problems/amazon-dynamic-kth-largest-queries)

**unknown difficulty** | **NN minutes** | **unknown categories**

You are given an initial list of integer values and a stream of operations. The list changes over time as values are inserted.

Each operation is one of the following:

"insert": insert the accompanying value into the list."find": treat the accompanying value as k and return the current k-th largest value in the list.Return the answers to all "find" operations in order.

## Examples

### Example 1

**Input:** `initialValues = [3, 7, 1]`, `operations = ["find", "insert", "insert", "find", "find"]`, `values = [3, 4, 9, 2, 4]`

**Output:** `[1, 7, 3]`

**Explanation:** Initially the sorted values are [1,3,7], so the 3rd largest is 1. After inserting 4 and 9, the values are [1,3,4,7,9]; the 2nd largest is 7 and the 4th largest is 3.

### Example 2

**Input:** `initialValues = [5]`, `operations = ["insert", "find", "insert", "find"]`, `values = [2, 1, 10, 2]`

**Output:** `[5, 5]`

**Explanation:** After inserting 2, the largest value is 5. After inserting 10, the 2nd largest value is still 5.

## Constraints

- `operations.length == values.length`
- `Each operation is either "insert" or "find".`
- `For each "find" operation, 1 <= k <= the current list size.`

## Solutions

<!-- Scaffold placeholder: the worked derivation and solutions land
     on the solutions branch later. See ../_TEMPLATE.md for the
     expected layout, naming, and ordering conventions. -->
