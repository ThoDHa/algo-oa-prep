# [All About Medians](https://www.fastprep.io/problems/amazon-medians)

**Easy** | **NN minutes** | **Array, Sorting**

$23

## Examples

### Example 1

**Input:** `nums = [1, 2, 3]`
**Input:** `k = 2`

**Output:** `[2, 1]`

**Explanation:** The subsequences of length k = 2 and their medians (using the lower-middle element of the sorted pair) are:[1, 2] → median 1[1, 3] → median 1[2, 3] → median 2The maximum median is 2 and the minimum median is 1.

### Example 2

**Input:** `nums = [56, 21]`
**Input:** `k = 1`

**Output:** `[56, 21]`

**Explanation:** The subsequences of length k = 1 and their medians are:[56] → median 56[21] → median 21The maximum median is 56 and the minimum median is 21.

### Example 3

**Input:** `nums = [16, 21, 9, 2, 78]`
**Input:** `k = 5`

**Output:** `[16, 16]`

**Explanation:** There is only one subsequence of length k = 5:[16, 21, 9, 2, 78] → sorted [2, 9, 16, 21, 78], median at index floor((5-1)/2) = 2 is 16Since there is only one subsequence, both the maximum and minimum median are 16.

## Constraints

- `1 ≤ n ≤ 10^50 ≤ nums[i] ≤ 10^91 ≤ k ≤ n`

## Solutions

<!-- Scaffold placeholder: the worked derivation and solutions land
     on the solutions branch later. See ../_TEMPLATE.md for the
     expected layout, naming, and ordering conventions. -->
