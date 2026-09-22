# [Merge Sorted Array](https://www.fastprep.io/problems/amazon-merge-sorted-array)

**Easy** | **NN minutes** | **Array, Two Pointers, Sorting**

You are given two integer arrays nums1 and nums2, each sorted in non-decreasing order, and two integers m and n representing the number of valid elements in the arrays.Merge the valid elements of nums1 and all elements of nums2 into nums1 in non-decreasing order.nums1 has length m + n. Its first m elements are valid input values, while its final n positions are placeholders that should be ignored before the merge.nums2 has length n.Modify nums1 in place, then return the merged nums1.

## Examples

### Example 1

**Input:** `nums1 = [1,2,3,0,0,0]`
**Input:** `m = 3`
**Input:** `nums2 = [2,5,6]`
**Input:** `n = 3`

**Output:** `[1,2,2,3,5,6]`

**Explanation:** The valid portions are [1,2,3] and [2,5,6]. Their merged order is [1,2,2,3,5,6].

### Example 2

**Input:** `nums1 = [1]`
**Input:** `m = 1`
**Input:** `nums2 = []`
**Input:** `n = 0`

**Output:** `[1]`

**Explanation:** The second array is empty, so nums1 remains unchanged.

### Example 3

**Input:** `nums1 = [0]`
**Input:** `m = 0`
**Input:** `nums2 = [1]`
**Input:** `n = 1`

**Output:** `[1]`

**Explanation:** nums1 has no valid input elements. Its single position is merge capacity for the value from nums2.

## Constraints

- `nums1.length == m + nnums2.length == n0 <= m, n <= 2001 <= m + n <= 200-10^9 <= nums1[i], nums2[j] <= 10^9The first m elements of nums1 and all elements of nums2 are sorted in non-decreasing order.`

## Solutions

<!-- Scaffold placeholder: the worked derivation and solutions land
     on the solutions branch later. See ../_TEMPLATE.md for the
     expected layout, naming, and ordering conventions. -->
