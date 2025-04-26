def flatten(coll):
    if not coll:
        return []
    result = []
    for item in coll:
        if isinstance(item, list):
            result = [*result, *item]
        else:
            result = [*result, item]
    return result

def test_flatten():
    assert flatten([]) == []
    assert flatten([1, [3, 2], 9]) == [1, 3, 2, 9]
    assert flatten([[9, 8], [], [0], 10]) == [9, 8, 0, 10]
    assert flatten([1, [[2], [3]], [9]]) == [1, [2], [3], 9]
