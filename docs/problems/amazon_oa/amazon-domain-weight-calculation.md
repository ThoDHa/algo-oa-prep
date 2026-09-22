# [Domain Weight Calculation](https://www.fastprep.io/problems/amazon-domain-weight-calculation)

**Medium** | **NN minutes** | **String, Hash Table, Trie, Depth First Search**

Source note: This came from a real onsite interview report. The original report shared the core domain-score task and a concrete example, and FastPrep filled in the runnable function format, ordering rule, and extra practice examples so you can try it here. Estimated match rate: 90% for the core task, 75% for interface and examples, and 35% for exact original wording. If you find a fuller version, feel free to let us know and we will update it.

You are given an array of strings domainScores. Each string has this format:

domain scoredomain is a dot-separated domain name, and score is an integer weight assigned directly to that domain.

For every leaf domain, compute its total score. A domain is a leaf domain if it appears in domainScores and no other input domain has it as a suffix child.

The total score of a leaf domain is the sum of the scores assigned to that domain and all of its suffix ancestors that appear in the input.

For example, the suffix ancestors of mail.domain.com are domain.com and com.

Return one string for each leaf domain in lexicographic order. Each output string should have this format:

domain=totalScoreWhat the interview report sharedThe interview report described a domain-score task: every domain has its own score, and the candidate had to output each leaf domain's accumulated score. The report included an example where mail.domain.com accumulated scores from mail.domain.com, domain.com, and com, and contact.user.test.com accumulated scores from all of its suffix ancestors. The report did not specify the function signature, constraints, or output ordering.

How FastPrep adapted itFastPrep turned that report into a runnable practice problem by using an array of "domain score" strings as input and returning sorted "domain=score" strings. The lexicographic ordering rule and additional examples are practice scaffolding based on the reported task, not exact original wording.

## Examples

### Example 1

**Input:** `domainScores = ["com 20", "domain.com 10", "mail.domain.com 5", "test.com 10", "user.test.com 30", "contact.user.test.com -5"]`

**Output:** `["contact.user.test.com=55", "mail.domain.com=35"]`

**Explanation:** mail.domain.com is a leaf, and its total is 5 + 10 + 20 = 35.

contact.user.test.com is also a leaf, and its total is -5 + 30 + 10 + 20 = 55.

### Example 2

**Input:** `domainScores = ["com 5", "a.com 2", "b.com 3"]`

**Output:** `["a.com=7", "b.com=8"]`

**Explanation:** a.com and b.com are leaves. Both include the score of their suffix ancestor com.

### Example 3

**Input:** `domainScores = ["api.shop.com 4", "shop.com -2", "com 1", "cdn.shop.com 7", "img.cdn.shop.com 3"]`

**Output:** `["api.shop.com=3", "img.cdn.shop.com=9"]`

**Explanation:** cdn.shop.com is not a leaf because img.cdn.shop.com is one of its suffix children.

## Constraints

- `1 <= domainScores.length <= 100000`
- `Each input string contains exactly one domain and one integer score separated by one space.`
- `Domain names contain lowercase English letters and dots.`
- `Each domain label has length at least 1.`
- `Each domain appears at most once.`
- `-10^9 <= score <= 10^9`
- `The sum of all domain string lengths is at most 300000.`

## Solutions

<!-- Scaffold placeholder: the worked derivation and solutions land
     on the solutions branch later. See ../_TEMPLATE.md for the
     expected layout, naming, and ordering conventions. -->
