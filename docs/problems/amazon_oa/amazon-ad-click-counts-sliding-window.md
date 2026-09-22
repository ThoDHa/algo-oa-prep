# [Recent Advertisement Click Counts](https://www.fastprep.io/problems/amazon-ad-click-counts-sliding-window)

**Medium** | **NN minutes** | **Queue, Hash Table, Sliding Window, Design**

You receive a finite sequence of advertisement click and count operations. Each operation is one of:

CLICK <adId> <timestamp>: record one click for the advertisement.COUNT <adId> <timestamp>: report how many clicks that advertisement received during the latest kMinutes.Timestamps are integer seconds and never decrease. Process operations in input order, including operations with the same timestamp. For a count at time t, include clicks whose timestamps are in the inclusive interval [t - 60 * kMinutes + 1, t].

Return one integer for each COUNT operation, in query order. CLICK operations produce no output.

## Examples

### Example 1

**Input:** `operations = ["CLICK shoes 100","CLICK books 120","CLICK shoes 159","COUNT shoes 160","COUNT books 180","COUNT shoes 220"]`, `kMinutes = 1`

**Output:** `[1,0,0]`

**Explanation:** At time 160, only the shoes click at 159 remains in [101,160]. The books click at 120 is outside [121,180], and both shoes clicks are outside [161,220].

### Example 2

**Input:** `operations = ["CLICK ad1 10","CLICK ad1 69","COUNT ad1 69","COUNT ad1 70"]`, `kMinutes = 1`

**Output:** `[2,1]`

**Explanation:** At time 69, timestamp 10 is exactly the inclusive lower boundary. At time 70, the lower boundary advances to 11, so only the click at 69 remains.

## Constraints

- `1 <= operations.length <= 100000.`
- `1 <= kMinutes <= 100000.`
- `Every operation is exactly CLICK <adId> <timestamp> or COUNT <adId> <timestamp>, with single spaces between tokens.`
- `Each advertisement ID contains 1 to 50 lowercase English letters or digits.`
- `0 <= timestamp <= 10^12, and timestamps are nondecreasing.`
- `Use signed 64-bit arithmetic for timestamps and window boundaries.`

## Solutions

<!-- Scaffold placeholder: the worked derivation and solutions land
     on the solutions branch later. See ../_TEMPLATE.md for the
     expected layout, naming, and ordering conventions. -->
