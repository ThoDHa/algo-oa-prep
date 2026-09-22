"""Maximum Possible Racers — https://www.fastprep.io/problems/amazon-maximum-possible-racers

Write-up & approaches: ../../docs/problems/amazon_oa/amazon-maximum-possible-racers.md

$23

  uv run python amazon_oa/amazon-maximum-possible-racers/solution.py   # debug one case (see CASE below)
  uv run pytest amazon_oa/amazon-maximum-possible-racers/              # run the test sets
"""

from harness import NotSolved, pick_case


class Solution:
    def maximumPossibleRacers(self, speed, k):
        """State the time and space complexity of your approach, and explain why.

        Time:  O(?):
        Space: O(?):
        """
        raise NotSolved


if __name__ == "__main__":
    # Debug playground: set a breakpoint in maximumPossibleRacers above, then run this file.
    # Pick a case by id (ids are in cases.json).
    CASE = "example_1"
    case = pick_case(__file__, CASE)
    result = Solution().maximumPossibleRacers(*case["args"])
    print(f"case {case['id']}: args = {case['args']}")
    print(f"expected: {case['expected']}")
    print(f"got:      {result}")
