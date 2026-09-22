# [Course Schedule II](https://www.fastprep.io/problems/amazon-course-schedule-ii)

**Medium** | **NN minutes** | **Graph, Heap, Breadth First Search, Topological Sort**

There are numCourses courses labeled from 0 to numCourses - 1. Each pair [course, prerequisite] means the prerequisite must be completed before the course.

Return the lexicographically smallest course ordering that satisfies every prerequisite. If no valid ordering exists, return an empty array.

## Examples

### Example 1

**Input:** `numCourses = 2`, `prerequisites = [[1,0]]`

**Output:** `[0,1]`

**Explanation:** Course 0 must appear before course 1.

### Example 2

**Input:** `numCourses = 4`, `prerequisites = [[1,0],[2,0],[3,1],[3,2]]`

**Output:** `[0,1,2,3]`

**Explanation:** After course 0, courses 1 and 2 are both available, so lexicographic order chooses 1.

### Example 3

**Input:** `numCourses = 2`, `prerequisites = [[1,0],[0,1]]`

**Output:** `[]`

**Explanation:** The two courses form a cycle, so no complete ordering exists.

## Constraints

- `1 <= numCourses <= 2000.`
- `0 <= prerequisites.length <= 5000.`
- `prerequisites[i].length == 2.`
- `0 <= course, prerequisite < numCourses.`
- `Every prerequisite pair is unique, and a course is never its own prerequisite.`

## Solutions

<!-- Scaffold placeholder: the worked derivation and solutions land
     on the solutions branch later. See ../_TEMPLATE.md for the
     expected layout, naming, and ordering conventions. -->
