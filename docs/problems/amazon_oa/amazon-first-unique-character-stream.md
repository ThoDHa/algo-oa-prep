# [First Unique Character in a Stream](https://www.fastprep.io/problems/amazon-first-unique-character-stream)

**Medium** | **NN minutes** | **String, Hash Table, Queue**

Characters arrive in the order of the string stream. After each arrival, append the earliest character seen so far whose frequency in the processed prefix is exactly one.

If the current prefix has no unique character, append #. Return the concatenation of all per-arrival answers. Comparisons are case-sensitive.

Sibling variants: same core, different skinThese four problems are sibling variants of the same first-unique pattern. Their story wrappers and query timing differ, while the core rule keeps the earliest value whose frequency is exactly one.

Longest-Waiting Unique TaskDynamic Longest-Waiting Unique Task QueriesFirst User to Log In Exactly OnceFirst Unique Character in a Stream (current)

## Examples

### Example 1

**Input:** `stream = "aabc"`

**Output:** `"a#bb"`

**Explanation:** The first a is unique, then none is unique, and b remains first after c arrives.

### Example 2

**Input:** `stream = "zz"`

**Output:** `"z#"`

**Explanation:** The only character stops being unique after its second occurrence.

### Example 3

**Input:** `stream = "abc"`

**Output:** `"aaa"`

**Explanation:** The earliest a remains unique throughout all three prefixes.

## Constraints

- `1 ≤ stream.length ≤ 100000.`
- `stream contains only ASCII letters and digits.`
- `The sentinel # does not occur in stream.`

## Solutions

<!-- Scaffold placeholder: the worked derivation and solutions land
     on the solutions branch later. See ../_TEMPLATE.md for the
     expected layout, naming, and ordering conventions. -->
