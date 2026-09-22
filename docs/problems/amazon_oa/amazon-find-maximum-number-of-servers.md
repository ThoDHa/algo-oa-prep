# [Get Max Servers](https://www.fastprep.io/problems/amazon-find-maximum-number-of-servers)

**Medium** | **NN minutes** | **Array, Sorting, Greedy**

Source note: 2026-07-02 — This problem duplicates Server Selection. Sighting dates were merged into this fuller official-source version, which remains the recommended practice page.

A company that uses cloud servers is planning to scale up its application horizontally. It needs to buy a certain number of servers from a given set of n servers. To ensure that adjacent servers have similar load handling capacity, they want the computational power of two adjacent servers to have a difference of 1 or less.

Given the computational power of all the n servers as an array of integers powers, find the maximum number of servers that the client can buy such that the selected set of servers can be rearranged in a way that the absolute difference between the computational power of two adjacent servers is less than or equal to 1. The client wants to create a circular network, so the first and last servers in the sequence are also considered adjacent.

More formally, a sequence candidate[] of length m is classified as a candidate for selection by the client if it can be rearranged in a way such that abs(candidate[i] - candidate[i+1]) <= 1 for 0 <= i < m-1 and abs(candidate[m-1] - candidate[0]) <= 1.

Find the maximum number of servers the client can buy from the n available servers.

Note:

A subsequence is a sequence that can be derived from the given sequence by deleting zero or more elements without changing the order of the remaining elements.

## Examples

### Example 1

**Input:** `powers = [4, 3, 5, 1, 2, 2, 1]`

**Output:** `5`

**Explanation:** Source update (July 2, 2026) ᕙ( •̀ ᗜ •́ )ᕗ : I found an official source image that includes the example illustration.

Example source illustration











4











3











5












1










2










2










1




selected subsequence
Highlighted values form [3, 1, 2, 2, 1].






Consider powers = [4, 3, 5, 1, 2, 2, 1].

The subsequence [3, 1, 2, 2, 1] can be selected (5 servers) and rearranged to [2, 1, 1, 2, 3]. Checking circular adjacency: abs(2-1)=1, abs(1-1)=0, abs(1-2)=1, abs(2-3)=1, and (circular) abs(3-2)=1, all of which are <= 1.

No valid candidate of size greater than 5 exists, so the maximum number of servers the client can buy is 5.

## Constraints

- `1 <= n <= 2 * 10^5`
- `0 <= powers[i] <= 10^9`

## Solutions

<!-- Scaffold placeholder: the worked derivation and solutions land
     on the solutions branch later. See ../_TEMPLATE.md for the
     expected layout, naming, and ordering conventions. -->
