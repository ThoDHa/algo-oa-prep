# [Max Aggregate Temp Change](https://www.fastprep.io/problems/amazon-get-max-aggregate-temperature-change)

**Easy** | **NN minutes** | **Array, Prefix Sum**

$23

## Examples

### Example 1

**Input:** `tempChange = [6, -2, 5]`

**Output:** `9`

**Explanation:** The aggregate temperature change on each day is evaluated as:



For day 1, there are no preceding days info, but the day itself is included in the calculation. Temperature changes = [6] for the before period.

For succeeding days, there are values [6, -2, 5] and 6 + (-2) + 5 = 9.

Again, the chagne for day 1 is included. The maximum of 6 and 9 is 9.

For day 2, consider [6, -2] -> 6 + (-2) = 4, and [-2, 5] -> (-2) + 5 = 3. The maximum of 3 and 4 is 4.

For day 3,consider [6, -2, 5] -> 6 + (-2) + 5  = 9, and [5]. The maximum of 9 and 5 is 9.

The max aggregate temp change is max (9, 4, 9) = 9.

### Example 2

**Input:** `tempChange = [-1, 2, 3]`

**Output:** `5`

**Explanation:** Explanation hasn't been found yet. If you happen to know about it, feel free to lmk! Manyyy thanks in advance! 💜

## Constraints

- `1 <= n <= 105-109 <= tempChange[i] <= 109 where, 1 <= i <= n`

## Solutions

<!-- Scaffold placeholder: the worked derivation and solutions land
     on the solutions branch later. See ../_TEMPLATE.md for the
     expected layout, naming, and ordering conventions. -->
