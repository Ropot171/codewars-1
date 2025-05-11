from collections import defaultdict


def collect_indexes(items):
    # result = {}
    result = defaultdict(list)

    for index, element in enumerate(items): # [(0, 'h'), (1, 'e'), (2, 'l'),  (3, 'l'), (4, 'o')]
        # if element not in result:
            # result[element] = [] # result = {'h': []}
        result[element].append(index) # result = {'h': [0]}
    return result


def test_collect_indexes():
    assert not collect_indexes([])
    assert collect_indexes([1]) == {1: [0]}
    assert collect_indexes([1, 2]) == {1: [0], 2: [1]}
    assert collect_indexes('lol') == {'l': [0, 2], 'o': [1]}
    assert collect_indexes('coco') == {'c': [0, 2], 'o': [1, 3]}