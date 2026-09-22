# [Task Scheduler](https://www.fastprep.io/problems/amazon-task-scheduler)

**Medium** | **NN minutes** | **Greedy, Heap**

Special thanks: ( ˶ˆᗜˆ˵ ) Many Manyy Manyyy thanks to spike!ᯓᡣ𐭩


    AMZ Interval Collection (A group of problems focused on operations involving intervals :) - 
    


    Task Scheduler (Full-Time)
    
    Merge Intervals (Intern, NG)
    
    Find Overlapping Times (Intern)
    
    Get Maximum Sum Find Overlapping Times (Full-Time)
    
    Optimal Interval Difference
    
    You are given an array of CPU tasks, each labeled with a letter from A to Z, and a number n. Each CPU interval can be idle or allow the completion of one task. Tasks can be completed in any order, but there's a constraint: there has to be a gap of at least n intervals between two tasks with the same label.
    


    Return the minimum number of CPU intervals required to complete all tasks.

## Examples

### Example 1

**Input:** `tasks = ["A","A","A","B","B","B"]`, `n = 2`

**Output:** `8`

**Explanation:** A possible sequence is: A -> B -> idle -> A -> B -> idle -> A -> B.
      


      After completing task A, you must wait two intervals before doing A again. The same applies to task B. In the 3rd interval, neither A nor B can be done, so you idle. By the 4th interval, you can do A again as 2 intervals have passed.

### Example 2

**Input:** `tasks = ["A","C","A","B","D","B"]`, `n = 1`

**Output:** `6`

**Explanation:** A possible sequence is: A -> B -> C -> D -> A -> B.
      


      With a cooling interval of 1, you can repeat a task after just one other task.

### Example 3

**Input:** `tasks = ["A","A","A","B","B","B"]`, `n = 3`

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
