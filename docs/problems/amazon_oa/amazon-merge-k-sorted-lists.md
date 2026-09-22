# [Merge k Sorted Lists](https://www.fastprep.io/problems/amazon-merge-k-sorted-lists)

**Hard** | **NN minutes** | **Linked List, Heap**

You are given an array lists containing k linked-list heads. Every linked list is sorted in ascending order.

Merge all of the linked lists into one ascending linked list and return its head.

## Examples

### Example 1

**Input:** `lists = [[1,4,5],[1,3,4],[2,6]]`

**Output:** `[1,1,2,3,4,4,5,6]`

**Explanation:** The linked lists are:

1 -> 4 -> 5
1 -> 3 -> 4
2 -> 6Merging them produces the sorted linked list 1 -> 1 -> 2 -> 3 -> 4 -> 4 -> 5 -> 6.

### Example 2

**Input:** `lists = []`

**Output:** `[]`

### Example 3

**Input:** `lists = [[]]`

**Output:** `[]`

## Constraints

- `k == lists.length`
- `0 <= k <= 10^4`
- `0 <= lists[i].length <= 500`
- `-10^4 <= lists[i][j] <= 10^4`
- `Each lists[i] is sorted in ascending order.`
- `The sum of all lists[i].length values does not exceed 10^4.`

## Solutions

<!-- Scaffold placeholder: the worked derivation and solutions land
     on the solutions branch later. See ../_TEMPLATE.md for the
     expected layout, naming, and ordering conventions. -->
