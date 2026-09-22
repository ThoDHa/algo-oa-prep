# [Maximum Frequency Stack](https://www.fastprep.io/problems/amazon-maximum-frequency-stack)

**Hard** | **NN minutes** | **Hash Table, Stack, Design**

Design a stack-like data structure that supports push and pop.

push(x) adds x to the structure.pop() removes and returns the value with the highest current frequency. If several values have the same highest frequency, return the one pushed most recently among them.Process the operations in order and return the values produced by the pop operations.

## Examples

### Example 1

**Input:** `operations = ["push","push","push","push","push","push","pop","pop","pop","pop"]`, `values = [5,7,5,7,4,5,0,0,0,0]`

**Output:** `[5,7,5,4]`

**Explanation:** The first pop returns 5 because it has frequency 3. The next two pops break frequency ties by recency, and the final pop returns 4.

### Example 2

**Input:** `operations = ["push","push","pop","pop"]`, `values = [1,2,0,0]`

**Output:** `[2,1]`

**Explanation:** Both values have frequency 1, so the more recently pushed value 2 is removed first.

## Constraints

- `1 <= operations.length <= 2 * 10^4`
- `values.length == operations.length`
- `Each operation is either push or pop.`
- `0 <= values[i] <= 10^9 for a push operation.`
- `Every pop operation is issued when the structure is nonempty.`
- `The value paired with a pop operation is ignored.`

## Solutions

<!-- Scaffold placeholder: the worked derivation and solutions land
     on the solutions branch later. See ../_TEMPLATE.md for the
     expected layout, naming, and ordering conventions. -->
