"""Rice Bags — https://www.fastprep.io/problems/max-set-size

Write-up & approaches: ../../docs/problems/amazon_oa/max-set-size.md

$23

  uv run python amazon_oa/max-set-size/solution.py   # debug one case (see CASE below)
  uv run pytest amazon_oa/max-set-size/              # run the test sets
"""

from harness import NotSolved, pick_case


class Solution:
    def maxSetSize(self, riceBags):
        """State the time and space complexity of your approach, and explain why.

        Time:  O(?):
        Space: O(?):
        """
        raise NotSolved


if __name__ == "__main__":
    # Debug playground: set a breakpoint in maxSetSize above, then run this file.
    # Pick a case by id (ids are in cases.json).
    CASE = "example_1"
    case = pick_case(__file__, CASE)
    result = Solution().maxSetSize(*case["args"])
    print(f"case {case['id']}: args = {case['args']}")
    print(f"expected: {case['expected']}")
    print(f"got:      {result}")
