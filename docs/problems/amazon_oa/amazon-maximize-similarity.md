# [Maximize Similarity](https://www.fastprep.io/problems/amazon-maximize-similarity)

**Easy** | **NN minutes** | **Array, Greedy, Math**

$23

## Examples

### Example 1

**Input:** `inv1 = [2, 4, 1]`
**Input:** `inv2 = [1, 2, 3]`

**Output:** `2`

**Explanation:** Apply the operation on indices i = 2 and j = 0, which makes inv1 = [1, 4, 2].
        Next, apply the operation on indices i = 2 and j = 1, which updates inv1 = [1, 3, 3].
      


      Now, there are two indices, i = 0 and i = 2, for which inv1[i] = inv2[i]. Since it's impossible to make the elements at all indices of the two arrays equal, the answer is 2.

## Constraints

- `1 <= n <= 10^51 <= inv1[i], inv2[i] <= 10^4`

## Solutions

<!-- Scaffold placeholder: the worked derivation and solutions land
     on the solutions branch later. See ../_TEMPLATE.md for the
     expected layout, naming, and ordering conventions. -->
