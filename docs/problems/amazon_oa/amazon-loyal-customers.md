# [Loyal Customers Across Two Days](https://www.fastprep.io/problems/amazon-loyal-customers)

**Easy** | **NN minutes** | **Hash Table, Sorting**

You are given two arrays of website logs, dayOneLogs and dayTwoLogs. Each log entry contains exactly three strings in this order: timestamp, customerId, and pageId.

A customer is loyal when both conditions hold:

The customer appears in the logs on both days.On each day, the customer visits more than two distinct pages.Return the loyal customer IDs in lexicographically increasing order. Repeated visits to the same page count only once for that day.

## Examples

### Example 1

**Input:** `dayOneLogs = [["09:00","alice","home"],["09:05","alice","search"],["09:10","alice","checkout"],["10:00","bob","home"],["10:05","bob","search"],["10:10","bob","checkout"],["11:00","cara","home"],["11:05","cara","search"],["11:10","cara","checkout"]]`, `dayTwoLogs = [["09:00","alice","home"],["09:05","alice","offers"],["09:10","alice","checkout"],["10:00","bob","home"],["10:05","bob","search"],["12:00","dan","home"],["12:05","dan","search"],["12:10","dan","checkout"]]`

**Output:** `["alice"]`

**Explanation:** alice visits three distinct pages on each day. bob visits only two distinct pages on day two, cara is absent on day two, and dan is absent on day one.

### Example 2

**Input:** `dayOneLogs = [["1","cust-b","p1"],["2","cust-b","p2"],["3","cust-b","p3"],["4","cust-a","p1"],["5","cust-a","p2"],["6","cust-a","p3"]]`, `dayTwoLogs = [["7","cust-a","p4"],["8","cust-a","p5"],["9","cust-a","p6"],["10","cust-b","p4"],["11","cust-b","p5"],["12","cust-b","p6"]]`

**Output:** `["cust-a","cust-b"]`

**Explanation:** Both customers visit three distinct pages on each day. The returned IDs are sorted lexicographically.

## Constraints

- `Every log entry contains exactly three strings: timestamp, customerId, and pageId.`
- `Customer IDs and page IDs are compared exactly as provided.`
- `The timestamp does not affect whether a customer is loyal.`

## Solutions

<!-- Scaffold placeholder: the worked derivation and solutions land
     on the solutions branch later. See ../_TEMPLATE.md for the
     expected layout, naming, and ordering conventions. -->
