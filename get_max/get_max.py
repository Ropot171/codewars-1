def get_max(text):
    if not text:
        return None

    first, *rest = text
    max_symbol = first

    for symbol in rest:
        if symbol > max_symbol:
            max_symbol = symbol

    return max_symbol

def test_get_max():
    assert get_max([]) is None
    assert get_max([1, 10, 8]) == 10
    assert get_max([11, -3, 8, 1]) == 11
    assert get_max([1, 8, -3, 11]) == 11


