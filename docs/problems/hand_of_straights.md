# [Hand of Straights](https://leetcode.com/problems/hand-of-straights/)

**Medium** | **NN minutes** | **Array, Hash Table, Greedy, Sorting**

You are given an integer array `hand` where `hand[i]` is the value written on the `ith` card and an integer `groupSize`.

You want to rearrange the cards into groups so that each group is of size `groupSize`, and card values are consecutively increasing by `1`.

Return `true` if it's possible to rearrange the cards in this way, otherwise, return `false`.

## Examples

### Example 1

**Input:** `hand = [1,2,4,2,3,5,3,4], groupSize = 4`

**Output:** `true`

**Explanation:** The cards can be rearranged as `[1,2,3,4]` and `[2,3,4,5]`.

### Example 2

**Input:** `hand = [1,2,3,3,4,5,6,7], groupSize = 4`

**Output:** `false`

**Explanation:** The closest we can get is `[1,2,3,4]` and `[3,5,6,7]`, but the cards in the second group are not consecutive.

## Constraints

- `1 <= hand.length <= 10000`
- `0 <= hand[i] <= 1000`
- `1 <= groupSize <= hand.length`

## Solutions

<!-- Scaffold placeholder: the worked derivation and solutions land
     on the solutions branch later. See ../_TEMPLATE.md for the
     expected layout, naming, and ordering conventions. -->
