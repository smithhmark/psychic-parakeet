import pytest

import canned_puzzles

# the following simple puzzle and its answer is from:
#  http://elmo.sbs.arizona.edu/sandiway/sudoku/examples.html
@pytest.fixture(scope='module')
def simple_puzzle_data():
    return canned_puzzles.easy_1()

@pytest.fixture(scope='module')
def simple_puzzle_answer():
    return canned_puzzles.easy_1_answer()

@pytest.fixture(scope='module')
def hard_puzzle_data():
    return canned_puzzles.hard_1()

@pytest.fixture(scope='module')
def hard_puzzle_answer():
    return canned_puzzles.hard_1_answer()
