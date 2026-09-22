# [Task Scheduler](https://www.fastprep.io/problems/amazon-task-scheduler)

**Medium** | **NN minutes** | **Greedy, Heap**

$23

## Examples

### Example 1

**Input:** `tasks = ["A","A","A","B","B","B"]`
**Input:** `n = 2`

**Output:** `8`

**Explanation:** A possible sequence is: A -> B -> idle -> A -> B -> idle -> A -> B.
      
      After completing task A, you must wait two intervals before doing A again. The same applies to task B. In the 3rd interval, neither A nor B can be done, so you idle. By the 4th interval, you can do A again as 2 intervals have passed.

### Example 2

**Input:** `tasks = ["A","C","A","B","D","B"]`
**Input:** `n = 1`

**Output:** `6`

**Explanation:** A possible sequence is: A -> B -> C -> D -> A -> B.
      
      With a cooling interval of 1, you can repeat a task after just one other task.

### Example 3

**Input:** `tasks = ["A","A","A","B","B","B"]`
**Input:** `n = 3`

**Output:** `10`

**Explanation:** A possible sequence is: A -> B -> idle -> idle -> A -> B -> idle -> idle -> A -> B.
      
      There are only two types of tasks, A and B, which need to be separated by 3 intervals. This leads to idling twice between repetitions of these tasks.

## Constraints

- `1 <= tasks.length <= 10^4`
- `tasks[i] is an uppercase English letter.`
- `0 <= n <= 100`

## Solutions

<!-- Scaffold placeholder: the worked derivation and solutions land
     on the solutions branch later. See ../_TEMPLATE.md for the
     expected layout, naming, and ordering conventions. -->
