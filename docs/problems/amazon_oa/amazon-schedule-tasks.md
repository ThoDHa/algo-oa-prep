# [Schedule Tasks](https://www.fastprep.io/problems/amazon-schedule-tasks)

**Medium** | **NN minutes** | **Greedy, Sorting, Two Pointers**

$23

## Examples

### Example 1

**Input:** `limit = 7`
**Input:** `primary = [4, 5, 2, 4]`
**Input:** `secondary = [5, 6, 3, 4]`

**Output:** `2`

**Explanation:** One of the optimal scheduling can be:
      
        Day 1: Schedule the first primary task and the third secondary task. Total time is 4 + 3 = 7.
        Day 2: Schedule the second primary task. Total time is 5.
        Day 3: Schedule the third primary task and first secondary task. Total time is 2 + 5 = 7.
        Day 4: Schedule the fourth primary task. Total time is 4.
      
      There is no other arrangement of secondary tasks for which more than 2 secondary tasks can be scheduled in 4 days.

## Constraints

- `🦦`

## Solutions

<!-- Scaffold placeholder: the worked derivation and solutions land
     on the solutions branch later. See ../_TEMPLATE.md for the
     expected layout, naming, and ordering conventions. -->
