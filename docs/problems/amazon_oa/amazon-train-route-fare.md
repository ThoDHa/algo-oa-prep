# [Fare Between Stops on a Train Route](https://www.fastprep.io/problems/amazon-train-route-fare)

**Easy** | **NN minutes** | **Array, Hash Table, Simulation**

A train route is given as an ordered array of unique stop names. Traveling across one adjacent segment costs one fare unit in either direction.

Implement calculateFare to return the fare between start and stop. Return -1 if either requested stop is absent.

## Examples

### Example 1

**Input:** `route = ["G","U","H","K","I"]`, `start = "G"`, `stop = "I"`

**Output:** `4`

**Explanation:** The endpoints are four adjacent segments apart.

### Example 2

**Input:** `route = ["A","B","C"]`, `start = "C"`, `stop = "A"`

**Output:** `2`

**Explanation:** Travel in the reverse direction costs the same two units.

### Example 3

**Input:** `route = ["A","B"]`, `start = "A"`, `stop = "Z"`

**Output:** `-1`

**Explanation:** Z is not a stop on the route.

## Constraints

- `1 ≤ route.length ≤ 100000.`
- `Every route entry is a non-empty unique printable ASCII string.`
- `start and stop are non-empty printable ASCII strings.`

## Solutions

<!-- Scaffold placeholder: the worked derivation and solutions land
     on the solutions branch later. See ../_TEMPLATE.md for the
     expected layout, naming, and ordering conventions. -->
