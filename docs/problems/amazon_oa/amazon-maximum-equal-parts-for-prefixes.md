# [Maximum Equal Parts for Prefixes](https://www.fastprep.io/problems/amazon-maximum-equal-parts-for-prefixes)

**Medium** | **NN minutes** | **String, Array, Hash Table, Math**

A team at Amazon is working to ensure all packages are correctly sorted for delivery. Each package has a label represented by an uppercase English letter. The full list of labels is given as the string packages, where the i^th character is the label of the i^th package.

To optimize the sorting process, the team wants to analyze each prefix of the string packages (from length 1 to n) and determine the maximum number of equal parts it can be divided into. Each part must satisfy the following conditions:

Each part must have the same frequency of every character as every other part in that divisionGiven a string packages, calculate for each prefix t (from length 1 to n), the maximum number of equal parts into which the prefix can be divided, such that each part has the same number of occurrences of each character.

## Examples

### Example 1

**Input:** `packages = "ABAB"`

**Output:** `[1, 1, 1, 2]`

**Explanation:** Given, packages = "ABAB".

In the given example t represents prefix string and length represents the length of the prefix string.

Return [1, 1, 1, 2] as the answer.

## Constraints

- `packages consists only of uppercase English letters ('A' to 'Z').`
- `The answer is computed for every prefix of packages of length 1 to n, where n is the length of packages.`
- `For each prefix, the maximum number of equal parts is at least 1, since a prefix can always be treated as a single undivided part.`

## Solutions

<!-- Scaffold placeholder: the worked derivation and solutions land
     on the solutions branch later. See ../_TEMPLATE.md for the
     expected layout, naming, and ordering conventions. -->
