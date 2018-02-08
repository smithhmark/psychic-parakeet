from Solver import Solver

class SimpleContraintsSolver(Solver):
    def __init__(self):
        self._uncertainty = []

    def _populate_uncertainties(self, state):
        asserted = [(ii, sym) for ii, sym in enumerate(state._st) 
                if sym is not None]

        cant_haves = [set() for unused in state._st]
        self._uncertainty = [None for unused in state._st]
        for loc, val in asserted:
            for index in state._scaler.locs_to_check_by_indx(loc, True):
                cant_haves[index].add(val)
        for ii, nopes in enumerate(cant_haves):
            if state._st[ii] is None:
                self._uncertainty[ii] = state._symbols - nopes

    def one_step(self, state):
        self._populate_uncertainties(state)
        changes = self._update_state_once(state)
        if len(changes) > 0:
            return changes[0]
        else:
            return[]

    def _update_state_once(self, state):
        discoveries = [] 
        for ii, maybes in enumerate(self._uncertainty):
            if maybes is not None and len(maybes) == 1:
                state._st[ii] = maybes.pop()
                discoveries.append(
                  (ii, state._st[ii], "conflicts with row/column/box"))
        #if len(discoveries) > 0:
        #    self._populate_uncertainties()
        return discoveries

    def solve(self, state):
        self._populate_uncertainties(state)
        changes = []
        new_changes = self._update_state_once(state)
        while new_changes:
            changes.extend(new_changes)
            self._populate_uncertainties(state)
            new_changes = self._update_state_once(state)
        return changes

