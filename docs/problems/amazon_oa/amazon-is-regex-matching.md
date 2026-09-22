# [Is Regex Matching](https://www.fastprep.io/problems/amazon-is-regex-matching)

**Hard** | **NN minutes** | **Dynamic Programming, String, Parsing**

$23

## Examples

### Example 1

**Input:** `regex = "ab(e.r)*e"`
**Input:** `arr = ["abbeere", "abefretre"]`

**Output:** `["NO", "YES"]`

**Explanation:** Here, n = 9, regex = "ab(e.r)*e", k = 2, arr = ["abbeere", "abefretre"]
     
        arr[0] = "abbeere" doesn't match the regex "ab(e.r)*e".arr[1] = "abefretre" matches the regex "ab(e.r)*e", if we replace '*' with 2 occurrences of "e.r", i.e. it becomes "abe.re.re". Now, replace both '.' with 'f' and 't' respectively.

Hence, the answer is ["NO", "YES"].

### Example 2

**Input:** `regex = "..()*e*"`
**Input:** `arr = ["code", "abeee", "cd"]`

**Output:** `["NO", "YES", "YES"]`

**Explanation:** Here, n = 8, regex = "..()*ex", k = 3, arr = ["code", "abeeee", "cd"]
    
        arr[0] = "code" doesn't matches the regex "..()*ex".arr[1] = "abeeee" matches the regex "..()*ex", if we replace first '*' with 0 occurrences of "" (an empty string) and second '*' with 3 occurrences of "e", i.e. it becomes "..eee". Now, replace both '.' with 'a' and 'b' respectively.arr[2] = "cd" matches the regex "..()*ex", if we replace first '*' with 0 occurrences of "" and second '*' with 0 occurrences of "e", i.e. it becomes "..". Now, replace both '.' with 'c' and 'd' respectively.
  
Hence, the answer is ["NO", "YES", "YES"].

## Constraints

- `N/A`

## Solutions

<!-- Scaffold placeholder: the worked derivation and solutions land
     on the solutions branch later. See ../_TEMPLATE.md for the
     expected layout, naming, and ordering conventions. -->
