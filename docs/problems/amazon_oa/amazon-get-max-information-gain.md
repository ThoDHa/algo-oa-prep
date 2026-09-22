# [Get Max Information Gain](https://www.fastprep.io/problems/amazon-get-max-information-gain)

**Easy** | **NN minutes** | **String, Hash Table, Sorting**

$23

## Examples

### Example 1

**Input:** `dataSet = ["abofh", "ab", "mo"]`
**Input:** `max_common_features = 1`

**Output:** `3`

**Explanation:** It is optimal to choose the strings "abofh" and "mo". Their number of common features is 1 ('o') and the information gain is |5 - 2| = 3.

### Example 2

**Input:** `dataSet = ["a", "bcdef"]`
**Input:** `max_common_features = 1`

**Output:** `4`

**Explanation:** The two strings can be chosen. They do not share any common features and their difference in length is 4.

## Constraints

- `2 ≤ n ≤ 1000`
- `1 ≤ len(dataSet[i]) ≤ 1000`
- `1 ≤ max_common_features ≤ 1000`

## Solutions

<!-- Scaffold placeholder: the worked derivation and solutions land
     on the solutions branch later. See ../_TEMPLATE.md for the
     expected layout, naming, and ordering conventions. -->
