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

# the following simple puzzle and its answer is from:
#  http://elmo.sbs.arizona.edu/sandiway/sudoku/examples.html
@pytest.fixture
def simple_puzzle():
    rawdata = [None,None,None,2,6,None,7,None,1,
            6,8,None,None,7,None,None,9,None,
            1,9,None,None,None,4,5,None,None,
            8,2,None,1,None,None,None,4,None,
            None,None,4,6,None,2,9,None,None,
            None,5,None,None,None,3,None,2,8,
            None,None,9,3,None,None,None,7,4,
            None,4,None,None,5,None,None,3,6,
            7,None,3,None,1,8,None,None,None,]
    data = []
    for ii in rawdata:
        if ii is None:
            data.append(ii)
        else:
            data.append(ii - 1)
    return data

@pytest.fixture
def simple_puzzle_answer():
    rawdata = [4,3,5,2,6,9,7,8,1,
            6,8,2,5,7,1,4,9,3,
            1,9,7,8,3,4,5,6,2,
            8,2,6,1,9,5,3,4,7,
            3,7,4,6,8,2,9,1,5,
            9,5,1,7,4,3,6,2,8,
            5,1,9,3,2,6,8,7,4,
            2,4,8,9,5,7,1,3,6,
            7,6,3,4,1,8,2,5,9,]
    return list(map(lambda k: k-1, rawdata))

@pytest.fixture
def hard_puzzle():
    """provides "Vegard Hanssen puzzle 2155141"
    """
    rawdata = [
        None,None,None, 6,None,None, 4,None,None,
        7,None,None, None,None,3, 6,None,None,
        None,None,None, None,9,1, None,8,None,

        None,None,None,None,None,None,None,None,None,
        None,5,None, 1,8,None, None,None,3,
        None,None,None, 3,None,6, None,4,5,

        None,4,None, 2,None,None, None,6,None,
        9,None,3, None,None,None, None,None,None,
        None,2,None, None,None,None, 1,None,None]
    data = []
    for ii in rawdata:
        if ii is None:
            data.append(ii)
        else:
            data.append(ii - 1)
    return data

def hard_puzzle_answer():
    rawdata = [
        5,8,1, 6,7,2, 4,3,9,
        7,9,2, 8,4,3, 6,5,1,
        3,6,4, 5,9,1, 7,8,2,

        4,3,8, 9,5,7, 2,1,6,
        2,5,6, 1,8,4, 9,7,3,
        1,7,9, 3,2,6, 8,4,5,

        8,4,5, 2,1,9, 3,6,7,
        9,1,3, 7,6,8, 5,2,4,
        6,2,7, 4,3,5, 1,9,8]
    return list(map(lambda k:k-1, rawdata))

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
