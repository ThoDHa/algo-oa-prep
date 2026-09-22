# [Maximum System Memory Capacity](https://www.fastprep.io/problems/amazon-maximum-capacity)

**Easy** | **NN minutes** | **Sorting, Greedy**

Amazon is optimizing the capacity of a cloud system with n servers. The memory capacity of the i-th server is memory[i].A system uses an even number of servers. If it uses 2x servers, exactly x are primary servers and the other x are backup servers. For every primary server P, it must be paired with a distinct backup server B whose memory capacity is at least that of P.The system memory capacity is the sum of the memory capacities of all primary servers. You may leave servers unused. Given memory, return the maximum system memory capacity that can be formed.Complete maximumCapacity, which receives the integer array memory and returns the maximum capacity as a long.

## Examples

### Example 1

**Input:** `memory = [1, 2, 1, 2]`

**Output:** `3`

**Explanation:** Here, we have 4 servers [serverA, serverB, serverC, serverD] having memory sizes as [1, 2, 1, 2].

We can choose serverA and serverB as primary servers, and serverC and serverD as their respective backup.
The conditions hold true since memory[serverC] ≥ memory[serverA] and memory[serverD] ≥ memory[serverB].
Hence, the maximum system memory capacity is 3.

### Example 2

**Input:** `memory = [1, 2, 1]`

**Output:** `1`

**Explanation:** Here, we have 3 servers [serverA, serverB, serverC] having memory sizes as [1, 2, 1].

We can choose serverA as a primary server, and serverB as its respective backup server.
The conditions hold true since memory[serverB] ≥ memory[serverA].
Hence, the maximum system memory capacity is 1.

### Example 3

**Input:** `memory = [2, 4, 3, 1, 2]`

**Output:** `5`

**Explanation:** $23

## Constraints

- `2 ≤ n ≤ 2 * 10^5`
- `1 ≤ size[i] ≤ 10^9`

## Solutions

<!-- Scaffold placeholder: the worked derivation and solutions land
     on the solutions branch later. See ../_TEMPLATE.md for the
     expected layout, naming, and ordering conventions. -->
