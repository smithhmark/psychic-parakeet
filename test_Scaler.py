import pytest
from unittest.mock import Mock

import Scaler

@pytest.fixture
def default_scaler():
    return Scaler.Scaler(9)

@pytest.fixture
def small_scaler():
    return Scaler.Scaler(2)

def test_indices_for_box(default_scaler):
    assert default_scaler._indices_for_box(1,0) == [3,4,5, 12,13,14, 21,22,23]
    assert default_scaler._indices_for_box(0,1) == [27,28,29, 36,37,38, 45,46,47]

def test_indices_for_row(default_scaler):
    assert default_scaler._indices_for_row(0) == list(range(9))
    assert default_scaler._indices_for_row(1) == list(range(9, 18))

def test_indices_for_col(default_scaler):
    assert default_scaler._indices_for_col(0) == list(range(0,81,9))
    assert default_scaler._indices_for_col(1) == list(range(1,81,9))

def test_indices_to_check(default_scaler):
    x, y = 4, 1
    expected = set([3,4,5, 12,13,14, 21,22,23])
    expected.update(range(9,18))
    expected.update(range(4, 81, 9))
    assert default_scaler.locs_to_check(x, y, False) == expected

def test_coord_to_idx(small_scaler):
    assert small_scaler.coord_to_idx(0,0) == 0
    assert small_scaler.coord_to_idx(1,0) == 1
    assert small_scaler.coord_to_idx(0,1) == 2
    assert small_scaler.coord_to_idx(1,1) == 3
    #assert small_scaler.at(1,1) == 3
    #assert small_scaler.at(0,1) == 2
    #assert small_scaler.at(0,0) == 0
    #assert small_scaler.at(1,0) == 1
