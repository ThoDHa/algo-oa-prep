# [Feasible Indices After Reduction](https://www.fastprep.io/problems/amazon-feasible-indices-after-reduction)

**unknown difficulty** | **NN minutes** | **unknown categories**

You are given an integer array arr of size n. All elements of arr are distinct.You may perform either of the following operations any number of times:Choose a non-empty prefix of the current array and delete every element in that prefix except the minimum element of the prefix.Choose a non-empty suffix of the current array and delete every element in that suffix except the maximum element of the suffix.After each operation, the remaining elements are concatenated to form the new array.An index i is called feasible if it is possible to reduce the array to the single element [arr[i]]. Return a binary string of length n where the i-th character is '1' if index i is feasible, and '0' otherwise.

## Examples

### Example 1

**Input:** `arr = [1, 3, 2, 5, 4]`

**Output:** `"10011"`

**Explanation:** The feasible values are 1, 5, and 4. They are the prefix minimum at index 0 or suffix maximums at indices 3 and 4.

### Example 2

**Input:** `arr = [4, 1, 3, 2]`

**Output:** `"1111"`

**Explanation:** All four indices are feasible. Values 4 and 1 are prefix minima, while values 3 and 2 are suffix maxima. For example, after reducing prefix [4,1] to 1, value 3 can survive a reduction of suffix [3,2] and then the whole array. The same first step followed by reducing the whole remaining suffix can leave 2.

## Constraints

- `1 <= n <= 10^51 <= arr[i] <= 10^9All values in arr are distinct.`

## Solutions

<!-- Scaffold placeholder: the worked derivation and solutions land
     on the solutions branch later. See ../_TEMPLATE.md for the
     expected layout, naming, and ordering conventions. -->
