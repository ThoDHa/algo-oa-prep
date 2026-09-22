# [Maximum Saw Height for At Least M Cut Length](https://www.fastprep.io/problems/amazon-woodcut-saw-height)

**Medium** | **NN minutes** | **Array, Binary Search**

You have vertical wooden poles with integer heights heights. Set a saw to a non-negative integer height h; every pole taller than h contributes height - h units of wood, and shorter poles contribute nothing.

Given requiredWood, return the largest saw height that collects at least that much wood.

## Examples

### Example 1

**Input:** `heights = [20,15,10,17]`, `requiredWood = 7`

**Output:** `15`

**Explanation:** At height 15 the cuts yield 5 + 0 + 0 + 2 = 7. Raising the saw would yield too little.

### Example 2

**Input:** `heights = [4,42,40,26,46]`, `requiredWood = 20`

**Output:** `36`

**Explanation:** Height 36 yields 6 + 4 + 10 = 20 units from the three taller poles.

### Example 3

**Input:** `heights = [5]`, `requiredWood = 5`

**Output:** `0`

**Explanation:** The only way to collect all five units is to place the saw at ground level.

## Constraints

- `1 <= heights.length <= 100000.`
- `1 <= heights[i] <= 10^9.`
- `1 <= requiredWood <= min(2 * 10^9, sum(heights)).`

## Solutions

<!-- Scaffold placeholder: the worked derivation and solutions land
     on the solutions branch later. See ../_TEMPLATE.md for the
     expected layout, naming, and ordering conventions. -->
