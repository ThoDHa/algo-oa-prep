# [Get Smallest Base Segment](https://www.fastprep.io/problems/amazon-get-smallest-base-segment)

**unknown difficulty** | **NN minutes** | **unknown categories**

In Amazon's distributed storage network, some critical data segments are missing. They are represented by a string missingData. The system restores data by choosing a base segment of length segmentSize and repeatedly appending copies of that base segment to a generated string.

A base segment is valid if, after some number of replications, the generated string contains every character in missingData at least as many times as it appears in missingData.

Among all valid base segments, choose one that requires the fewest replications. If more than one base segment requires that same minimum number of replications, return the lexicographically smallest one. If no valid base segment exists, return "-1".

## Examples

### Example 1

**Input:** `segmentSize = 2`, `missingData = "aavvavv"`

**Output:** `"av"`

**Explanation:** The character a appears 3 times and v appears 4 times. Both "av" and "va" require 4 replications. Since "av" is lexicographically smaller, it is returned.

### Example 2

**Input:** `segmentSize = 1`, `missingData = "abc"`

**Output:** `"-1"`

**Explanation:** A base segment of length 1 can contain only one distinct character, so it cannot generate all three required characters.

## Constraints

- `1 <= segmentSize <= missingData.length`
- `missingData consists of lowercase English letters.`

## Solutions

<!-- Scaffold placeholder: the worked derivation and solutions land
     on the solutions branch later. See ../_TEMPLATE.md for the
     expected layout, naming, and ordering conventions. -->
