# [Closest Version Date](https://www.fastprep.io/problems/amazon-closest-version-date)

**Easy** | **NN minutes** | **Array, String, Binary Search**

2026-07-02 •ᴗ• Practice note: This version should match the core of the reported interview question by about 85%-90%. It was reported for SDE II. It may not be word-for-word identical, but the main idea and expected approach are close.

You are given a target date and a list of release dates for different software versions. Return the release date that is closest to the target date. The distance between two dates is the absolute number of calendar days between them.

If two release dates are equally close to the target date, return the later date. All dates are provided in YYYY-MM-DD format.

Function Signature

function findClosestVersionDate(targetDate: string, versions: string[]): string

## Examples

### Example 1

**Input:** `targetDate = "2026-04-01"`, `versions = ["2023-04-01", "2025-04-01", "2026-05-03"]`

**Output:** `"2026-05-03"`

**Explanation:** 2023-04-01 is 1096 days away, 2025-04-01 is 365 days away, and 2026-05-03 is 32 days away. The closest release date is 2026-05-03.

### Example 2

**Input:** `targetDate = "2024-06-10"`, `versions = ["2024-06-01", "2024-06-20", "2024-07-01"]`

**Output:** `"2024-06-01"`

**Explanation:** 2024-06-01 is 9 days away, which is closer than 2024-06-20 and 2024-07-01.

### Example 3

**Input:** `targetDate = "2025-01-15"`, `versions = ["2025-01-10", "2025-01-20"]`

**Output:** `"2025-01-20"`

**Explanation:** Both dates are 5 days away. Since there is a tie, return the later date.

### Example 4

**Input:** `targetDate = "2026-04-01"`, `versions = ["2026-04-01", "2026-05-03", "2025-12-31"]`

**Output:** `"2026-04-01"`

**Explanation:** An exact match has distance 0, so it is the closest version date.

## Constraints

- `1 <= versions.length <= 100000`
- `targetDate and every date in versions are valid dates in YYYY-MM-DD format.`
- `versions may not be sorted.`
- `Follow-up`
- `If versions is already sorted, can you solve each query faster than checking every date? What if there are many target dates queried against the same version list?`

## Solutions

<!-- Scaffold placeholder: the worked derivation and solutions land
     on the solutions branch later. See ../_TEMPLATE.md for the
     expected layout, naming, and ordering conventions. -->
