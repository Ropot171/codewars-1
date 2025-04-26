def get_intersection_of_sorted_lists(list1, list2):
    finish_list = []

    for symbol in list1:
        if symbol in list2:
            if symbol not in finish_list:
                finish_list.append(symbol)
    return finish_list

def test_get_intersection_of_sorted_lists():
    assert get_intersection_of_sorted_lists([], []) == []
    assert get_intersection_of_sorted_lists([1], []) == []
    assert get_intersection_of_sorted_lists([], [2]) == []

    assert get_intersection_of_sorted_lists(
        [10, 11, 24],
        [-2, 3, 4]
        ) == []

    assert get_intersection_of_sorted_lists(
        [10, 11, 24],
        [10, 13, 14, 18, 24, 30]
        ) == [10, 24]

    assert get_intersection_of_sorted_lists(
        [3, 5, 10],
        [10, 12, 19, 21]
        ) == [10]

    assert get_intersection_of_sorted_lists(
        [10, 12, 19, 21],
        [3, 5, 10]
        ) == [10]

    assert get_intersection_of_sorted_lists(
        [10, 13, 14, 18, 24, 30],
        [10, 11, 24]
        ) == [10, 24]

    assert get_intersection_of_sorted_lists(
        [10, 11, 24, 30],
        [10, 13, 14, 18, 24, 30]
        ) == [10, 24, 30]

    assert get_intersection_of_sorted_lists(
        [10, 11, 14, 18, 24, 30],
        [10, 13, 14, 18, 24, 30],
    ) == [10, 14, 18, 24, 30]

    assert get_intersection_of_sorted_lists(
        [1, 1, 1, 2, 2, 2],
        [1, 1, 2, 2, 3, 3]
    ) == [1, 2]




s = 'ABRAKADABRA'
print(s[5:2:-1])
