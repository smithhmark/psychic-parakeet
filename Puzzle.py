from math import sqrt

from Scaler import Scaler
import State
from SimpleContraintsSolver import SimpleContraintsSolver as SCS

class Puzzle():
    def __init__(self, symbolcnt=9, board=None):
        self._symbols = {x for x in range(symbolcnt)}
        self._symbolcnt = symbolcnt
        self._basenum = int(sqrt(symbolcnt))
        self._scaler = Scaler(symbolcnt)

        if self._basenum ** 2 != symbolcnt:
            raise ValueError("symbolcnt must be a perfect square")

        self._st = State.State(self._symbols, self._scaler, board)
        self._orig = self._st.clone()
        self._solvers = {"simple": SCS()}

    def at(self, x, y):
        return self._st.at(x, y)

    def set(self, x, y, val):
        """updates the grid at <x>,<y> to be <val>
        if that update would create a conflict, it returns the x,y of the
        conflicting location.
        """
        return self._st.set(x,y,val)

    def solved(self):
        """return True if there are no unpopulated cells
        """
        return self._st.solved()
        for ii in self._board:
            if ii is None:
                return False
        return True

