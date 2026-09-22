# [Find Networking Calls](https://www.fastprep.io/problems/amazon-find-network-calls)

**Medium** | **NN minutes** | **Array, Sorting, Prefix Sum**

$23

## Examples

### Example 1

**Input:** `feedback = [4, 6, 5, 2, 1]`
**Input:** `targetCounts = [3]`

**Output:** `[10, 20]`

**Explanation:** Answer Version 1 - 



Therefore, the total API calls made to change the number of reviews for all products to 3 is: 1 + 3 + 2 + 1 + 2 = 9.
  

Hence, return the array [9].

Answer Version 2 (newly found on 03-31-2025) -

The source indicates that the expected output for this test case is expected to be [10, 20].

As we can see, the table is not complete in the source found this time. I will update once find more complete source.




As the screenshots were taken on the platform, our expected output will go with [10, 20].

### Example 2

**Input:** `feedback = [3, 6, 6]`
**Input:** `targetCounts = [5, 6]`

**Output:** `[4, 3]`

**Explanation:** For counts value 5 -

The total number of API calls to be made is 2 + 1 + 1 = 4.

For counts value 6 -

The total number of API calls to be made is 3 + 0 + 0 = 3.

So, we return [4, 3].

## Constraints

- `1 ≤ n ≤ 10^51 ≤ feedback[i] ≤ 10^61 ≤ q ≤ 10^51 ≤ targetCounts[i] ≤ 10^6`

## Solutions

<!-- Scaffold placeholder: the worked derivation and solutions land
     on the solutions branch later. See ../_TEMPLATE.md for the
     expected layout, naming, and ordering conventions. -->
