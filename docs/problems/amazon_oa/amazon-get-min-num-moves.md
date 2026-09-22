# [Get Min Num Moves](https://www.fastprep.io/problems/amazon-get-min-num-moves)

**Easy** | **NN minutes** | **Array, Greedy**

$23

## Examples

### Example 1

**Input:** `blocks = [2, 4, 3, 1, 6]`

**Output:** `3`

**Explanation:** The lightest block needs to move left. The heaviest block is already in the correct position.

        In the first move, swap the third and the fourth blocks: blocks = [2, 4, 1, 3, 6].Swap the second and the third blocks: blocks = [2, 1, 4, 3, 6].Swap the first and the second blocks: blocks = [1, 2, 4, 3, 6].

### Example 2

**Input:** `blocks = [4, 11, 9, 10, 12]`

**Output:** `0`

**Explanation:** The blocks are already in their correct positions.

### Example 3

**Input:** `blocks = [3, 2, 1]`

**Output:** `3`

**Explanation:** Let the blocks be in the order:
blocks = [3, 2, 1]


In the first move, we swap the first and the second blocks. After swapping, the order becomes:
blocks = [2, 3, 1]



In the second move, we swap the second and the third blocks. After swapping, the order becomes:
blocks = [2, 1, 3]



In the third move, we swap the first and second blocks. After swapping, the order becomes:
blocks = [1, 2, 3]


Now, the array satisfies the condition after 3 moves.

## Constraints

- `2 ≤ n ≤ 1051 ≤ blocks[i] ≤ 109 for all 1 ≤ i ≤ nblocks consists of distinct integers.`

## Solutions

<!-- Scaffold placeholder: the worked derivation and solutions land
     on the solutions branch later. See ../_TEMPLATE.md for the
     expected layout, naming, and ordering conventions. -->
