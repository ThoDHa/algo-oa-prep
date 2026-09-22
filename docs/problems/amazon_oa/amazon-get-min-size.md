# [Get Min Size](https://www.fastprep.io/problems/amazon-get-min-size)

**Medium** | **NN minutes** | **Binary Search, Greedy, Sorting**

$23

## Examples

### Example 1

**Input:** `gameSize = [9, 2, 4, 6]`
**Input:** `k = 3`

**Output:** `9`

**Explanation:** We note that we will need pen drives of the size of at least 9 units, to store the first game.

This also turns out to be the minimum size of pen drives that should be ordered to give the games to these children.

We can use the first pen drive to store the game of size 9, the 2nd one to store the second and third games, and the 3rd pen drive to store the fourth game.

Hence, the minimum capacity of pen drives required is 9 units.

## Constraints

- `1 ≤ k ≤ n ≤ 2 * 10^5`
- `1 ≤ gameSize[i] ≤ 10^9`
- `n ≤ 2*k`

## Solutions

<!-- Scaffold placeholder: the worked derivation and solutions land
     on the solutions branch later. See ../_TEMPLATE.md for the
     expected layout, naming, and ordering conventions. -->
