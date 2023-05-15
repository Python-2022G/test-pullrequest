from main import func

def test_func():
    assert func(1, 2) == 3
    assert func(1, 1) == 2
    assert func(1, 0) == 1
    assert func(1, -1) == 0
    assert func(1, -2) == -1
    assert func(1, -3) == -2
    assert func(1, -4) == -3
    assert func(1, -5) == -4