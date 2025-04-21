
def unique(collection):
    seen = set()
    unique_items = []
    for item in collection:
        if item not in seen:
            seen.add(item)
            unique_items.append(item)
    return unique_items

def get_same_count(list1,list2):
    if len(list1) == 0 or len(list2) == 0:
        return 0
    list1 = unique(list1)
    list2 = unique(list2)
    same = []
    for item in list1:
        if item in list2:
            same.append(item)
    for item in list2:
        if item in list1:
            if item not in same:
                same.append(item)
    return len(same)


def test_get_same_count():
    assert get_same_count([], []) == 0
    assert get_same_count([1, 2], []) == 0
    assert get_same_count([0], ['one', 'two']) == 0
    assert get_same_count([5, 3, 3], ['one', 'two']) == 0
    assert get_same_count([1, 2, 3], [2, 8, 10]) == 1
    assert get_same_count([1, 8, 2, 3], [2, 8, 10]) == 2
    assert get_same_count([1, 3, 2, 2], [3, 1, 1, 2]) == 3
    assert get_same_count([1, 1, 1, 2, 3], [1, 1]) == 1
    assert get_same_count([1, 1, 2, 3], [2, 3]) == 2


