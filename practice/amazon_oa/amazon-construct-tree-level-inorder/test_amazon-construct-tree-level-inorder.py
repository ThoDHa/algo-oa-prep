"""Tests for Construct a Tree from Level-Order and Inorder Traversals — your attempt (solution.py) against cases.json.

The worked approaches live in ../../docs/problems/amazon_oa/amazon-construct-tree-level-inorder.md.
"""

import pytest

from harness import NotSolved, load_solution

CASES = [
    {
        "id": 'example_1',
        "args": [
            [
                3,
                9,
                20,
                15,
                7,
            ],
            [
                9,
                3,
                15,
                20,
                7,
            ],
        ],
        "expected": [
            3,
            9,
            20,
            None,
            None,
            15,
            7,
        ],
    },
    {
        "id": 'example_2',
        "args": [
            [
                1,
            ],
            [
                1,
            ],
        ],
        "expected": [
            1,
        ],
    },
    {
        "id": 'example_3',
        "args": [
            [
                1,
                2,
                3,
                4,
                5,
            ],
            [
                4,
                2,
                5,
                1,
                3,
            ],
        ],
        "expected": [
            1,
            2,
            3,
            4,
            5,
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
        _check(solution.Solution().buildTree, case)
    except NotSolved:
        pytest.skip("solution.py not implemented yet")
