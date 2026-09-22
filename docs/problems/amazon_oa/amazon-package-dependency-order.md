# [Package Dependency Order](https://www.fastprep.io/problems/amazon-package-dependency-order)

**Medium** | **NN minutes** | **Graph, Depth First Search, Topological Sort**

You are given package dependency pairs and a target package. Each pair [package, dependency] means the package depends on that dependency.Return an order in which to install the target package and all of its transitive dependencies so that every dependency appears before the package that needs it.If there is a cyclic dependency among packages needed by the target package, return an empty array.The source noted that multiple valid orders may exist. FastPrep uses this deterministic rule: process dependencies in the order they appear in the input pairs.

## Examples

### Example 1

**Input:** `dependencies = [["A","B"],["A","C"],["B","D"],["B","E"],["B","F"],["C","F"],["F","G"],["H","I"],["H","J"],["J","G"]]`
**Input:** `target = "A"`

**Output:** `["D","E","G","F","B","C","A"]`

**Explanation:** The order installs D, E, and F before B; installs G before F; installs F before C; and installs both B and C before A.

## Constraints

<!-- Constraints not parseable from FastPrep for amazon-package-dependency-order; fill them in. -->

## Solutions

<!-- Scaffold placeholder: the worked derivation and solutions land
     on the solutions branch later. See ../_TEMPLATE.md for the
     expected layout, naming, and ordering conventions. -->
