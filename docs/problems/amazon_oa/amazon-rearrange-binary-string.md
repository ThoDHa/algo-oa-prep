# [Rearrange Binary String](https://www.fastprep.io/problems/amazon-rearrange-binary-string)

**Medium** | **NN minutes** | **String, Greedy, Hash Table**

$23

## Examples

### Example 1

**Input:** `binary = "101100"`
**Input:** `arr = ["?110?1", "111???"]`

**Output:** `["YES", "NO"]`

**Explanation:** Consider the binary string binary = "101100" and the array arr = ["?110?1", "111???"].
      
        
        For arr[0] = "?110?1", you can replace the '?' characters to form the string "011001". It is possible to rearrange the binary string into "011001" using the sorting operations:
          
            Choose the subsequence {0, 2}, and sorting it transforms binary to "011100".
            Choose the subsequence {3, 4, 5}, and sorting it transforms binary to "011001".
          
          The answer for this element is "YES".
        
        
        For arr[1] = "111???", no valid replacement of '?' characters allows the binary string to be rearranged to match the resulting string. Therefore, the answer is "NO".
        
      
      Thus, the output for this case would be ["YES", "NO"].

## Constraints

- `🐵🐵`

## Solutions

<!-- Scaffold placeholder: the worked derivation and solutions land
     on the solutions branch later. See ../_TEMPLATE.md for the
     expected layout, naming, and ordering conventions. -->
