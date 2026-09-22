# [Find Min Time Required](https://www.fastprep.io/problems/amazon-find-minimum-time-required)

**Medium** | **NN minutes** | **String, Greedy, Hash Table**

$23

## Examples

### Example 1

**Input:** `requests = "abacadaeafag"`
**Input:** `minGap = 2`

**Output:** `16`

**Explanation:** One optimal strategy is "ab_ad_afgae_ac_a".

### Example 2

**Input:** `requests = "aaabbb"`
**Input:** `minGap = 0`

**Output:** `6`

**Explanation:** Since the minGap is 0, the requests can be processed in any order without any gaps.

### Example 3

**Input:** `requests = "aaabbb"`
**Input:** `minGap = 2`

**Output:** `8`

**Explanation:** The requests can be sent in order "ab_ab_ab" wher _ represents that no request was sent. Here, the min time gap between two requests from the same region is minGap = 2. The total time taken is 8 units :)

## Constraints

- `🍓`

## Solutions

<!-- Scaffold placeholder: the worked derivation and solutions land
     on the solutions branch later. See ../_TEMPLATE.md for the
     expected layout, naming, and ordering conventions. -->
