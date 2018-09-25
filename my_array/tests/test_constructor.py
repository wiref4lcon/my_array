from .. import Array

def test_boolean_list():
    a_list = [False, True, True]
    arr = Array(a_list)
    assert arr.dtype == 'b'