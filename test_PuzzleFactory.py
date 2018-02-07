import pytest

import PuzzleFactory

@pytest.fixture
def factory():
    return PuzzleFactory.PuzzleFactory()

def test_easy(factory, simple_puzzle):
    puzzle = factory.easy()
    diffs = 0
    for e, s in zip(puzzle._board, simple_puzzle):
        if e != s:
            diffs += 1
    assert diffs == 0

def test_hard(factory, hard_puzzle):
    puzzle = factory.hard()
    diffs = 0
    for h, s in zip(puzzle._board, hard_puzzle):
        if h != s:
            diffs += 1
    assert diffs == 0
