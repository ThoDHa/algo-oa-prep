# [Maximize Distance to the Closest Occupied Seat](https://www.fastprep.io/problems/amazon-maximize-distance-to-closest-person)

**Easy** | **NN minutes** | **Array, Two Pointers**

You are given an array seats, where seats[i] = 1 means seat i is occupied and seats[i] = 0 means it is empty. At least one seat is empty and at least one seat is occupied.Choose an empty seat that maximizes its distance to the closest occupied seat, and return the zero-based index of that seat. If several seats have the same maximum distance, return the smallest index.

## Examples

### Example 1

**Input:** `seats = [1,0,0,0,1,1]`

**Output:** `2`

**Explanation:** Seat 2 is two positions from the nearest occupied seat. Every other empty seat is only one position away.

### Example 2

**Input:** `seats = [1,0,0,0]`

**Output:** `3`

**Explanation:** The last seat is three positions from the only occupied seat.

### Example 3

**Input:** `seats = [0,1]`

**Output:** `0`

**Explanation:** Seat 0 is the only empty seat.

### Example 4

**Input:** `seats = [1,0,0,1,0,0,1]`

**Output:** `1`

**Explanation:** Seats 1, 2, 4, and 5 all have nearest-person distance one, so the smallest index is returned.

## Constraints

- `2 <= seats.length <= 20000seats[i] is 0 or 1.At least one seat is empty.At least one seat is occupied.If several empty seats have the same best distance, return the smallest index.`

## Solutions

<!-- Scaffold placeholder: the worked derivation and solutions land
     on the solutions branch later. See ../_TEMPLATE.md for the
     expected layout, naming, and ordering conventions. -->
