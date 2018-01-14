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

def test_sz2_constructort():
    board = [0,1,1,0]
    g = Grid.Grid(2, board)

    assert g._symbolcnt == 2
    assert g._board == board

