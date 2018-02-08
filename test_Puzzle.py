import pytest
from unittest.mock import Mock

import Puzzle

@pytest.fixture
def empty_puzzle():
    return Puzzle.Puzzle()

@pytest.fixture
def easy_puzzle(simple_puzzle_data):
    return Puzzle.Puzzle(9, simple_puzzle_data)

@pytest.fixture
def easy_puzzle_complete(simple_puzzle_answer):
    return Puzzle.Puzzle(9, simple_puzzle_answer)

def test_standard_constructor(empty_puzzle):
    assert len(empty_puzzle._symbols) == 9
    assert empty_puzzle._symbols == {x for x in range(9)}
    assert empty_puzzle._st._len == 9 * 9
    for pos in empty_puzzle._st._st:
        assert pos is None

def test_set(empty_puzzle):
    assert empty_puzzle.at(0,0) == None
    empty_puzzle.set(0,0,0)
    assert empty_puzzle.at(0,0) == 0

    with pytest.raises(ValueError):
        empty_puzzle.set(0,0,'A')
    with pytest.raises(ValueError):
        empty_puzzle.set(0,0,10)

    ret = empty_puzzle.set(0,0,1)
    assert ret is None

    ret = empty_puzzle.set(1,0,1)
    assert ret == (0,0)


def no_test_sz2_constructort():
    board = [0,1,1,0]
    g = Puzzle.Puzzle(2, board)
    assert g._symbolcnt == 2
    assert g._st._st == board

def test_simple_puzzle(easy_puzzle):
    assert easy_puzzle._symbolcnt == 9
    assert easy_puzzle.at(0,0) == None
    assert easy_puzzle.at(7,5) == 1


def test_solved(empty_puzzle, easy_puzzle, easy_puzzle_complete):
    assert empty_puzzle.solved() == False
    assert easy_puzzle.solved() == False
    assert easy_puzzle_complete.solved() == True
