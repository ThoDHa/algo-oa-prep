# [Product of Array Except Self](https://www.fastprep.io/problems/amazon-product-array-except-self)

**Medium** | **NN minutes** | **Array, Prefix Sum**

Given an integer array nums, return an array answer where answer[i] equals the product of every element of nums except nums[i].

Solve the problem without division in O(n) time. The output array does not count as extra space.

## Examples

### Example 1

**Input:** `nums = [1,2,3,4]`

**Output:** `[24,12,8,6]`

**Explanation:** For index 0, the product is 2 * 3 * 4 = 24; apply the same rule at every index.

### Example 2

**Input:** `nums = [-1,1,0,-3,3]`

**Output:** `[0,0,9,0,0]`

**Explanation:** Only the position containing zero has a nonzero result, equal to (-1) * 1 * (-3) * 3 = 9.

### Example 3

**Input:** `nums = [2,3]`

**Output:** `[3,2]`

**Explanation:** With two values, each output is the other value.

## Constraints

- `2 <= nums.length <= 10^5.`
- `-30 <= nums[i] <= 30.`
- `Every prefix product and suffix product fits in a signed 32-bit integer.`

## Solutions

<!-- Scaffold placeholder: the worked derivation and solutions land
     on the solutions branch later. See ../_TEMPLATE.md for the
     expected layout, naming, and ordering conventions. -->
