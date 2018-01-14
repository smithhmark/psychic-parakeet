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

    def _offset(self, x, y):
        return y * self._symbolcnt + x
    def at(self, x, y):
        return self._board[self._offset(x, y)]

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

    def _indices_to_check(self, x, y):
        iis = set()
        iis.update(self._indices_for_row(y))
        iis.update(self._indices_for_col(x))
        #box
        box_x = x // self._basenum
        box_y = y // self._basenum
        iis.update(self._indices_for_box(box_x, box_y))
        return iis
