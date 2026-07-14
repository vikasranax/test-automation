def add(a, b):
    return a + b


def test_add_two_numbers():
    result = add(7, 3)
    assert result == 10


def test_add_negative_numbers():
    result = add(-1, -1)
    assert result == -2