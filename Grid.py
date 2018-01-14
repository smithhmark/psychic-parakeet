from math import sqrt

class Grid():
    def __init__(self, symbolcnt=9, board=None):
        self._symbols = {x for x in range(symbolcnt)}
        self._symbolcnt = symbolcnt
        self._basenum = int(sqrt(symbolcnt))
        if self._basenum ** 2 != symbolcnt:
            raise ValueError("symbolcnt must be a perfect square")

        if board is None:
            self._board = [None for unused in range(symbolcnt**2)]
        else:
            allowed = set()
            allowed.add(None)
            allowed.update(self._symbols)
            #allowed = {None}.update(self._symbols)

            for ii, pos in enumerate(board):
                if pos not in allowed:
                    raise ValueError("board cannot contain symbols outside"
                      + repr(allowed))
            if len(board) != self._symbolcnt ** 2:
                raise ValueError(
                  "board must be a square exactly symbolcnt on a side")
            self._board = board[:]
            self._orig_board = board[:]
        self._populate_uncertainties()

    def _offset(self, x, y):
        return y * self._symbolcnt + x

    def at(self, x, y):
        return self._board[self._offset(x, y)]

    def set(self, x, y, val):
        if val not in self._symbols:
            raise ValueError("value must be a known symbol")
        self._board[self._offset(x,y)] = val

    def _indices_for_box(self, x, y):
        iis = []
        for ri in range(self._basenum): #ros
            for ci in range(self._basenum): #col
                iis.append(self._offset(x*self._basenum + ci, y*self._basenum + ri))
        return iis

    def _indices_for_col(self, col):
        iis = []
        for ci in range(self._symbolcnt):
            iis.append(self._offset(col, ci))
        return iis

    def _indices_for_row(self, row):
        iis = []
        start = self._offset(0, row)
        stop = self._offset(self._symbolcnt, row)
        for ri in range(start, stop):
            iis.append(ri)
        return iis

    def _indices_to_check(self, x, y, all=True):
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

    def _index_to_coord(self, idx):
        y, x = divmod(idx, self._symbolcnt)
        return x, y

    def _populate_uncertainties(self):
        asserted = [(ii, sym) for ii, sym in enumerate(self._board) 
                if sym is not None]

        cant_haves = [set() for unused in self._board]
        #cant_haves = [set() for unused in range(len(self._board))]
        self._uncertainty = [None for unused in self._board]
        #self._uncertainty = [None for unused in range(len(self._board))]
        for loc, val in asserted:
            pt = self._index_to_coord(loc)
            for index in self._indices_to_check(pt[0], pt[1], False):
                cant_haves[index].add(val)
        for ii, nopes in enumerate(cant_haves):
            if self._board[ii] is None:
                self._uncertainty[ii] = self._symbols - nopes

    def _update_state(self):
        discoveries = 0
        for ii, maybes in enumerate(self._uncertainty):
            if maybes is not None and len(maybes) == 1:
                self._board[ii] = maybes.pop()
                discoveries += 1
        if discoveries > 0:
            self._populate_uncertainties()

        return discoveries
