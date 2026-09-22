# [Find Minimum Time](https://www.fastprep.io/problems/amazon-find-minimum-time)

**Medium** | **NN minutes** | **Array, Sorting, Greedy**

$23

## Examples

### Example 1

**Input:** `n = 3`
**Input:** `k = 3`
**Input:** `position = [-20, 5, 10]`

**Output:** `40`

**Explanation:** It is optimal to choose the following way:
 
        Initially, the snake is at coordinate 0. As the snake needs to eat all three apples,It will first go right for 5 seconds and eat the apple at position 5.It moves in the same direction for another 5 seconds to reach coordinate 10 and eat the apple there.Now it moves left for 30 seconds to reach the coordinate -20 and eat the apple there.
      Time taken will be 5 + 5 + 30 = 40 seconds.
      It can be shown that it is not possible for the snake to eat all the apples in less than 40 seconds.
      Hence, the answer is 40.

## Constraints

- `1 ≤ n ≤ 10^51 <= k <= n| position[i]| <= 10^8 OR −108 ≤ position[i] ≤ 108The array position consists of distinct integers.`

## Solutions

<!-- Scaffold placeholder: the worked derivation and solutions land
     on the solutions branch later. See ../_TEMPLATE.md for the
     expected layout, naming, and ordering conventions. -->
