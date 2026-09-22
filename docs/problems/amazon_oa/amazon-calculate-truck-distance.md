# [Calculate Truck Distance](https://www.fastprep.io/problems/amazon-calculate-truck-distance)

**Medium** | **NN minutes** | **Array, Prefix Sum**

$23

## Examples

### Example 1

**Input:** `position = [3, 6, 10, 15, 20]`
**Input:** `extraGasStations = [[2, 4]]`

**Output:** `8`

**Explanation:** There are n = 5 trucks, and their positions are position = [3, 6, 10, 15, 20]. There is q = 1 query with extra gas stations at extraGasStations = [[2, 4]].
      
      Once extra gas stations are installed at position[2 - 1] = 6 and position[4 - 1] = 15:
      
        0th truck will move towards x = 6.
        1st truck will not move since there is already a gas station installed.
        2nd truck will move towards x = 15. Recall that trucks can move in increasing x-coordinate/position only.
        3rd truck will not move since there is already a gas station installed.
        4th truck will not move since there is already a gas station installed.
      Total distance travelled:(6 - 3) + (6 - 6) + (15 - 10) + (15 - 15) + (20 - 20) = 3 + 0 + 5 + 0 + 0 = 8.

## Constraints

- `:P`

## Solutions

<!-- Scaffold placeholder: the worked derivation and solutions land
     on the solutions branch later. See ../_TEMPLATE.md for the
     expected layout, naming, and ordering conventions. -->
