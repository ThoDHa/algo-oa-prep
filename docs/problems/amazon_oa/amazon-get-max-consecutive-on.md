# [Max Consecutive ON Servers](https://www.fastprep.io/problems/amazon-get-max-consecutive-on)

**Hard** | **NN minutes** | **String, Sliding Window**

$23

## Examples

### Example 1

**Input:** `machine_status = "00010"`
**Input:** `max_flips = 1`

**Output:** `4`

**Explanation:** The optimal approach is to perform one flip on the range of indices [0..2].

After flipping: "11110"

This results in a sequence of 4 consecutive active machines.

### Example 2

**Input:** `machine_status = "1001"`
**Input:** `max_flips = 2`

**Output:** `4`

**Explanation:** You can flip indices [1..2] to obtain "1111".



Only one operation is needed to achieve a maximum of 4 continuous active machines.

There’s no advantage in using the second operation.

### Example 3

**Input:** `machine_status = "11101010110011"`
**Input:** `max_flips = 2`

**Output:** `8`

**Explanation:** Flip indices [7..9]: "11101011000011"

Then flip [8..11]: "11101011111111"

This strategy yields a block of 8 active machines in a row.

## Constraints

- `1 ≤ n ≤ 2 * 10^5`
- `1 ≤ max_flips ≤ 2 * 10^5`
- `machine_status contains only 0s and 1s`

## Solutions

<!-- Scaffold placeholder: the worked derivation and solutions land
     on the solutions branch later. See ../_TEMPLATE.md for the
     expected layout, naming, and ordering conventions. -->
