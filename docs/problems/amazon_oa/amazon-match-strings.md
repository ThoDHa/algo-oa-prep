# [Match Strings](https://www.fastprep.io/problems/amazon-match-strings)

**Easy** | **NN minutes** | **String, Two Pointers**

$23

## Examples

### Example 1

**Input:** `text = ["code", "coder"]`
**Input:** `pat = ["co*d", "co*er"]`

**Output:** `["NO", "YES"]`

**Explanation:** Given n = 2, text = ["code", "coder"], pat = ["co*d", "co*er"],
   
text[0] = "code", pat[0] = "co*d", "NO", the suffixes do not matchtext[1] = "coder", pat[1] = "co*er", "YES", the prefixes and suffixes match
  
Here prefix of a string is defined as any substring that starts at the beginning of the string and suffix of a string is defined as any substring that ends at the end of the string.
   
Return ["NO", "YES"].

### Example 2

**Input:** `text = ["hackerrank", "hackerrnak"]`
**Input:** `pat = ["hac*rank", "hac*rank"]`

**Output:** `["YES", "NO"]`

**Explanation:** The prefixes and suffixes must match. The suffix in text[1] is "rnak".

## Constraints

- `1 ≤ n ≤ 10`
- `1 ≤ |text[i]|, |pat[i]| ≤ 10^5`
- `text[i] contains only lowercase English characters.`
- `pat[i] contains exactly one wildcard character and other lowercase English characters.`

## Solutions

<!-- Scaffold placeholder: the worked derivation and solutions land
     on the solutions branch later. See ../_TEMPLATE.md for the
     expected layout, naming, and ordering conventions. -->
