import pytest
from unittest.mock import Mock

import Puzzle

@pytest.fixture
def empty_grid():
    return Puzzle.Puzzle()

def test_standard_constructor(empty_grid):
    assert len(empty_grid._symbols) == 9
    assert empty_grid._symbols == {x for x in range(9)}
    assert len(empty_grid._board) == 9 * 9
    for pos in empty_grid._board:
        assert pos is None

def test_set(empty_grid):
    assert empty_grid._board[0] == None
    empty_grid.set(0,0,0)
    assert empty_grid._board[0] == 0
    with pytest.raises(ValueError):
        empty_grid.set(0,0,'A')
    with pytest.raises(ValueError):
        empty_grid.set(0,0,10)
    ret = empty_grid.set(0,0,1)
    assert ret is None
    ret = empty_grid.set(1,0,1)
    assert ret == (0,0)


def test_offset_calculation_sz2():
    g = Puzzle.Puzzle()
    g._symbolcnt = 2
    g._board = list(range(4))

    assert g._offset(0,0) == 0
    assert g.at(0,0) == 0
    assert g._offset(1,0) == 1
    assert g.at(1,0) == 1
    assert g._offset(0,1) == 2
    assert g.at(0,1) == 2
    assert g._offset(1,1) == 3
    assert g.at(1,1) == 3


@pytest.fixture
def simple_grid_puzzle(simple_puzzle):
    return Puzzle.Puzzle(9,simple_puzzle)

@pytest.fixture
def simple_grid_complete(simple_puzzle_answer):
    return Puzzle.Puzzle(9,simple_puzzle_answer)

def no_test_sz2_constructort():
    board = [0,1,1,0]
    g = Puzzle.Puzzle(2, board)
    assert g._symbolcnt == 2
    assert g._board == board

def test_simple_puzzle(simple_grid_puzzle):
    assert simple_grid_puzzle._symbolcnt == 9
    assert simple_grid_puzzle.at(0,0) == None
    assert simple_grid_puzzle.at(7,5) == 1

def test_indices_for_box(empty_grid):
    assert empty_grid._indices_for_box(1,0) == [3,4,5, 12,13,14, 21,22,23]
    assert empty_grid._indices_for_box(0,1) == [27,28,29, 36,37,38, 45,46,47]

def test_indices_for_row(empty_grid):
    assert empty_grid._indices_for_row(0) == list(range(9))
    assert empty_grid._indices_for_row(1) == list(range(9, 18))

def test_indices_for_col(empty_grid):
    assert empty_grid._indices_for_col(0) == list(range(0,81,9))
    assert empty_grid._indices_for_col(1) == list(range(1,81,9))

def test_indices_to_check(empty_grid):
    x, y = 4, 1
    expected = set([3,4,5, 12,13,14, 21,22,23])
    expected.update(range(9,18))
    expected.update(range(4, 81, 9))
    assert empty_grid._indices_to_check(x, y) == expected

def test_update_uncertainty(empty_grid):
    expected_uncertainty = [empty_grid._symbols.copy() for ii in range(81)]
    expected_board = [None] * 81
    assert empty_grid._uncertainty == expected_uncertainty
    assert empty_grid._board == expected_board

    sym = 0
    empty_grid.set(0,0,sym)
    assert empty_grid._board[0] == 0
    assert empty_grid._board[1] == None
    empty_grid._populate_uncertainties()

    for ii in empty_grid._indices_to_check(0,0):
        expected_uncertainty[ii].remove(sym)
    expected_uncertainty[0] = None
    assert empty_grid._uncertainty == expected_uncertainty


def test_update_state_once(simple_grid_puzzle):
    discovered = simple_grid_puzzle._update_state_once()
    assert simple_grid_puzzle.at(4,4) == 7
    changes = 0
    for ii, ov in enumerate(simple_grid_puzzle._orig_board):
        if ov != simple_grid_puzzle._board[ii]:
            changes += 1
    assert discovered == changes

def test_update_state(simple_grid_puzzle, simple_puzzle_answer):
    cycles = simple_grid_puzzle._update_state()
    diffs = 0
    print(simple_grid_puzzle._board)
    for ii, ov in enumerate(simple_grid_puzzle._board):
        if ov != simple_puzzle_answer[ii]:
            diffs += 1
    assert diffs == 0
    assert cycles == 5

def test_solved(empty_grid,simple_grid_puzzle,simple_grid_complete):
    assert empty_grid.solved() == False
    assert simple_grid_puzzle.solved() == False
    assert simple_grid_complete.solved() == True
