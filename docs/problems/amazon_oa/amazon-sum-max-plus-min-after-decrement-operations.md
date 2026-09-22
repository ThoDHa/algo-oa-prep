# [Sum Max Plus Min After Decrement Operations](https://www.fastprep.io/problems/amazon-sum-max-plus-min-after-decrement-operations)

**Medium** | **NN minutes** | **Heap, Greedy**

You are given an integer array arr and an integer requests.Repeat the following operation exactly requests times:Find the current maximum value and the current minimum value in arr.Add their sum to the answer.Choose one occurrence of the maximum value and decrease it by 1.Return the final accumulated answer.Function Description Complete the function sumMaxPlusMinAfterOperations in the editor below.sumMaxPlusMinAfterOperations has the following parameters:int[] arr: the initial valuesint requests: the number of operationsReturns long: the accumulated sum

## Examples

### Example 1

**Input:** `arr = [1, 2]`
**Input:** `requests = 2`

**Output:** `5`

**Explanation:** First add 1 + 2 = 3 and decrement the 2 to 1. Then add 1 + 1 = 2. The total is 5.

### Example 2

**Input:** `arr = [3, 3, 3]`
**Input:** `requests = 1`

**Output:** `6`

**Explanation:** The current maximum and minimum are both 3, so the answer increases by 6.

## Constraints

- `1 <= arr.length <= 1051 <= arr[i] <= 1090 <= requests <= 109Each operation decreases one occurrence of the current maximum value by exactly 1.Use a wide enough integer type (e.g., long) for the accumulated total.`

## Solutions

<!-- Scaffold placeholder: the worked derivation and solutions land
     on the solutions branch later. See ../_TEMPLATE.md for the
     expected layout, naming, and ordering conventions. -->
