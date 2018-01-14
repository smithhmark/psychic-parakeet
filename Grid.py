
class Grid():
    def __init__(self, symbolcnt=9, board=None):
        self._symbols = {x for x in range(symbolcnt)}
        self._symbolcnt = symbolcnt
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
