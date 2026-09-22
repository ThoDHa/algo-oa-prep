# [Max Transfer Rate](https://www.fastprep.io/problems/amazon-max-transfer-rate)

**Easy** | **NN minutes** | **Greedy, Sorting, Math**

$23

## Examples

### Example 1

**Input:** `throughput = [4, 2, 5]`
**Input:** `pipelineCount = 4`

**Output:** `36`

**Explanation:** The data pipelines can select their connection among the following 9 possible server pairs:

[1, 1], [1, 2], [1, 3], [2, 2], [2, 3], [3, 1], [3, 2], [3, 3]
(Assuming 1-based indexing of throughput array).

However, each data pipeline must select a unique pair of servers.

To achieve the maximum total transferRate, the data pipelines can optimally choose the pairs [3, 3], [1, 3], [3, 1], [1, 1] to obtain the maximum sum of transferRate = (5 + 5) + (5 + 4) + (4 + 5) + (4 + 4) = 36.

## Constraints

- `:)`

## Solutions

<!-- Scaffold placeholder: the worked derivation and solutions land
     on the solutions branch later. See ../_TEMPLATE.md for the
     expected layout, naming, and ordering conventions. -->
