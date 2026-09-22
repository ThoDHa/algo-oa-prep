# [Max Number of Products You can Pick](https://www.fastprep.io/problems/amazon-maximum-number-of-products-you-can-pick)

**Hard** | **NN minutes** | **Dynamic Programming, Array**

$23

## Examples

### Example 1

**Input:** `products = [2, 9, 4, 7, 5, 3]`

**Output:** `16`

**Explanation:** The optimal subarray to pick from is [2, 9, 4, 7]. You can pick the following number of products:
      
        From the first product: 2
        From the second product: 3 (since it must be strictly more than the previous pick)
        From the third product: 4 (since it must be strictly more than the previous pick)
        From the fourth product: 7 (since it must be strictly more than the previous pick)
      
      The total number of products picked is 2 + 3 + 4 + 7 = 16.

## Constraints

- `TO-DO`

## Solutions

<!-- Scaffold placeholder: the worked derivation and solutions land
     on the solutions branch later. See ../_TEMPLATE.md for the
     expected layout, naming, and ordering conventions. -->
