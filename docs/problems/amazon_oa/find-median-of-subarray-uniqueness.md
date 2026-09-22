# [Find Median Of Subarray Uniqueness](https://www.fastprep.io/problems/find-median-of-subarray-uniqueness)

**Hard** | **NN minutes** | **Binary Search, Sliding Window**

$23

## Examples

### Example 1

**Input:** `arr = [1, 1]`

**Output:** `1`

**Explanation:** The subarrays along with their uniqueness values are:
   
        [1]: uniqueness = 1[1, 1]: uniqueness = 1[1]: uniqueness = 1subarray_uniqueness is [1, 1, 1].

### Example 2

**Input:** `arr = [1, 2, 3]`

**Output:** `1`

**Explanation:** Given n = 3 and arr = [1, 2, 3], the subarrays along with their uniqueness values are:

        [1]: uniqueness = 1[1, 2]: uniqueness = 2[1, 2, 3]: uniqueness = 3[2]: uniqueness = 1[2, 3]: uniqueness = 2[3]: uniqueness = 1subarray_uniqueness is [1, 2, 3, 1, 2, 1], and after sorting it is [1, 1, 1, 2, 2, 3].

### Example 3

**Input:** `arr = [1, 2, 1]`

**Output:** `1`

**Explanation:** The subarrays with their uniqueness values are:

[1]: uniqueness = 1
[1, 2]: uniqueness = 2
[1, 2, 1]: uniqueness = 2
[2]: uniqueness = 1
[2, 1]: uniqueness = 2
[1]: uniqueness = 1

The subarray_uniqueness array is [1, 2, 2, 1, 2, 1]. After sorting, the arr is [1, 1, 1, 2, 2, 2]. The choice is between the two bold values. Return the min of the two, 1.

[1]: uniqueness = 1

## Constraints

- `N/A`

## Solutions

<!-- Scaffold placeholder: the worked derivation and solutions land
     on the solutions branch later. See ../_TEMPLATE.md for the
     expected layout, naming, and ordering conventions. -->
