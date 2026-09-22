# [Initial and Final Accounts in a Transfer Chain](https://www.fastprep.io/problems/amazon-transfer-chain-endpoints)

**Easy** | **NN minutes** | **Array, Hash Table, Graph**

You are given directed account-transfer pairs [from, to] in arbitrary order. Together they form one non-branching chain containing every pair exactly once.Return [initialAccount, finalAccount], where the initial account has no incoming transfer and the final account has no outgoing transfer.

## Examples

### Example 1

**Input:** `transfers = [[222,111],[111,333],[444,222]]`

**Output:** `[444,333]`

**Explanation:** The complete chain is 444 to 222 to 111 to 333.

### Example 2

**Input:** `transfers = [[1,2]]`

**Output:** `[1,2]`

**Explanation:** A one-transfer chain exposes both endpoints directly.

### Example 3

**Input:** `transfers = [[3,4],[1,3],[4,8]]`

**Output:** `[1,8]`

**Explanation:** Input order does not affect the recovered endpoints.

## Constraints

- `1 &le; transfers.length &le; 100000.Every transfer contains two distinct integer account IDs.The pairs form exactly one acyclic chain with no branches.`

## Solutions

<!-- Scaffold placeholder: the worked derivation and solutions land
     on the solutions branch later. See ../_TEMPLATE.md for the
     expected layout, naming, and ordering conventions. -->
