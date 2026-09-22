# [Next Palindromic Time](https://www.fastprep.io/problems/amazon-next-palindromic-time)

**Medium** | **NN minutes** | **String, Simulation**

Given a valid 24-hour time time in HH:MM format, return the first strictly later time whose four digits form a palindrome.Advance in one-minute steps and wrap from 23:59 to 00:00. The input itself is never returned unless a full day has elapsed.

## Examples

### Example 1

**Input:** `time = "12:21"`

**Output:** `"13:31"`

**Explanation:** 13:31 is the first later valid time whose digits read the same in both directions.

### Example 2

**Input:** `time = "23:32"`

**Output:** `"00:00"`

**Explanation:** No later palindromic time remains that day, so the search wraps to midnight.

### Example 3

**Input:** `time = "05:50"`

**Output:** `"10:01"`

**Explanation:** The next palindromic four-digit clock value after 0550 is 1001.

## Constraints

- `time.length == 5.time[2] == ':'.time is a valid zero-padded 24-hour time from 00:00 through 23:59.`

## Solutions

<!-- Scaffold placeholder: the worked derivation and solutions land
     on the solutions branch later. See ../_TEMPLATE.md for the
     expected layout, naming, and ordering conventions. -->
