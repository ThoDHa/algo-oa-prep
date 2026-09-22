# [Maximize Pages Before Suspension](https://www.fastprep.io/problems/amazon-maximize-pages-before-suspension)

**Hard** | **NN minutes** | **Greedy, Sorting, Simulation**

$23

## Examples

### Example 1

**Input:** `pages = [4, 1, 5, 2, 3]`
**Input:** `threshold = [3, 3, 2, 3, 3]`

**Output:** `14`

**Explanation:** $24

### Example 2

**Input:** `pages = [2, 4, 4, 4, 5, 3]`
**Input:** `threshold = [1, 3, 1, 3, 3, 2]`

**Output:** `20`

**Explanation:** $25

### Example 3

**Input:** `pages = [2, 6, 10, 13]`
**Input:** `threshold = [2, 1, 1, 1]`

**Output:** `15`

**Explanation:** The optimal way to maximize the number of pages printed is as follows - (Assuming 1-based indexing :)

1. First, the engineers decide to activate the 4th printer, which prints 13 pages. At this point, the total number of operational printers is 1. The printing of 13 pages is completed first, followed by the suspension of any printers exceeding their threshold.

2. Next, since the threshold for printers 2, 3, and 4 is 1, and there is now 1 operational printer (4th printer), these printers become damaged. So, all the printers (2nd, 3rd, 4th) with threshold = 1, gets suspended and stop working.

3. Later, the only printer the team can turn on is printer 1. By activating printing 1, they print 2 more pages. The number of operational printer is now 1, and because threahold[1] = 2, printer 1 will not be suspended and remains functional.

So, the total number of pages printed is 13 (from printer 4) + 2(from printer 1) = 15.

we return 15.

## Constraints

- `The arrays pages and threshold have the same length n, where pages[i] is the number of pages printer i can print and threshold[i] is the suspension threshold of printer i.pages.length == threshold.length == nEach printer is in exactly one of three states at any time: operational, idle, or suspended.A printer is suspended as soon as the number of operational printers x satisfies threshold[i] <= x; its pages are counted before it is suspended.Printers are activated one at a time, and the activation order may be chosen freely to maximize the total pages printed.`

## Solutions

<!-- Scaffold placeholder: the worked derivation and solutions land
     on the solutions branch later. See ../_TEMPLATE.md for the
     expected layout, naming, and ordering conventions. -->
