# [Select Least Resource Tasks](https://www.fastprep.io/problems/amazon-select-least-resource-tasks)

**unknown difficulty** | **NN minutes** | **unknown categories**

Amazon's Elastic Container Service schedules tasks dynamically. You are given an integer array resourceConsumption, where resourceConsumption[i] is the resource consumption of one task.

Repeat the following process until no tasks remain:

Select the remaining task with the lowest resource consumption. If multiple tasks have the same lowest value, select the one with the smallest current index.Add the selected task's resource consumption to the total.Remove the selected task and its adjacent remaining tasks, if they exist.Return the total resource consumption of all selected tasks.

Complete the function selectLeastResourceTasks, which receives resourceConsumption and returns the total as an int.

## Examples

### Example 1

**Input:** `resourceConsumption = [4, 3, 2, 1]`

**Output:** `4`

**Explanation:** The lowest value is 1, so it is selected and removed with its left neighbor 2. The remaining tasks are [4, 3]. Next, 3 is selected and removed with 4. The total is 1 + 3 = 4.

### Example 2

**Input:** `resourceConsumption = [6, 4, 9, 10, 34, 56, 54]`

**Output:** `68`

**Explanation:** First select 4 and remove it with adjacent values 6 and 9. The remaining tasks are [10, 34, 56, 54]. Next select 10 and remove 10 and 34. Finally select 54 and remove 56 and 54. The total selected consumption is 4 + 10 + 54 = 68.

## Constraints

- `3 <= n <= 2000`
- `1 <= resourceConsumption[i] <= 10^5`

## Solutions

<!-- Scaffold placeholder: the worked derivation and solutions land
     on the solutions branch later. See ../_TEMPLATE.md for the
     expected layout, naming, and ordering conventions. -->
