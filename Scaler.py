from math import sqrt

class Scaler:
    """Base class of strategy object that understands mapping puzzle x-y space 
    to State's location-based view of data

    assumes a square puzzle
    """
    def __init__(self, numsymbols):
        self._symbolcnt = numsymbols
        self._basenum = int(sqrt(numsymbols))

    def coord_to_idx(self, x, y):
        return y * self._symbolcnt + x

    def idx_to_coord(self, idx):
        y, x = divmod(idx, self._symbolcnt)
        return x, y

    def _indices_for_box(self, x, y):
        boxidxs = []
        for ri in range(self._basenum): #ros
            for ci in range(self._basenum): #col
                boxidxs.append(
                  self.coord_to_idx(
                      x*self._basenum + ci,
                      y*self._basenum + ri))
        return boxidxs
    
    def _indices_for_row(self, row):
        rowindxs = []
        start = self.coord_to_idx(0, row)
        stop = self.coord_to_idx(self._symbolcnt, row)
        for ri in range(start, stop):
            rowindxs.append(ri)
        return rowindxs

    def _indices_for_col(self, col):
        colidxs = []
        for ci in range(self._symbolcnt):
            colidxs.append(self.coord_to_idx(col, ci))
        return colidxs

    def locs_to_check(self, x, y, exclude_target=False):
        """produces a set of indices into _board that have impact on given 
        coordinate.

        by default includes the location at (x,y)
        """
        col = x
        row =  y

        iis = set()
        iis.update(self._indices_for_row(row))
        iis.update(self._indices_for_col(col))
        #box
        box_x = x // self._basenum
        box_y = y // self._basenum
        iis.update(self._indices_for_box(box_x, box_y))

        if exclude_target:
            iis.remove(self.coord_to_idx(x, y))
        return iis

    def locs_to_check_by_indx(self, idx, exclude_target=False):
        x, y = self.idx_to_coord(idx)
        return self.locs_to_check(x, y, exclude_target)

