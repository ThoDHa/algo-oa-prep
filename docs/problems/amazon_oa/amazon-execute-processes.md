# [Execute Processes](https://www.fastprep.io/problems/amazon-execute-processes)

**Medium** | **NN minutes** | **Array, Hash Table, Simulation**

$23

## Examples

### Example 1

**Input:** `execution = [5, 5, 3, 6, 5, 3]`

**Output:** `21`

**Explanation:** processes 1, 2, 5 are cohesive
processes 3, 6 are cohesive
process 4 is cohesive

Excuting Process 1 results in [0, 3, 3, 6, 3, 3] // total_execution = 5
Excuting Process 2 results in [0, 0, 3, 6, 2, 3] // total_execution = 8
Excuting Process 3 results in [0, 0, 0, 6, 2, 2] // total_execution = 11
Excuting Process 4 results in [0, 0, 0, 0, 2, 2] // total_execution = 17
Excuting Process 5 results in [0, 0, 0, 0, 0, 2] // total_execution = 19
Excuting Process 6 results in [0, 0, 0, 0, 0, 0] // total_execution = 21

Hence, total excution time is 21.

## Constraints

- `Unknown for now 🐰`

## Solutions

<!-- Scaffold placeholder: the worked derivation and solutions land
     on the solutions branch later. See ../_TEMPLATE.md for the
     expected layout, naming, and ordering conventions. -->
