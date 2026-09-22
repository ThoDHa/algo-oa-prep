# [Get Distinct Pairs](https://www.fastprep.io/problems/amazon-get-distinct-pairs)

**Easy** | **NN minutes** | **Hash Table, Two Pointers**

A financial strategist at Amazon Web Services (AWS) is analyzing a collection of profitable investments, each represented by an integer array. Every value in the array indicates the annual gain of a particular investment. The strategist's goal is to identify all unique investment pairs whose combined annual returns exactly match a given target value.
    


    Unique pairs are defined as combinations that vary by at least one element (i.e., their values are not at the exact same positions or do not have identical values in identical positions).
    


    Given the array of gains, compute the number of unique investment pairs whose sum equals the specified target return.

## Examples

### Example 1

**Input:** `stocksProfit = [5, 7, 9, 13, 11, 6, 6, 3, 3]`, `target = 12`

**Output:** `3`

**Explanation:** There are four pairs whose combined gains equal the target return of 12. However, since the array includes duplicate values of 3, there are two versions of the pair (9, 3): one between positions 2 and 7, and another between positions 2 and 8. But only one of these can be counted to maintain uniqueness.

Therefore, the valid and unique pairs are:



(5, 7)(3, 9)(6, 6)

We return 3.

## Constraints

- `1 ≤ n ≤ 5 x 10^5`
- `0 ≤ investmentReturns[i] ≤ 10^9`
- `0 ≤ goal ≤ 5 x 10^9`

## Solutions

<!-- Scaffold placeholder: the worked derivation and solutions land
     on the solutions branch later. See ../_TEMPLATE.md for the
     expected layout, naming, and ordering conventions. -->
