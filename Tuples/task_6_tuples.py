def create_unique_tuple_and_return_index(text):
    items = text.split()
    create_tuple = tuple(items)
    counts = {}
    result = []

    for item in create_tuple:
        counts[item] = counts.get(item, 0) + 1

    for i, item in enumerate(create_tuple):
        if counts[item] > 1:
            result.append(str(i))

    return ' '.join(result)


def test_create_unique_tuple_and_return_index():
        assert create_unique_tuple_and_return_index('5 4 -3 2 4 5 10 11') == '0 1 4 5'
