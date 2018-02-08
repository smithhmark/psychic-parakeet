from pytest import fixture

import Scaler

import State

@fixture
def symbols():
    return [i for i in range(9)]

@fixture
def base_scaler(symbols):
    return Scaler.Scaler(len(symbols))

@fixture
def empty_state(symbols, base_scaler):
    st = State.State(symbols, base_scaler)
    return st

def test_clone(empty_state):
    st2 = empty_state.clone()
    assert id(empty_state) != id(st2)
    assert id(empty_state._st) != id(st2._st)
    assert id(empty_state._scaler) == id(st2._scaler)
    assert id(empty_state._symbols) == id(st2._symbols)

def test_stringify(empty_state):
    expected = ""
    for y in range(len(empty_state._symbols)):
        expected += " None," * len(empty_state._symbols)
        expected += "\n"
    assert empty_state.stringify() == expected
         
    expected = ""
    indent = 7
    for y in range(len(empty_state._symbols)):
        expected += " " * indent
        expected += " None," * len(empty_state._symbols)
        expected += "\n"
    assert empty_state.stringify(indent) == expected

