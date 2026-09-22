# [Reconstruct Itinerary](https://leetcode.com/problems/reconstruct-itinerary/)

**Hard** | **NN minutes** | **Depth-First Search, Graph Theory, Eulerian Circuit**

You are given a list of flight tickets `tickets` where `tickets[i] = [from_i, to_i]` represent the source airport and the destination airport. 

Each `from_i` and `to_i` consists of three uppercase English letters.

Reconstruct the itinerary in order and return it.

All of the tickets belong to someone who originally departed from `"JFK"`. Your objective is to reconstruct the flight path that this person took, assuming each ticket was used exactly once.

If there are multiple valid flight paths, return the lexicographically smallest one.
* For example, the itinerary `["JFK", "SEA"]` has a smaller lexical order than `["JFK", "SFO"]`.

You may assume all the tickets form at least one valid flight path.

## Examples

### Example 1

**Input:** `tickets = [["BUF","HOU"],["HOU","SEA"],["JFK","BUF"]]`

**Output:** `["JFK","BUF","HOU","SEA"]`

### Example 2

**Input:** `tickets = [["HOU","JFK"],["SEA","JFK"],["JFK","SEA"],["JFK","HOU"]]`

**Output:** `["JFK","HOU","JFK","SEA","JFK"]`

**Explanation:** Another possible reconstruction is `["JFK","SEA","JFK","HOU","JFK"]` but it is lexicographically larger.

## Constraints

- `1 <= tickets.length <= 300`
- `from_i != to_i`

## Solutions

<!-- Scaffold placeholder: the worked derivation and solutions land
     on the solutions branch later. See ../_TEMPLATE.md for the
     expected layout, naming, and ordering conventions. -->
