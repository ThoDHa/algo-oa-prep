# [Get Max Stability](https://www.fastprep.io/problems/amazon-get-max-stability)

**Medium** | **NN minutes** | **Sorting, Greedy**

$23

## Examples

### Example 1

**Input:** `reliability = [1, 2, 2]`
**Input:** `availability = [1, 1, 3]`

**Output:** `6`

**Explanation:** Consider the set of servers where reliability = [1, 2, 2] and availability = [1, 1, 3].
      
      The possible subsets of servers are:
      
        Indices {0}: Stability = 1*1 = 1
        Indices {1}: Stability = 1*2 = 2
        Indices {2}: Stability = 3*2 = 6
        Indices {0, 1}: Stability = min(1, 1) * (1+ 2) = 3
        Indices {0, 2}: Stability = min(1, 3) * (1+ 2) = 3
        Indices {1, 2}: Stability = min(1, 3) * (2+2) = 4
        Indices {0, 1, 2}: Stability = min(1, 1, 3) * (1+2+2) = 5
      
      So the answer is the maximum stability for the set of index {2}, answer = 6 % 1000000007 = 6.

### Example 2

**Input:** `reliability = [75, 104, 72, 72, 8, 125]`
**Input:** `availability = [1, 2, 2, 1, 2, 1]`

**Output:** `5`

**Explanation:** Take servers at positions 1, 2, 4, and 6. This will cost 5 and the sum of efficiency values is 376.

(This new test case was added on 03-31-2025)

## Constraints

- `1 < n ≤ 10^5`
- `1 <= reliability[i], availability[i] <= 10^6`
- `It is guaranteed that lengths of reliability and availability are the same.`

## Solutions

<!-- Scaffold placeholder: the worked derivation and solutions land
     on the solutions branch later. See ../_TEMPLATE.md for the
     expected layout, naming, and ordering conventions. -->
