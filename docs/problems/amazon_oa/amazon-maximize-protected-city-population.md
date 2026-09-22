# [Maximize Protected City Population](https://www.fastprep.io/problems/amazon-maximize-protected-city-population)

**Medium** | **NN minutes** | **Array, Greedy, Dynamic Programming**

$23

## Examples

### Example 1

**Input:** `population = [10, 5, 8, 9, 6]`
**Input:** `unit = "01101"`

**Output:** `27`

**Explanation:** Move the unit from city 2 to city 1, keep the unit in city 3, and move the unit from city 5 to city 4. Cities 1, 3, and 4 are then protected, for a total population of 10 + 8 + 9 = 27.

### Example 2

**Input:** `population = [7, 4]`
**Input:** `unit = "01"`

**Output:** `7`

**Explanation:** Move the only unit left from city 2 to city 1. Protecting city 1 yields the larger total population.

## Constraints

- `population.length = unit.length()unit contains only '0' and '1'Each security unit may move left by at most one city, and may move at most once.`

## Solutions

<!-- Scaffold placeholder: the worked derivation and solutions land
     on the solutions branch later. See ../_TEMPLATE.md for the
     expected layout, naming, and ordering conventions. -->
