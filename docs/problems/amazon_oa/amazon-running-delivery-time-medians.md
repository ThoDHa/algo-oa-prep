# [Running Delivery Time Medians](https://www.fastprep.io/problems/amazon-running-delivery-time-medians)

**Medium** | **NN minutes** | **Heap, Design**

Given an array deliveryTimes, process the values from left to right. After each new delivery time arrives, output the median of all delivery times seen so far.When the number of seen values is even, use the lower median, meaning the larger value in the lower half after sorting.Return an array containing the median after each insertion.

## Examples

### Example 1

**Input:** `deliveryTimes = [5,17,100,11]`

**Output:** `[5,5,17,11]`

**Explanation:** The sorted prefixes are [5], [5,17], [5,17,100], and [5,11,17,100]. Their lower medians are 5, 5, 17, and 11.

## Constraints

- `deliveryTimes are processed from left to right.After each new value is inserted, record the median of all values seen so far.When the number of seen values is even, use the lower median: the larger value in the lower half after sorting.Return one median for each insertion.`

## Solutions

<!-- Scaffold placeholder: the worked derivation and solutions land
     on the solutions branch later. See ../_TEMPLATE.md for the
     expected layout, naming, and ordering conventions. -->
