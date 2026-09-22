# [Most Frequent Consecutive Website Pattern](https://www.fastprep.io/problems/amazon-consecutive-website-visit-pattern)

**Medium** | **NN minutes** | **Array, Hash Table, Sorting, String**

You are given three equal-length arrays describing website visits. Entry i contains a username, an integer timestamp, and a website.For each user, sort visits by timestamp; when timestamps are equal, keep their original input order. Every three adjacent visits in that per-user order form a consecutive website pattern. A user contributes at most once to the count of any distinct pattern, even if that pattern occurs several times for the user.Return the three websites in the pattern seen by the greatest number of distinct users. If several patterns have the same count, return the lexicographically smallest three-element sequence. If no user has at least three visits, return an empty array.

## Examples

### Example 1

**Input:** `usernames = ["amy","amy","amy","ben","ben","ben"]`
**Input:** `timestamps = [1,2,3,1,2,3]`
**Input:** `websites = ["home","cart","pay","home","cart","pay"]`

**Output:** `["home","cart","pay"]`

**Explanation:** Both users have the consecutive pattern [home, cart, pay], so it has two distinct-user supporters.

### Example 2

**Input:** `usernames = ["a","a","a","b","b","b"]`
**Input:** `timestamps = [3,1,2,1,2,3]`
**Input:** `websites = ["z","a","z","a","z","z"]`

**Output:** `["a","z","z"]`

**Explanation:** User a produces [a, z, z], and user b produces the same pattern. Sorting is performed within each user rather than on the global input.

### Example 3

**Input:** `usernames = ["a","a","b"]`
**Input:** `timestamps = [1,2,1]`
**Input:** `websites = ["x","y","z"]`

**Output:** `[]`

**Explanation:** No user has three visits, so no consecutive triple exists.

## Constraints

- `0 <= usernames.length <= 5000.usernames.length == timestamps.length == websites.length.Usernames and websites contain 1 to 30 lowercase English letters.0 <= timestamps[i] <= 10^9.Input rows may be globally unordered; equal timestamps for one user retain input order.`

## Solutions

<!-- Scaffold placeholder: the worked derivation and solutions land
     on the solutions branch later. See ../_TEMPLATE.md for the
     expected layout, naming, and ordering conventions. -->
