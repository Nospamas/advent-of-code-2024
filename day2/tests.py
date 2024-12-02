from main import isSafe


def test_decreasing_safe():
    assert isSafe([7,6,4,2,1])

def test_increasing_safe():
    assert isSafe([1,3,6,7,9])

def test_big_increase_unsafe():
    assert not isSafe([1,2,7,8,9])

def test_big_decrease_unsafe():
    assert not isSafe([9,7,6,2,1])

def test_decrease_after_increase_unsafe():
    assert not isSafe([1,3,2,4,5])

def test_increase_after_decrease_unsafe():
    assert not isSafe([5,4,2,3,1])

def test_no_change_unsafe():
    assert not isSafe([8,6,4,4,1])