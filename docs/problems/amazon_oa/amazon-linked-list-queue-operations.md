# [Linked-List Queue with Delete and Deduplication](https://www.fastprep.io/problems/amazon-linked-list-queue-operations)

**Medium** | **NN minutes** | **Linked List, Design, Simulation**

Source note: The source omits whether deletion removes one or all matches, which duplicate occurrence survives, and the callable batch format. The judged core task matches the visible report at about 90%.

Implement a queue whose state is stored in a hand-built singly linked list. The queue starts empty. Process operations from left to right, using the integer at the same index in values when an operation needs an argument.

The supported operations are:

enqueue: append a new node containing values[i] at the tail in O(1) time.dequeue: remove the head in O(1) time and append its value to the result.delete: remove the first node, from the head, whose value equals values[i]. If no node matches, leave the queue unchanged.removeAllDuplicates: retain the first occurrence of every value and remove all later occurrences, preserving the relative order of the retained nodes.Return the values produced by dequeue operations in encounter order. The value paired with dequeue or removeAllDuplicates is ignored.

Use explicit node, head, and tail references for the queue state. Do not use a library queue, deque, or linked-list container to represent it. An auxiliary membership set may be used only while processing removeAllDuplicates.

## Examples

### Example 1

**Input:** `operations = ["enqueue","enqueue","enqueue","enqueue","enqueue","removeAllDuplicates","dequeue","delete","dequeue"]`, `values = [3,1,3,2,1,0,0,1,0]`

**Output:** `[3,2]`

**Explanation:** Deduplication changes [3,1,3,2,1] to [3,1,2]. The first dequeue returns 3, deletion removes the first 1, and the final dequeue returns 2.

### Example 2

**Input:** `operations = ["enqueue","enqueue","enqueue","delete","enqueue","dequeue","dequeue","dequeue"]`, `values = [4,5,6,6,7,0,0,0]`

**Output:** `[4,5,7]`

**Explanation:** Deleting the tail value 6 must repair the tail pointer, so the later enqueue appends 7 after 5.

### Example 3

**Input:** `operations = ["enqueue","enqueue","enqueue","delete","dequeue","dequeue"]`, `values = [8,9,8,8,0,0]`

**Output:** `[9,8]`

**Explanation:** delete 8 removes only the first matching node. The later 8 remains behind 9.

## Constraints

- `1 <= operations.length <= 2000`
- `values.length == operations.length`
- `Every operation is enqueue, dequeue, delete, or removeAllDuplicates.`
- `-10^9 <= values[i] <= 10^9`
- `Every dequeue occurs when the queue is nonempty.`
- `The queue state must use hand-built singly linked nodes with explicit head and tail references.`

## Solutions

<!-- Scaffold placeholder: the worked derivation and solutions land
     on the solutions branch later. See ../_TEMPLATE.md for the
     expected layout, naming, and ordering conventions. -->
