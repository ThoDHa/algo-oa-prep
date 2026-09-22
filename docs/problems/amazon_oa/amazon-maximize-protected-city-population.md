# [Maximize Protected City Population](https://www.fastprep.io/problems/amazon-maximize-protected-city-population)

**Medium** | **NN minutes** | **Array, Greedy, Dynamic Programming**

You are given n cities arranged in a line. City i has population population[i] and may contain a security unit described by unit[i], where unit[i] = '1' means a unit is initially stationed in city i.

Each security unit may stay where it is, or if it is not in the first city, it may move exactly one city to the left. Every unit can move at most once.

After all moves are chosen, a city is protected if at least one security unit is stationed there. Return the maximum total population of all protected cities.

## Examples

### Example 1

**Input:** `population = [10, 5, 8, 9, 6]`, `unit = "01101"`

**Output:** `27`

**Explanation:** Move the unit from city 2 to city 1, keep the unit in city 3, and move the unit from city 5 to city 4. Cities 1, 3, and 4 are then protected, for a total population of 10 + 8 + 9 = 27.

### Example 2

**Input:** `population = [7, 4]`, `unit = "01"`

**Output:** `7`

**Explanation:** Move the only unit left from city 2 to city 1. Protecting city 1 yields the larger total population.

## Constraints

- `population.length = unit.length()`
- `unit contains only '0' and '1'`
- `Each security unit may move left by at most one city, and may move at most once.`

## Solutions

<!-- Scaffold placeholder: the worked derivation and solutions land
     on the solutions branch later. See ../_TEMPLATE.md for the
     expected layout, naming, and ordering conventions. -->
