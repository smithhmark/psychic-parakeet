import pytest
from unittest.mock import Mock

import Grid

def test_grid():
    assert Grid.grid == "grid"

@pytest.fixture
def empty_grid():
    return Grid.Grid()

def test_standard_constructor(empty_grid):
    assert len(empty_grid._symbols) == 9
    assert empty_grid._symbols == {x for x in range(9)}
    assert len(empty_grid._board) == 9 * 9
    for pos in empty_grid._board:
        assert pos is None

def test_offset_calculation_sz2():
    g = Grid.Grid()
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
def simple_puzzle():
    data = [ None,None,None, 1,5,None, 6,None,0,
            5,7,None,  None,6,None, None,8,None,
            0,8,None,  None,None,3,  4,None,None,
            7,1,None,  0,None,None,  None,3,None,
            None,None,3,  5,None,1,  8,None,None,
            None,4,None,  None,None,2,  None,1,7,
            None,None,8,  2,None,None,  None,6,3,
            None,3,None, None,4,None,  None,2,5,
            6,None,2,  None,0,7, None,None,None]
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
    return list(map(lambda k: k+1, rawdata))

@pytest.fixture
def simple_grid_puzzle(simple_puzzle):
    return Grid.Grid(9,simple_puzzle)

@pytest.fixture
def simple_grid_complete(simple_puzzle_answer):
    return Grid.Grid(9,simple_puzzle_answer)

def test_sz2_constructort():
    board = [0,1,1,0]
    g = Grid.Grid(2, board)

    assert g._symbolcnt == 2
    assert g._board == board

def test_simple_puzzle(simple_grid_puzzle):
    assert simple_grid_puzzle._symbolcnt == 9
    assert simple_grid_puzzle.at(0,0) == None
    assert simple_grid_puzzle.at(7,5) == 1

