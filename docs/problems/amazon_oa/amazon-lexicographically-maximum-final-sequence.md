# [Lexicographically Maximum Final Sequence](https://www.fastprep.io/problems/amazon-lexicographically-maximum-final-sequence)

**unknown difficulty** | **NN minutes** | **unknown categories**

You are given a binary string shipmentData consisting only of '0' and '1'.A final string is built from a chosen ordering of shipmentData as follows:Start with an empty string finalSequence.For each character c in the chosen ordering from left to right, append c to finalSequence, then reverse finalSequence.You may rearrange the characters of shipmentData arbitrarily before applying the operation. Return the rearranged shipmentData string that should be fed into the operation to produce the lexicographically maximum possible finalSequence.Do not return finalSequence itself. The answer must be a rearrangement of the original shipmentData.

## Examples

### Example 1

**Input:** `shipmentData = "0011"`

**Output:** `"0101"`

**Explanation:** The returned rearranged string is "0101". If this string is fed into the operation, the resulting final sequence is "1100", which is lexicographically maximum among all rearrangements.

### Example 2

**Input:** `shipmentData = "10100"`

**Output:** `"00101"`

**Explanation:** The final sequence reads positions 5,3,1,2,4 from the rearranged string. Placing the two '1' characters at positions 5 and 3 produces final sequence "11000".

## Constraints

- `shipmentData.length >= 1shipmentData contains only '0' and '1'.`

## Solutions

<!-- Scaffold placeholder: the worked derivation and solutions land
     on the solutions branch later. See ../_TEMPLATE.md for the
     expected layout, naming, and ordering conventions. -->
