# [Minimum Moves for Two Knights to Meet](https://www.fastprep.io/problems/amazon-two-knights-minimum-meeting-moves)

**Medium** | **NN minutes** | **Math, Breadth First Search**

Two knights start at coordinates first = [x1, y1] and second = [x2, y2] on an infinite chessboard. They take turns, with the first knight moving first. On a turn, the chosen knight must make one standard knight move: two squares along one axis and one square along the other.Return the minimum total number of moves until the two knights occupy the same coordinate. If they already share a coordinate, return 0.

## Examples

### Example 1

**Input:** `first = [0,0]`
**Input:** `second = [1,2]`

**Output:** `1`

**Explanation:** The first knight can reach the second knight in one move.

### Example 2

**Input:** `first = [0,0]`
**Input:** `second = [1,0]`

**Output:** `3`

**Explanation:** The adjacent displacement is the exceptional three-move case.

### Example 3

**Input:** `first = [7,-4]`
**Input:** `second = [7,-4]`

**Output:** `0`

**Explanation:** The knights already meet.

## Constraints

- `first.length == second.length == 2-10^9 <= first[i], second[i] <= 10^9`

## Solutions

<!-- Scaffold placeholder: the worked derivation and solutions land
     on the solutions branch later. See ../_TEMPLATE.md for the
     expected layout, naming, and ordering conventions. -->
