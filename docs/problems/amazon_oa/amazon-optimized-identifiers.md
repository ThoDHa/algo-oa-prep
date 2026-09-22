# [Optimize Identifiers](https://www.fastprep.io/problems/amazon-optimized-identifiers)

**Medium** | **NN minutes** | **String, Two Pointers**

$23

## Examples

### Example 1

**Input:** `s = "hchc"`

**Output:** `2`

**Explanation:** The type of the initial string is "h", so the operations analyst can remove the first 2 or last 2 letters and get the string "h" with a type "h", hence the answer is 2.

### Example 2

**Input:** `s = "abbc"`

**Output:** `0`

**Explanation:** The operations analyst can't remove any letters from the string since the type will change, hence the answer is 0.

### Example 3

**Input:** `s = "babdcaac"`

**Output:** `0`

**Explanation:** The type of the initial string s is "bc":
Final String, Number of Operations, Type
babdcaac, 0, bc
bdcaac, 6, bc
d, 7, dd
bdc, 5, bc
babdc, 3, bc


From the above final strings, the only valid final strings (strings with a type equal to the type of the initial string "bc") are "babdcaac", "bdc", and "babdc" with a total of operations performed of 0, 5, and 3 respectively, hence the answer is 5.

## Constraints

- `2 ≤ |s| ≤ 2 * 10^5String s consists of lowercase English letters only.`

## Solutions

<!-- Scaffold placeholder: the worked derivation and solutions land
     on the solutions branch later. See ../_TEMPLATE.md for the
     expected layout, naming, and ordering conventions. -->
