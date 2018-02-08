


class State:
    def __init__(self, symbols, scaler, current=None):
        self._symbolcnt = len(symbols)
        self._scaler = scaler
        self._symbols = symbols
        self._len = len(symbols) ** 2

        if current is None:
            self._st = [None for unused in range(self._len)]
        else:
            if len(current) != self._len:
                raise ValueError(
                  "board must be a square exactly symbolcnt on a side")

            allowed = set()
            allowed.add(None)
            allowed.update(self._symbols)
            for ii, pos in enumerate(current):
                if pos not in allowed:
                    raise ValueError("current cannot contain symbols outside"
                      + repr(allowed))
            self._st = current[:]

    def clone(self):
        return State(self._symbols, self._scaler, self._st)

    def at(self, x, y):
        return self._st[self._scaler.coord_to_idx(x, y)]

    def set(self, x, y, val):
        """updates the grid at <x>,<y> to be <val>
        if that update would create a conflict, it returns the x,y of the
        conflicting location.
        """
        if val not in self._symbols:
            raise ValueError("value must be a known symbol")
        for idx in self._scaler.locs_to_check(x,y):
            if self._st[idx] == val:
               return self._scaler.idx_to_coord(idx)

        self._st[self._scaler.coord_to_idx(x,y)] = val

    def solved(self):
        """return True if there are no unpopulated cells
        """
        for ii in self._st:
            if ii is None:
                return False
        return True
