# [Get Max Programs](https://www.fastprep.io/problems/amazon-get-max-programs)

**Medium** | **NN minutes** | **Array, Binary Search, Greedy**

$23

## Examples

### Example 1

**Input:** `time = [5, 2, 1, 4, 2]`
**Input:** `m = 2`
**Input:** `k = 6`

**Output:** `4`

**Explanation:** $24

### Example 2

**Input:** `time = [4, 2, 3, 4, 1]`
**Input:** `m = 1`
**Input:** `k = 4`

**Output:** `1`

**Explanation:** Since there is only one time slot, of length 4, we can not start from the 1st, 2nd, 3rd, or 4th software program. Only the last software program will be executed. Hence the answer is 1.

### Example 3

**Input:** `time = [1, 2, 3, 1, 1]`
**Input:** `m = 3`
**Input:** `k = 3`

**Output:** `5`

**Explanation:** All the software programs will be executed in the following manner:
 
1st and 2nd software programs in the first time slot.3rd software program in the second time slot.4th and 5th software programs in the third time slot.
    
Hence the answer is 5.

## Constraints

- `1 ≤ n, m ≤ 2*1051 ≤ k ≤ 1091 <= time[i] <= k/li>`

## Solutions

<!-- Scaffold placeholder: the worked derivation and solutions land
     on the solutions branch later. See ../_TEMPLATE.md for the
     expected layout, naming, and ordering conventions. -->
