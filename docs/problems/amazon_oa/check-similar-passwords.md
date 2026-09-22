# [Check Similar Passwords](https://www.fastprep.io/problems/check-similar-passwords)

**Medium** | **NN minutes** | **String, Two Pointers**

$23

## Examples

### Example 1

**Input:** `newPasswords = ["baacbab", "accdb", "baacba"]`
**Input:** `oldPasswords = ["abdbc", "ach", "abb"]`

**Output:** `["YES", "NO", "YES"]`

**Explanation:** For the first pair, choose indices 3, 4, and 7 in "baacbab" using 1-based indexing. The selected characters "a", "c", and "b" become "b", "d", and "c", so "abdbc" is a subsequence of the transformed password.For the second pair, no choice of indices can make "ach" a subsequence of "accdb", because no transformed character can become 'h'.For the third pair, "abb" can be matched as a subsequence after choosing an appropriate subset of indices.

### Example 2

**Input:** `newPasswords = ["aaccbbee", "aab"]`
**Input:** `oldPasswords = ["bdbf", "aee"]`

**Output:** `["YES", "NO"]`

**Explanation:** For newPasswords[0] = "aaccbbee" and oldPasswords[0] = "bdbf", choose characters so the transformed new password contains "bdbf" as a subsequence.For newPasswords[1] = "aab" and oldPasswords[1] = "aee", there is no way to obtain two 'e' characters as a subsequence, so the answer is "NO".

## Constraints

- `1 <= n <= 10newPasswords.length == oldPasswords.length == n1 <= oldPasswords[i].length <= newPasswords[i].lengthThe total length of all strings in newPasswords and oldPasswords does not exceed 2 * 105.All passwords consist of lowercase English letters.`

## Solutions

<!-- Scaffold placeholder: the worked derivation and solutions land
     on the solutions branch later. See ../_TEMPLATE.md for the
     expected layout, naming, and ordering conventions. -->
