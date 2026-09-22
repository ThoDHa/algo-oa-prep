# [Product Category Group Sizes](https://www.fastprep.io/problems/amazon-product-category-groups)

**Easy** | **NN minutes** | **Union Find, Sorting**

You are given a list of products and a list of pairs. Each pair means the two products belong to the same category. Category membership is transitive: if product A is in the same category as B, and B is in the same category as C, then A and C are in the same category.Return the size of every final category group, sorted in increasing order. The number of returned sizes is the number of final categories.Function Description Complete the function productCategoryGroupSizes in the editor.productCategoryGroupSizes has the following parameters:String products[]: all product identifiersString pairs[][]: product pairs that belong to the same categoryReturns int[]: the sorted sizes of the final category groups

## Examples

### Example 1

**Input:** `products = ["A", "B", "C", "D", "E"]`
**Input:** `pairs = [["A", "B"], ["B", "C"], ["D", "E"]]`

**Output:** `[2, 3]`

**Explanation:** A, B, and C form one category of size 3. D and E form one category of size 2.

### Example 2

**Input:** `products = ["p1", "p2", "p3", "p4"]`
**Input:** `pairs = [["p1", "p2"]]`

**Output:** `[1, 1, 2]`

**Explanation:** Products p3 and p4 are not paired with any other product, so each is its own category.

## Constraints

- `Product identifiers are unique in products.Each pair contains two valid product identifiers.Category membership is transitive.`

## Solutions

<!-- Scaffold placeholder: the worked derivation and solutions land
     on the solutions branch later. See ../_TEMPLATE.md for the
     expected layout, naming, and ordering conventions. -->
