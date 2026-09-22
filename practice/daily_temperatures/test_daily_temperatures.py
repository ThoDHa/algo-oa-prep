"""Tests for Daily Temperatures — your attempt (solution.py) against cases.json.

The worked approaches live in ../../docs/problems/daily_temperatures.md.
"""

import pytest

from harness import NotSolved, load_solution

CASES = [
    {
        "id": 'example_1',
        "args": [
            [
                30,
                38,
                30,
                36,
                35,
                40,
                28,
            ],
        ],
        "expected": [
            1,
            4,
            1,
            2,
            1,
            0,
            0,
        ],
    },
    {
        "id": 'example_2',
        "args": [
            [
                22,
                21,
                20,
            ],
        ],
        "expected": [
            0,
            0,
            0,
        ],
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
        _check(solution.Solution().dailyTemperatures, case)
    except NotSolved:
        pytest.skip("solution.py not implemented yet")
