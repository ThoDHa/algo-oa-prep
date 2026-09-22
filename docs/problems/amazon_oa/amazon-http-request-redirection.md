# [HTTP Request Redirection](https://www.fastprep.io/problems/amazon-http-request-redirection)

**Medium** | **NN minutes** | **Array, Hash Table, Sorting, Simulation, Geometry**

Amazon engineers are investigating an HTTP request that is redirected among servers.

There are n servers on an infinite two-dimensional plane. The coordinates of server i are given by locations[i] = [x, y]. The request starts at locations[0], and that server is marked as visited.

Each value in redirectRecords specifies one redirect direction from the current server (a, b). In every formula below, Z is an arbitrary positive integer:

Direction 1: (a, b) -> (a + Z, b + Z).Direction 2: (a, b) -> (a + Z, b - Z).Direction 3: (a, b) -> (a - Z, b + Z).Direction 4: (a, b) -> (a - Z, b - Z).Process the redirect records in order. For each record, redirect the request to the nearest server in the specified direction that has not previously been visited. If no eligible server exists in that direction, skip that redirect. Whenever the request reaches a server, mark it as visited.

Return the coordinates [x, y] of the server holding the request after all redirect records have been processed.

## Examples

### Example 1

**Input:** `locations = [[3,4],[1,2],[7,8],[5,6]]`, `redirectRecords = [1,4]`

**Output:** `[1,2]`

**Explanation:** The request starts at [3, 4]. Direction 1 points toward both [5, 6] and [7, 8], so the nearest unvisited server is [5, 6].

Direction 4 points back toward [3, 4] and then [1, 2]. Because [3, 4] has already been visited, the request moves to [1, 2].

## Constraints

<!-- Constraints not parseable from FastPrep for amazon-http-request-redirection; fill them in. -->

## Solutions

<!-- Scaffold placeholder: the worked derivation and solutions land
     on the solutions branch later. See ../_TEMPLATE.md for the
     expected layout, naming, and ordering conventions. -->
