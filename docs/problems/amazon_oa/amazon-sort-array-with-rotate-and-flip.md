# [Sort an Array with Rotate and Flip](https://www.fastprep.io/problems/amazon-sort-array-with-rotate-and-flip)

**Medium** | **NN minutes** | **Array, Math, Simulation**

You are given an array values containing distinct integers. You may apply either of these operations:Rotate: Move the first element to the end of the array.Flip: Reverse the entire array.Return the minimum number of operations needed to place values in strictly increasing order. You may use the operations in any sequence. If increasing order cannot be reached, return -1.

## Examples

### Example 1

**Input:** `values = [3,4,1,2]`

**Output:** `2`

**Explanation:** Rotate twice: [3,4,1,2] becomes [1,2,3,4]. No single operation produces increasing order.

### Example 2

**Input:** `values = [3,2,1,4]`

**Output:** `2`

**Explanation:** Flip to obtain [4,1,2,3], then rotate once to obtain [1,2,3,4].

### Example 3

**Input:** `values = [1,3,2,4]`

**Output:** `-1`

**Explanation:** Rotations preserve the circular order, and a flip only reverses that order. Neither orientation can match [1,2,3,4], so sorting is impossible.

## Constraints

- `1 <= values.length <= 200000Every element is a 32-bit signed integer.All elements are distinct.`

## Solutions

<!-- Scaffold placeholder: the worked derivation and solutions land
     on the solutions branch later. See ../_TEMPLATE.md for the
     expected layout, naming, and ordering conventions. -->
