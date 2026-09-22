# [Reorder List](https://leetcode.com/problems/reorder-list/)

**Medium** | **NN minutes** | **Linked List, Two Pointers, Stack, Recursion**

You are given the head of a singly linked-list.

The positions of a linked list of `length = 7` for example, can intially be represented as:

`[0, 1, 2, 3, 4, 5, 6]`

Reorder the nodes of the linked list to be in the following order:

`[0, 6, 1, 5, 2, 4, 3]`

In the general case, label the nodes by their original zero-based positions from `0` to `n - 1`. After reordering, those original positions appear in this order:

`[0, n-1, 1, n-2, 2, n-3, ...]`

These numbers represent node positions, not the values stored in the nodes.

You may not modify the values in the list's nodes, but instead you must reorder the nodes themselves.

## Examples

### Example 1

**Input:** `head = [2,4,6,8]`

**Output:** `[2,8,4,6]`

### Example 2

**Input:** `head = [2,4,6,8,10]`

**Output:** `[2,10,4,8,6]`

## Constraints

- `1 <= Length of the list <= 1000`.
- `1 <= Node.val <= 1000`

## Solutions

<!-- Scaffold placeholder: the worked derivation and solutions land
     on the solutions branch later. See _TEMPLATE.md for the
     expected layout, naming, and ordering conventions. -->
