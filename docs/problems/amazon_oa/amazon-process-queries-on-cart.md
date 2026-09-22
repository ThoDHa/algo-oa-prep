# [Process Queries On Cart](https://www.fastprep.io/problems/amazon-process-queries-on-cart)

**Easy** | **NN minutes** | **Linked List, Hash Table, Simulation**

$23

## Examples

### Example 1

**Input:** `items = [1, 2, 1, 2, 1]`
**Input:** `query = [-1, -1, 3, 4, -3]`

**Output:** `[2, 2, 1, 4]`

**Explanation:** Initially, there are n = 5 items in the cart represented as cart = [1,2,1,2,1] and queries = [-1,-1,3,4,-3]
      
        QueryTaskCart
        -1Delete first 1 from cart[2,1,2,1]
        -1Delete first 1 from cart[2,2,1]
        3Append 3 to cart[2,2,1,3]
        4Append 4 to cart[2,2,1,3,4]
        -3Delete first 3 from cart[2,2,1,4]
      Report [2,2,1,4] as the final cart.

### Example 2

**Input:** `items = [5, 1, 2, 2, 4, 6]`
**Input:** `query = [1, -2, -1, -1]`

**Output:** `[5, 2, 4, 6]`

**Explanation:** items = [5, 1, 2, 2, 4, 6]
        queries = [1, -2, -1, -1]
      
        QueryTaskCart
        1Append 1 to cart[5, 1, 2, 2, 4, 6, 1]
        -2Delete first 2 from cart[5, 1, 2, 4, 6, 1]
        -1Delete first 1 from cart[5, 2, 4, 6, 1]
        -1Delete first 1 from cart[5, 2, 4, 6]
      Report [5, 2, 4, 6] as the final cart.

## Constraints

- `1 <= n, q <= 2 * 10^5`
- `1 <= items[i] <= 10^9`
- `-10^9 <= query[i] <= 10^9`
- `It is guaranteed that query[i] != 0`

## Solutions

<!-- Scaffold placeholder: the worked derivation and solutions land
     on the solutions branch later. See ../_TEMPLATE.md for the
     expected layout, naming, and ordering conventions. -->
