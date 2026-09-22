# [Ways to Group Parcels](https://www.fastprep.io/problems/amazon-find-number-of-ways-to-group-parcels)

**Medium** | **NN minutes** | **Hash Table, Math, Combinatorics**

$24

## Examples

### Example 1

**Input:** `weight = [4, 5, 5, 4, 4, 5, 2, 3]`
**Input:** `wt = 1`

**Output:** `6`

**Explanation:** Pairs will contain either 4 and 5 or 2 and 3 with an absolute difference of 1.

All possible ways of grouping the parcels into pairs are, {(1, 2), (4, 3), (5, 6), (7, 8)}, {(1, 3), (4, 2), (5, 6), (7, 8)}, {(1, 6), (4, 3), (5, 2), (7, 8)}, {(1, 2), (4, 6), (5, 3), (7, 8)}, {(1, 3), (4, 6), (5, 2), (7, 8)} and {(1, 6), (4, 2), (5, 3), (7, 8)}. In all these groups, the absolute difference of the weights of each pair of parcels is equal to the given extra weight wt = 1. For example, consider the group {(1, 6), (4, 2), (5, 3), (7, 8)}.
 
        |weight[1] - weight[6]| = |4 - 5| = 1|weight[4] - weight[2]| = |4 - 5| = 1|weight[3] - weight[5]| = |5 - 4| = 1|weight[7] - weight[8]| = |2 - 3| = 1

## Constraints

- `Unknown for now 🙉`

## Solutions

<!-- Scaffold placeholder: the worked derivation and solutions land
     on the solutions branch later. See ../_TEMPLATE.md for the
     expected layout, naming, and ordering conventions. -->
