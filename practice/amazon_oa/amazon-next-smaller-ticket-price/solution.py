"""Next Smaller Ticket Price — https://www.fastprep.io/problems/amazon-next-smaller-ticket-price

Write-up & approaches: ../../docs/problems/amazon_oa/amazon-next-smaller-ticket-price.md

You are given an integer array prices, where prices[i] is the price of ticket i.For each ticket, find the next strictly smaller price to its right. If no later ticket is cheaper, the answer for that t

  uv run python amazon_oa/amazon-next-smaller-ticket-price/solution.py   # debug one case (see CASE below)
  uv run pytest amazon_oa/amazon-next-smaller-ticket-price/              # run the test sets
"""

from harness import NotSolved, pick_case


class Solution:
    def nextSmallerPrices(self, prices):
        """State the time and space complexity of your approach, and explain why.

        Time:  O(?):
        Space: O(?):
        """
        raise NotSolved


if __name__ == "__main__":
    # Debug playground: set a breakpoint in nextSmallerPrices above, then run this file.
    # Pick a case by id (ids are in cases.json).
    CASE = "example_1"
    case = pick_case(__file__, CASE)
    result = Solution().nextSmallerPrices(*case["args"])
    print(f"case {case['id']}: args = {case['args']}")
    print(f"expected: {case['expected']}")
    print(f"got:      {result}")
