"""Tests for Best Time to Buy And Sell Stock With Cooldown — your attempt (solution.py) against cases.json.

The worked approaches live in ../../docs/problems/best_time_to_buy_and_sell_stock_with_cooldown.md.
"""

import pytest

from harness import NotSolved, load_solution

CASES = [
    {
        "id": 'example_1',
        "args": [
            [
                1,
                3,
                4,
                0,
                4,
            ],
        ],
        "expected": 6,
    },
    {
        "id": 'example_2',
        "args": [
            [
                1,
            ],
        ],
        "expected": 0,
    },
]

if len(CASES) == 0:
    pytest.skip("no cases parsed", allow_module_level=True)

solution = load_solution(__file__)


def _ids(cases):
    return [case["id"] for case in cases]


def _check(method, case):
    assert method(*case["args"]) == case["expected"]


@pytest.mark.parametrize("case", CASES, ids=_ids(CASES))
def test_solution(case):
    try:
        _check(solution.Solution().maxProfit, case)
    except NotSolved:
        pytest.skip("solution.py not implemented yet")
