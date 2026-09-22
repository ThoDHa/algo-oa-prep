# [Detect Squares](https://leetcode.com/problems/detect-squares/)

**Medium** | **NN minutes** | **Array, Hash Table, Design, Counting**

You are given a stream of points consisting of x-y coordinates on a 2-D plane. Points can be added and queried as follows:

* **Add** - new points can be added to the stream into a data structure. Duplicate points are allowed and should be treated as separate points.
* **Query** - Given a single query point, **count** the number of ways to choose three additional points from the data structure such that the three points and the query point form a **square**. The square must have all sides parallel to the x-axis and y-axis, i.e. no diagonal squares are allowed. Recall that a **square** must have four equal sides.


Implement the `CountSquares` class:
* `CountSquares()` Initializes the object.
* `void add(int[] point)` Adds a new point `point = [x, y]`.
* `int count(int[] point)` Counts the number of ways to form valid **squares** with point `point = [x, y]` as described above.

## Examples

### Example 1

**Input:** `["CountSquares", "add", [[1, 1]], "add", [[2, 2]], "add", [[1, 2]], "count", [[2, 1]], "count", [[3, 3]], "add", [[2, 2]], "count", [[2, 1]]]`

**Output:** `[null, null, null, null, 1, 0, null, 2]`

**Explanation:** CountSquares countSquares = new CountSquares();
countSquares.add([1, 1]);
countSquares.add([2, 2]);
countSquares.add([1, 2]);

countSquares.count([2, 1]);   // return 1.
countSquares.count([3, 3]);   // return 0.
countSquares.add([2, 2]);     // Duplicate points are allowed.
countSquares.count([2, 1]);   // return 2.

## Constraints

- `point.length == 2`
- `0 <= x, y <= 1000`

## Solutions

<!-- Scaffold placeholder: the worked derivation and solutions land
     on the solutions branch later. See _TEMPLATE.md for the
     expected layout, naming, and ordering conventions. -->
