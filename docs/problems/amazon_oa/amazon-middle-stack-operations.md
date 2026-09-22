# [Stack with Constant-Time Middle Queries](https://www.fastprep.io/problems/amazon-middle-stack-operations)

**Medium** | **NN minutes** | **Array, Stack, Design, Simulation**

Process a sequence of stack operations. Each operation is ["push", value], ["pop"], ["top"], or ["middle"]. Values are signed decimal integers encoded as strings.Return one string for every non-push operation. For an empty stack, return EMPTY. For an even-sized stack, middle returns the lower middle element, the one closer to the bottom. Every operation must run in constant time; preallocated array storage is allowed.

## Examples

### Example 1

**Input:** `operations = [["push","1"],["push","2"],["push","3"],["middle"],["top"],["pop"],["middle"]]`

**Output:** `["2","3","3","1"]`

**Explanation:** The lower middle of three values is 2; after popping 3, the lower middle of [1,2] is 1.

### Example 2

**Input:** `operations = [["top"],["middle"],["pop"]]`

**Output:** `["EMPTY","EMPTY","EMPTY"]`

**Explanation:** All three queries use the empty sentinel.

### Example 3

**Input:** `operations = [["push","-4"],["middle"],["pop"]]`

**Output:** `["-4","-4"]`

**Explanation:** A one-element stack has the same top and middle.

## Constraints

- `1 &le; operations.length &le; 100000.Every operation has one of the four documented forms.Push values are integers in [-10^9, 10^9].The output contains one entry for every non-push operation.`

## Solutions

<!-- Scaffold placeholder: the worked derivation and solutions land
     on the solutions branch later. See ../_TEMPLATE.md for the
     expected layout, naming, and ordering conventions. -->
