# [Linked-List Queue with Delete and Deduplication](https://www.fastprep.io/problems/amazon-linked-list-queue-operations)

**Medium** | **NN minutes** | **Linked List, Design, Simulation**

$23

## Examples

### Example 1

**Input:** `operations = ["enqueue","enqueue","enqueue","enqueue","enqueue","removeAllDuplicates","dequeue","delete","dequeue"]`
**Input:** `values = [3,1,3,2,1,0,0,1,0]`

**Output:** `[3,2]`

**Explanation:** Deduplication changes [3,1,3,2,1] to [3,1,2]. The first dequeue returns 3, deletion removes the first 1, and the final dequeue returns 2.

### Example 2

**Input:** `operations = ["enqueue","enqueue","enqueue","delete","enqueue","dequeue","dequeue","dequeue"]`
**Input:** `values = [4,5,6,6,7,0,0,0]`

**Output:** `[4,5,7]`

**Explanation:** Deleting the tail value 6 must repair the tail pointer, so the later enqueue appends 7 after 5.

### Example 3

**Input:** `operations = ["enqueue","enqueue","enqueue","delete","dequeue","dequeue"]`
**Input:** `values = [8,9,8,8,0,0]`

**Output:** `[9,8]`

**Explanation:** delete 8 removes only the first matching node. The later 8 remains behind 9.

## Constraints

- `1 <= operations.length <= 2000values.length == operations.lengthEvery operation is enqueue, dequeue, delete, or removeAllDuplicates.-10^9 <= values[i] <= 10^9Every dequeue occurs when the queue is nonempty.The queue state must use hand-built singly linked nodes with explicit head and tail references.`

## Solutions

<!-- Scaffold placeholder: the worked derivation and solutions land
     on the solutions branch later. See ../_TEMPLATE.md for the
     expected layout, naming, and ordering conventions. -->
