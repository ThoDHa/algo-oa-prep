# [Get Min Errors](https://www.fastprep.io/problems/amazon-get-min-errors)

**Hard** | **NN minutes** | **Dynamic Programming, String, Greedy**

$23

## Examples

### Example 1

**Input:** `errorString = "101!1"`
**Input:** `x = 2`
**Input:** `y = 3`

**Output:** `9`

**Explanation:** If the '!' at index 3 is replaced with '0', the string is "10101". The number of times the subsequence 01 occurs is 3 at indices (1, 2), (1, 4), and (3, 4). The number of times the subsequence 10 occurs is also 3, indices (0, 1), (0, 3) and (2, 3). The number of errors is 3 * x + 3 * y = 6 + 9 = 15.
   
If the '!' is replaced with '1', the string is "10111". The subsequence 01 occurs 3 times and 10 occurs 1 time. The number of errors is 3 * x + y = 9.
      
The minimum number of errors is min(9, 15) modulo (109 + 7) = 9.

### Example 2

**Input:** `errorString = "01!0"`
**Input:** `x = 2`
**Input:** `y = 2`

**Output:** `6`

**Explanation:** The better string is 0100 with one substring 01 at index (0,1) and two subsequence of 10 at indices (1,2) and (2,3) making total errors generate = 2 * 1 + 2 * 2 = 6.

࣪𓏲ּ ᥫ᭡ ₊ ⊹ Credit to 𓇼 Suat 𓇼 ˑ🌷 ִֶ 𓂃

### Example 3

**Input:** `errorString = "!!!!!!!"`
**Input:** `x = 23`
**Input:** `y = 27`

**Output:** `0`

**Explanation:** There is a tie for the best string generated, 00000 or 11111, with zero substrings 01 or 10.

## Constraints

- `1<= len (errorString)<=1050 <= x, y <= 105s consists only of characters '0', '1', and 'l'`

## Solutions

<!-- Scaffold placeholder: the worked derivation and solutions land
     on the solutions branch later. See ../_TEMPLATE.md for the
     expected layout, naming, and ordering conventions. -->
