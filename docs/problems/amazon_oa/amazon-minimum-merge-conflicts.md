# [Minimum Merge Conflicts](https://www.fastprep.io/problems/amazon-minimum-merge-conflicts)

**Hard** | **NN minutes** | **Dynamic Programming, String**

$23

## Examples

### Example 1

**Input:** `primary = "zc"`
**Input:** `secondary = "d"`

**Output:** `2`

**Explanation:** Valid merges include:zcd with 2 merge conflicts (z being lower priority is placed before higher priority commits c and d).Similarly, zdc with 3 merge conflicts.Similarly, dzc with 2 merge conflicts.The minimum number of merge conflicts possible is 2.

### Example 2

**Input:** `primary = "dae"`
**Input:** `secondary = "add"`

**Output:** `1`

**Explanation:** adadde has 1 merge conflict.

### Example 3

**Input:** `primary = "aaa"`
**Input:** `secondary = "abb"`

**Output:** `0`

**Explanation:** aaaabb has no merge conflicts.Added from a newer source found on June 24, 2026 🦒

## Constraints

- `1 <= |primary|, |secondary| <= 1000primary and secondary consist of lowercase English letters only.`

## Solutions

<!-- Scaffold placeholder: the worked derivation and solutions land
     on the solutions branch later. See ../_TEMPLATE.md for the
     expected layout, naming, and ordering conventions. -->
