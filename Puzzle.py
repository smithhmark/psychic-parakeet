from math import sqrt

from Scaler import Scaler
import State

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
        self._populate_uncertainties()

    def mv_offset(self, x, y):
        return y * self._symbolcnt + x

    def at(self, x, y):
        return self._st.at(x, y)

    def set(self, x, y, val):
        """updates the grid at <x>,<y> to be <val>
        if that update would create a conflict, it returns the x,y of the
        conflicting location.
        """
        return self._st.set(x,y,val)

    def rm_indices_for_box(self, x, y):
        iis = []
        for ri in range(self._basenum): #ros
            for ci in range(self._basenum): #col
                iis.append(self._offset(x*self._basenum + ci, y*self._basenum + ri))
        return iis

    def rm_indices_for_col(self, col):
        iis = []
        for ci in range(self._symbolcnt):
            iis.append(self._offset(col, ci))
        return iis

    def rm_indices_for_row(self, row):
        iis = []
        start = self._offset(0, row)
        stop = self._offset(self._symbolcnt, row)
        for ri in range(start, stop):
            iis.append(ri)
        return iis

    def rm_indices_to_check(self, x, y, all=True):
        """produces a set of indices into _board that have impact on given 
        coordinate.
        """
        return self._scaler.locs_to_check(x,y,not all)

        iis = set()
        iis.update(self._indices_for_row(y))
        iis.update(self._indices_for_col(x))
        #box
        box_x = x // self._basenum
        box_y = y // self._basenum
        iis.update(self._indices_for_box(box_x, box_y))
        if not all:
            iis.remove(self._offset(x, y))
        return iis

    def _populate_uncertainties(self):
        asserted = [(ii, sym) for ii, sym in enumerate(self._st._st) 
                if sym is not None]

        cant_haves = [set() for unused in self._st._st]
        self._uncertainty = [None for unused in self._st._st]
        for loc, val in asserted:
            for index in self._scaler.locs_to_check_by_indx(loc, True):
                cant_haves[index].add(val)
        for ii, nopes in enumerate(cant_haves):
            if self._st._st[ii] is None:
                self._uncertainty[ii] = self._symbols - nopes

    def _update_state_once(self):
        discoveries = 0
        for ii, maybes in enumerate(self._uncertainty):
            if maybes is not None and len(maybes) == 1:
                self._st._st[ii] = maybes.pop()
                discoveries += 1
        if discoveries > 0:
            self._populate_uncertainties()
        return discoveries

    def _update_state(self):
        """continuously applies _update_state_once until no further changes are made.
        returns the number of times _update_state_once is called
        """
        cycles = 0
        changes = self._update_state_once()
        while changes > 0:
            cycles += 1
            changes = self._update_state_once()
        return cycles

    def solved(self):
        """return True if there are no unpopulated cells
        """
        return self._st.solved()
        for ii in self._board:
            if ii is None:
                return False
        return True

