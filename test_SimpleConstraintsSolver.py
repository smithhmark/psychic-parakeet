from pytest import fixture

import State
import Scaler
import SimpleContraintsSolver

@fixture
def symbols():
    return {i for i in range(9)}

@fixture
def base_scaler(symbols):
    return Scaler.Scaler(len(symbols))

@fixture
def empty_state(symbols, base_scaler):
    return State.State(symbols, base_scaler)

@fixture
def easy_state(symbols, base_scaler, simple_puzzle_data):
    return State.State(symbols, base_scaler, simple_puzzle_data)

@fixture
def SCSolver():
    return SimpleContraintsSolver.SimpleContraintsSolver()

def test_update_uncertainty(empty_state, SCSolver):
    expected_uncertainty = [empty_state._symbols.copy() for ii in range(81)]
    SCSolver._populate_uncertainties(empty_state)
    assert SCSolver._uncertainty == expected_uncertainty

    sym = 0
    empty_state.set(0,0,sym)
    SCSolver._populate_uncertainties(empty_state)

    for ii in empty_state._scaler.locs_to_check(0,0):
        expected_uncertainty[ii].remove(sym)
    expected_uncertainty[0] = None
    assert SCSolver._uncertainty == expected_uncertainty

def test_one_step(easy_state, SCSolver):
    expected = (1, 2, "an explanation")
    result = SCSolver.one_step(easy_state)
    assert result[0] == expected[0]
    assert result[1] == expected[1]

def test_update_state_once(easy_state, SCSolver):
    orig = easy_state.clone()
    SCSolver._populate_uncertainties(easy_state)
    discovered = SCSolver._update_state_once(easy_state)

    #print(len(discovered))
    #print(discovered)
    #print(easy_state.stringify())
    assert easy_state.at(4,4) == 7
    changes = 0
    for ii, ov in enumerate(orig._st):
        if ov != easy_state._st[ii]:
            changes += 1
    assert len(discovered) == changes

def test_solve(SCSolver, easy_state, simple_puzzle_answer):
    orig = easy_state.clone()
    unknowns = 0
    for kk, pp in zip(simple_puzzle_answer, easy_state._st):
        if kk != pp:
            unknowns += 1
    discovered = SCSolver.solve(easy_state)
    errors = 0
    #print(easy_state._st)
    for ii, ov in enumerate(easy_state._st):
        if ov != simple_puzzle_answer[ii]:
            errors += 1
    assert errors == 0
    assert len(discovered) == unknowns
