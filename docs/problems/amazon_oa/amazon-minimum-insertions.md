# [Min Insertions](https://www.fastprep.io/problems/amazon-minimum-insertions)

**Medium** | **NN minutes** | **Dynamic Programming, Array**

$23

## Examples

### Example 1

**Input:** `finalList = [5, 1, 3]`
**Input:** `initialList = [9, 4, 2, 3, 4]`

**Output:** `2`

**Explanation:** We make the following insertions in the initialList:
      
        Operation 1: Insert 5 such that initialList = [5, 9, 4, 2, 3, 4], so current common
        subsequence [5, 3].
        Operation 2: Insert 1 such that initialList = [5, 9, 4, 1, 2, 3, 4], so current common
        subsequence [5, 1, 3].
      
      Now, consider the subsequence formed from the elements at index (0, 3, 5) of the
      initialList, and make up the finalList, hence we require a minimum of 2 operations.

## Constraints

- `🍓🍓`

## Solutions

<!-- Scaffold placeholder: the worked derivation and solutions land
     on the solutions branch later. See ../_TEMPLATE.md for the
     expected layout, naming, and ordering conventions. -->
