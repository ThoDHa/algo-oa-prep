# [Get Total Requests](https://www.fastprep.io/problems/amazon-get-total-requests)

**Easy** | **NN minutes** | **Array, Hash Table, Simulation**

$23

## Examples

### Example 1

**Input:** `server = [20, 10]`
**Input:** `replaced = [10, 20]`
**Input:** `newId = [20, 1]`

**Output:** `[40, 2]`

**Explanation:** Day 1: The servers are [20, 10]. Server with id 10 is replaced by a server with id 20. New servers are [20, 20]. Total requests = 20 + 20 = 40.
      
        Day 2: The servers are [20, 20]. Server with id 20 is replaced by a server with id 1. New servers are [1, 1]. Total requests = 1 + 1 = 2.
      
        Hence the answer is [40, 2].

### Example 2

**Input:** `server = [3, 3]`
**Input:** `replaced = [3, 1]`
**Input:** `newId = [1, 5]`

**Output:** `[2, 10]`

**Explanation:** After the first day, the servers are [1, 1].

After the second day, the servers are [5, 5] :)

### Example 3

**Input:** `server = [2, 5, 2]`
**Input:** `replaced = [2, 5, 3]`
**Input:** `newId = [3, 1, 5]`

**Output:** `[11, 7, 11]`

**Explanation:** After the first day, the servers are [3, 5, 3].)

After the second day, the servers are [3, 1, 3] :)

After the third day,the servers are [5, 1, 5] :)

## Constraints

- `1 ≤ n ≤ 10^51 ≤ server[i], replaced[i], newId[i] < 10^4server, replaced, and newId each have exactly n elements.`

## Solutions

<!-- Scaffold placeholder: the worked derivation and solutions land
     on the solutions branch later. See ../_TEMPLATE.md for the
     expected layout, naming, and ordering conventions. -->
