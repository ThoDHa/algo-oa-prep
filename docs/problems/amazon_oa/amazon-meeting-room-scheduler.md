# [Meeting Room Scheduler](https://www.fastprep.io/problems/amazon-meeting-room-scheduler)

**Medium** | **NN minutes** | **Array, Heap, Intervals, Simulation**

Implement a scheduler for roomCount meeting rooms numbered from 0 to roomCount - 1.

Each row meetings[i] = [start, end] is a request for the half-open interval [start, end). Requests appear in nondecreasing start order and are processed in input order. Assign the lowest-numbered available room. If every room overlaps the request, reject it with -1.

Return an array whose ith value is the assigned room number or -1. A rejected request does not reserve a room.

## Examples

### Example 1

**Input:** `roomCount = 2`, `meetings = [[0,10],[5,7],[10,12],[10,15]]`

**Output:** `[0,1,0,1]`

**Explanation:** The first two requests occupy rooms 0 and 1. At time 10, both are free; input order gives the third request room 0 and the fourth room 1.

### Example 2

**Input:** `roomCount = 1`, `meetings = [[1,4],[2,3],[4,5]]`

**Output:** `[0,-1,0]`

**Explanation:** The second request conflicts with [1,4). The room is available again exactly at time 4.

### Example 3

**Input:** `roomCount = 2`, `meetings = [[1,2],[1,2],[1,2]]`

**Output:** `[0,1,-1]`

**Explanation:** Two simultaneous requests take both rooms, so the third request is rejected.

## Constraints

- `1 <= roomCount <= 10^5.`
- `1 <= meetings.length <= 10^5.`
- `meetings[i].length == 2.`
- `0 <= start < end <= 10^9.`
- `Meeting start times are nondecreasing.`

## Solutions

<!-- Scaffold placeholder: the worked derivation and solutions land
     on the solutions branch later. See ../_TEMPLATE.md for the
     expected layout, naming, and ordering conventions. -->
