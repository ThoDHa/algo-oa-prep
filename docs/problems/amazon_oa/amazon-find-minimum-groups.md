# [Find Minimum Groups](https://www.fastprep.io/problems/amazon-find-minimum-groups)

**Medium** | **NN minutes** | **Array, Hash Table, Greedy**

A financial services company has requested AWS for a private deployment of its cloud network. Considering the sensitive nature of the company's business, AWS has also advised them to add a specific type of security system.

Overall, there are n servers in the network where the security needs of the i-th server are represented by security[i], where each element represents the grade of security needed for a server.

To ensure the highest possible protection, the AWS security team has recommended the following rule to be followed while designing the security system: all servers in a security group must have the same grade of security needs, and the number of servers in any two security groups should not differ by more than 1.

Given an integer array security, find the minimum number of security levels needed to ensure the protection of the network.

## Examples

### Example 1

**Input:** `security = [2, 3, 3, 3, 2, 1]`

**Output:** `4`

**Explanation:** Consider n = 6 and security = [2, 3, 3, 3, 2, 1].

Then, the elements can be grouped as follows:

Group 1: 2 devices of vulnerability 2.Group 2: 2 devices of vulnerability 3.Group 3: 1 device of vulnerability 3.Group 4: 1 device of vulnerability 1.It requires 4 groups.

## Constraints

<!-- Constraints not parseable from FastPrep for amazon-find-minimum-groups; fill them in. -->

## Solutions

<!-- Scaffold placeholder: the worked derivation and solutions land
     on the solutions branch later. See ../_TEMPLATE.md for the
     expected layout, naming, and ordering conventions. -->
