# [Find Median from Data Stream](https://www.fastprep.io/problems/amazon-find-median-from-data-stream)

**Hard** | **NN minutes** | **Design, Heap, Sorting**

Process a finite sequence of operations while maintaining every integer added so far. Each row in operations has one of these forms:

["add", value] inserts the integer represented by value.["median"] queries the current median.For an odd number of stored values, the median is the middle value after sorting. For an even number, it is the arithmetic mean of the two middle values. Return a double[] containing the median-query results in encounter order. Add operations produce no output.

## Examples

### Example 1

**Input:** `operations = [["add","5"],["median"],["add","1"],["median"],["add","9"],["median"]]`

**Output:** `[5.0,3.0,5.0]`

**Explanation:** The stored multisets at the three queries are [5], [1,5], and [1,5,9], whose medians are 5, 3, and 5.

### Example 2

**Input:** `operations = [["add","-4"],["add","8"],["median"],["add","8"],["median"],["add","20"],["median"]]`

**Output:** `[2.0,8.0,8.0]`

**Explanation:** The queries observe [-4,8], [-4,8,8], and [-4,8,8,20]. Their medians are 2, 8, and 8.

### Example 3

**Input:** `operations = [["add","1000000000"],["add","999999999"],["median"]]`

**Output:** `[999999999.5]`

**Explanation:** The two middle values are 999999999 and 1000000000, so their arithmetic mean is 999999999.5.

## Constraints

- `1 <= operations.length <= 2000`
- `Every row is either ["add", value] or ["median"].`
- `Each added value is an integer from -1000000000 through 1000000000.`
- `Every median query occurs after at least one add operation.`
- `At least one median query appears.`

## Solutions

<!-- Scaffold placeholder: the worked derivation and solutions land
     on the solutions branch later. See ../_TEMPLATE.md for the
     expected layout, naming, and ordering conventions. -->
