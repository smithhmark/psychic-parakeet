
grid = "grid"

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
                    raise ValueError("board cannot contain symbols outside"+ repr(allowed))
            if all(map(lambda pos: pos in allowed, board)):
              #and not any(map(lambda pos: pos not in allowed, board)):
                self._board = board[:]

            else:
                raise ValueError("board must be square, symbolcnt on a side, and not contain any symbols outside of the allowed range")

    def _offset(self, x, y):
        return y * self._symbolcnt + x
    def at(self, x, y):
        return self._board[self._offset(x, y)]
