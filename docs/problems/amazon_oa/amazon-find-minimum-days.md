# [Find Minimum Days](https://www.fastprep.io/problems/amazon-find-minimum-days)

**Hard** | **NN minutes** | **Binary Search, Sliding Window**

$23

## Examples

### Example 1

**Input:** `pages = [3, 1, 4]`
**Input:** `k = 2`
**Input:** `p = 2`

**Output:** `4`

**Explanation:** There are n=3 chapters with pages=[3,1,4], k=2 consecutive chapters per day, and up to p=2 pages read from each chosen chapter per day. One optimal sequence (4 days):
Day 1: Choose chapters 1 and 2. Remaining pages: [1, 0, 4].
Day 2: Choose chapters 1 and 2. Remaining pages: [0, 0, 4].
Day 3: Choose chapters 2 and 3. Remaining pages: [0, 0, 2].
Day 4: Choose chapters 2 and 3. Remaining pages: [0, 0, 0].
Chapter 1 needs ceil(3/2)=2 coverings, chapter 2 needs ceil(1/2)=1, and chapter 3 needs ceil(4/2)=2. Since every window has length k=2 and must lie within the chapters, chapters 1 and 3 can never be covered by the same window, so their required coverings (2 + 2 = 4) cannot be combined into the same days. Hence the chapters cannot be completed in fewer than 4 days, and the answer is 4.

### Example 2

**Input:** `pages = [3, 4]`
**Input:** `k = 1`
**Input:** `p = 2`

**Output:** `4`

**Explanation:** Let's trace this sample case:

Day 1: Choose chapter 1 (pages = 3). Read min(3,2)=2 pages. Remaining pages: [3−2,4]=[1,4].
Day 2: Choose chapter 1 (pages = 1). Read min(1,2)=1 page. Remaining pages: [1−1,4]=[0,4].
Day 3: Choose chapter 2 (pages = 4). Read min(4,2)=2 pages. Remaining pages: [0,4−2]=[0,2].
Day 4: Choose chapter 2 (pages = 2). Read min(2,2)=2 pages. Remaining pages: [0,2−2]=[0,0].

So, for this sample case, the minimum number of days would be 4.

This test case is fromt the second source we found. You can find source ss from the second source images in the Problem Source section below.

## Constraints

- `1 ≤ n ≤ 10^51 ≤ pages[i] ≤ 10^91 ≤ k ≤ n1 ≤ p ≤ 10^9`

## Solutions

<!-- Scaffold placeholder: the worked derivation and solutions land
     on the solutions branch later. See ../_TEMPLATE.md for the
     expected layout, naming, and ordering conventions. -->
