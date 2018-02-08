import pytest

import PuzzleFactory

@pytest.fixture
def factory():
    return PuzzleFactory.PuzzleFactory()

def test_easy(factory, simple_puzzle_data):
    puzzle = factory.easy()
    diffs = 0
    for e, s in zip(puzzle._st._st, simple_puzzle_data):
        if e != s:
            diffs += 1
    assert diffs == 0

def test_hard(factory, hard_puzzle_data):
    puzzle = factory.hard()
    diffs = 0
    for h, s in zip(puzzle._st._st, hard_puzzle_data):
        if h != s:
            diffs += 1
    assert diffs == 0
