from pytest import fixture

import Scaler

import State

@fixture
def symbols():
    return [i for i in range(9)]

@fixture
def base_scaler(symbols):
    return Scaler.Scaler(len(symbols))

def test_clone(symbols, base_scaler):
    st = State.State(symbols, base_scaler)
    st2 = st.clone()
    assert id(st) != id(st2)
    assert id(st._st) != id(st2._st)
    assert id(st._scaler) == id(st2._scaler)
    assert id(st._symbols) == id(st2._symbols)
