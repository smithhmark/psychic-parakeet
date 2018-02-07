import Puzzle

import canned_puzzles

class PuzzleFactory:
    def easy(self):
        """build a Puzzle that is easy to solve.
        """
        return Puzzle.Puzzle(9,canned_puzzles.easy_1())

    def hard(self):
        """Build a puzzle that is needs more than the simplest constraint 
        checking to solve.
        """
        return Puzzle.Puzzle(9,canned_puzzles.hard_1())
