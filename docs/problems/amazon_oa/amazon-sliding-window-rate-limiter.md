# [Sliding-Window Rate Limiter](https://www.fastprep.io/problems/amazon-sliding-window-rate-limiter)

**Medium** | **NN minutes** | **Queue, Hash Table, Sliding Window, Design**

You receive requests in nondecreasing timestamp order. Each request has a user ID and an integer timestamp in seconds.

A request is accepted when that user has fewer than 100 previously accepted requests in the interval (timestamp - 60, timestamp]. Otherwise it is rejected. Rejected requests do not consume capacity. Requests with the same timestamp are processed in input order.

Return one boolean per input request, where true means accepted and false means rejected.

## Examples

### Example 1

**Input:** `userIds = ["amy","amy","amy","amy","amy","amy","amy","amy","amy","amy","amy","amy","amy","amy","amy","amy","amy","amy","amy","amy","amy","amy","amy","amy","amy","amy","amy","amy","amy","amy","amy","amy","amy","amy","amy","amy","amy","amy","amy","amy","amy","amy","amy","amy","amy","amy","amy","amy","amy","amy","amy","amy","amy","amy","amy","amy","amy","amy","amy","amy","amy","amy","amy","amy","amy","amy","amy","amy","amy","amy","amy","amy","amy","amy","amy","amy","amy","amy","amy","amy","amy","amy","amy","amy","amy","amy","amy","amy","amy","amy","amy","amy","amy","amy","amy","amy","amy","amy","amy","amy","amy"]`, `timestamps = [10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]`

**Output:** `[true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,false]`

**Explanation:** The first 100 requests for amy fill the window. The 101st request has the same timestamp and is rejected.

### Example 2

**Input:** `userIds = ["a","b","a","a"]`, `timestamps = [0,0,59,60]`

**Output:** `[true,true,true,true]`

**Explanation:** Users have independent windows. At timestamp 60, the accepted request for a at timestamp 0 lies on the excluded lower boundary and has expired.

## Constraints

- `0 <= userIds.length <= 5000.`
- `userIds.length == timestamps.length.`
- `User IDs contain 1 to 50 lowercase English letters or digits.`
- `0 <= timestamps[i] <= 10^9.`
- `Timestamps are nondecreasing.`

## Solutions

<!-- Scaffold placeholder: the worked derivation and solutions land
     on the solutions branch later. See ../_TEMPLATE.md for the
     expected layout, naming, and ordering conventions. -->
