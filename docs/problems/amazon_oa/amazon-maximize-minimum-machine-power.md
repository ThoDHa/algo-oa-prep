# [Maximize Minimum Machine Power](https://www.fastprep.io/problems/amazon-maximize-minimum-machine-power)

**unknown difficulty** | **NN minutes** | **unknown categories**

You are given an integer array sources, where sources[i] is the amount of power available from the i-th power source, and an integer n representing the number of machines.

Each machine must receive power from exactly one source. A source may power multiple machines, but the total power assigned from that source cannot exceed its capacity.

Return the maximum possible value of the minimum power assigned to any machine.

## Examples

### Example 1

**Input:** `sources = [5, 8, 6]`, `n = 4`

**Output:** `4`

**Explanation:** A minimum assignment of 4 is possible: the sources can support 1 + 2 + 1 = 4 machines with at least 4 power each. A minimum of 5 would support only 1 + 1 + 1 = 3 machines.

### Example 2

**Input:** `sources = [10, 10]`, `n = 3`

**Output:** `5`

**Explanation:** Each source can power two machines with 5 power each, so three machines can be powered. A minimum of 6 would allow only two machines total.

## Constraints

- `1 <= sources.length`
- `1 <= n`
- `sources[i] is a non-negative integer power capacity.`

## Solutions

<!-- Scaffold placeholder: the worked derivation and solutions land
     on the solutions branch later. See ../_TEMPLATE.md for the
     expected layout, naming, and ordering conventions. -->
