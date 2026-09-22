# [Domain Weight Calculation](https://www.fastprep.io/problems/amazon-domain-weight-calculation)

**Medium** | **NN minutes** | **String, Hash Table, Trie, Depth First Search**

$23

## Examples

### Example 1

**Input:** `domainScores = ["com 20", "domain.com 10", "mail.domain.com 5", "test.com 10", "user.test.com 30", "contact.user.test.com -5"]`

**Output:** `["contact.user.test.com=55", "mail.domain.com=35"]`

**Explanation:** mail.domain.com is a leaf, and its total is 5 + 10 + 20 = 35.contact.user.test.com is also a leaf, and its total is -5 + 30 + 10 + 20 = 55.

### Example 2

**Input:** `domainScores = ["com 5", "a.com 2", "b.com 3"]`

**Output:** `["a.com=7", "b.com=8"]`

**Explanation:** a.com and b.com are leaves. Both include the score of their suffix ancestor com.

### Example 3

**Input:** `domainScores = ["api.shop.com 4", "shop.com -2", "com 1", "cdn.shop.com 7", "img.cdn.shop.com 3"]`

**Output:** `["api.shop.com=3", "img.cdn.shop.com=9"]`

**Explanation:** cdn.shop.com is not a leaf because img.cdn.shop.com is one of its suffix children.

## Constraints

- `1 <= domainScores.length <= 100000Each input string contains exactly one domain and one integer score separated by one space.Domain names contain lowercase English letters and dots.Each domain label has length at least 1.Each domain appears at most once.-10^9 <= score <= 10^9The sum of all domain string lengths is at most 300000.`

## Solutions

<!-- Scaffold placeholder: the worked derivation and solutions land
     on the solutions branch later. See ../_TEMPLATE.md for the
     expected layout, naming, and ordering conventions. -->
