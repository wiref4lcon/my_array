from .. import Array    #-Relative import - going up one level

arr = Array([5, 8, -4])

def test_sum():
    assert arr.sum() == 9  

