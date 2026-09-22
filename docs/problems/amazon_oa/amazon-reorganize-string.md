# [Reorganize a String](https://www.fastprep.io/problems/amazon-reorganize-string)

**Medium** | **NN minutes** | **String, Hash Table, Heap, Greedy**

Rearrange a lowercase string so that no two adjacent characters are equal. If no such arrangement exists, return the empty string.

To make the judged result deterministic, construct the answer with this rule: at each position, select the eligible character with the greatest remaining frequency. The previously placed character is not eligible. If several eligible characters have the same frequency, select the lexicographically smallest one.

## Examples

### Example 1

**Input:** `s = "aab"`

**Output:** `"aba"`

**Explanation:** The highest-frequency eligible character is chosen first, producing a valid arrangement.

### Example 2

**Input:** `s = "aaab"`

**Output:** `""`

**Explanation:** Three copies of one character cannot be separated by the single remaining character.

### Example 3

**Input:** `s = "aabbcc"`

**Output:** `"abcabc"`

**Explanation:** Frequency ties are resolved in lexicographic order while the previous character remains temporarily ineligible.

## Constraints

- `1 <= s.length <= 10^5`
- `s contains only lowercase English letters.`

## Solutions

<!-- Scaffold placeholder: the worked derivation and solutions land
     on the solutions branch later. See ../_TEMPLATE.md for the
     expected layout, naming, and ordering conventions. -->
