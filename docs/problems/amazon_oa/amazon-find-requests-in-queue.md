# [Find Requests In Queue](https://www.fastprep.io/problems/amazon-find-requests-in-queue)

**Medium** | **NN minutes** | **Queue, Simulation**

$23

## Examples

### Example 1

**Input:** `wait = [2, 2, 3, 1]`

**Output:** `[4, 2, 1, 0]`

**Explanation:** - time = 0 seconds, the 1st request is served. The number of requests in the queue is 4. queue = [1, 2, 3, 4].


- time = 1 second, request 1 is removed because it is processed, request 4 (wait[3] = 1) is removed because time = wait[3] = 1 which exceeds its maximum waiting time. Also, request 2 is served. The number of requests in the queue at time = 1 seconds is 2. queue = [2, 3].


- time = 2 seconds, request 2 is removed because it is processed, request 3 is served. The number of requests in the queue is 1. queue = [3].


- time = 3 seconds, request 3 is removed because it is processed. The number of requests in the queue is 0. queue = [empty].

    
The answer is [4, 2, 1, 0].

### Example 2

**Input:** `wait = [4, 4, 4]`

**Output:** `[3, 2, 1, 0]`

**Explanation:** time = 0 seconds, request 1 is served. queue = [1, 2, 3]

time = 1 second, request 1 is removed as it is processed, request 2 is served. queue = [2, 3]

time = 2 seconds, request 2 is removed as it is processed, request 3 is served. queue = [3]

time = 3 seconds, request 3 is removed as it is processed. queue = [empty]

so the answer is [3, 2, 1, 0]~~

### Example 3

**Input:** `wait = [3, 1, 2, 1]`

**Output:** `[4, 1, 0]`

**Explanation:** time = 0 secons, request 1 is served. The num of requests in queue is 4. queue = [3, 1, 2, 1]

time = 1 second, request 1 is removed as it is processed, request 2 and 4 are removed as time exceeds their max wating time 🥲, which is wait[1] = wait[3] = 1. Finally request 3 is served 🙌. The num of requests in the queue is 1. queue = [3]

time = 2 seconds, request 3 is removed as it is processed. The num of requests in the queue is 0, queue = [empty]

so the answer is [4, 1, 0]~

## Constraints

- `1 ≤ n ≤ 105`
- `1 ≤ wait[i] ≤ 105`

## Solutions

<!-- Scaffold placeholder: the worked derivation and solutions land
     on the solutions branch later. See ../_TEMPLATE.md for the
     expected layout, naming, and ordering conventions. -->
