# [Bit at an Index After Repeated Binary Expansion](https://www.fastprep.io/problems/amazon-indexed-bit-after-binary-expansion)

**Medium** | **NN minutes** | **String, Math**

Start with a binary string bits. In one expansion round, replace every character independently:

0 becomes 00.1 becomes 10.After exactly rounds expansions, return the bit at the zero-based position index. The position is guaranteed to exist in the expanded string.

## Examples

### Example 1

**Input:** `bits = "01"`, `rounds = 1`, `index = 2`

**Output:** `1`

**Explanation:** One expansion produces 0010, whose zero-based index 2 contains 1.

### Example 2

**Input:** `bits = "1"`, `rounds = 2`, `index = 3`

**Output:** `0`

**Explanation:** The two expansions are 1 -> 10 -> 1000, and its last bit is 0.

### Example 3

**Input:** `bits = "101"`, `rounds = 0`, `index = 2`

**Output:** `1`

**Explanation:** With zero rounds, query the original string directly.

## Constraints

- `1 <= bits.length <= 10^5`
- `bits contains only 0 and 1.`
- `0 <= rounds <= 30`
- `0 <= index <= 10^9`
- `index < bits.length * 2^rounds.`

## Solutions

<!-- Scaffold placeholder: the worked derivation and solutions land
     on the solutions branch later. See ../_TEMPLATE.md for the
     expected layout, naming, and ordering conventions. -->
