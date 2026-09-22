# [Find Max Num](https://www.fastprep.io/problems/amazon-find-maximum-num)

**Easy** | **NN minutes** | **Array, Greedy, Sorting**

$24

## Examples

### Example 1

**Input:** `answered = [24, 27, 0]`
**Input:** `needed = [51, 52, 100]`
**Input:** `q = 100`

**Output:** `2`

**Explanation:** Here answered=[24,27,0] and needed=[51,52,100]. The additional answers needed to pass are [27,25,100]. The best distribution is at least 27+25=52 questions among the first two subjects. It would take all q=100 questions to pass the third subject.

### Example 2

**Input:** `answered = [24, 27, 0]`
**Input:** `needed = [51, 52, 100]`
**Input:** `q = 200`

**Output:** `3`

**Explanation:** Explanation not found. If you happen to know about it, feel free to lmk! Manyyy thx in advance 🫰

### Example 3

**Input:** `answered = [2, 4]`
**Input:** `needed = [4, 5]`
**Input:** `q = 1`

**Output:** `1`

**Explanation:** There are n = 2 subjects and needed = [4, 5] answered questions, respectively, to pass. The student has answered answered = [2, 4] questions in the two subjects so far, and can answer another q = 1 questions in all subjects combined. The best outcome is to answer an additional question in the second subject to pass it, and it is not possible to pass the first subject. The maximum num of subjects that can be passed is 1 :)

## Constraints

- `1 ≤ n ≤ 10^5`
- `0 ≤ answered[i], needed[i], q ≤ 10^9`

## Solutions

<!-- Scaffold placeholder: the worked derivation and solutions land
     on the solutions branch later. See ../_TEMPLATE.md for the
     expected layout, naming, and ordering conventions. -->
