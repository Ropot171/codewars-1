def rotated_left(text):
    return text[1:] + text[:1]

def rotated_right(text):
    return text[-1:] + text[:-1]

def test_rotated_right1():
    source = [1, 2, 3, 4]
    result = rotated_right(source)
    assert result is not source, "Function should return a new list!"
    assert source == [1, 2, 3, 4], "Function shouldn't change the source list!"
    assert result == [4, 1, 2, 3]


def test_rotated_right2():
    source = ['one', 'two', 1, 2, 'A', 'B']
    result = rotated_right(source)
    assert result is not source, "Function should return a new list!"
    assert source == ['one', 'two', 1, 2, 'A', 'B'], "Function shouldn't change the source list!"  # noqa: E501
    assert result == ['B', 'one', 'two', 1, 2, 'A']


def test_rotated_left1():
    source = "ABCD"
    result = rotated_left(source)
    assert result == "BCDA"


def test_rotated_left2():
    source = "ABCDefg"
    result = rotated_left(source)
    assert result == "BCDefgA"


def test_symmetricity():
    source = (1, True, "foo")
    result1 = rotated_right(rotated_left(source))
    assert result1 == source
    result2 = rotated_left(rotated_right(source))
    assert result2 == source
