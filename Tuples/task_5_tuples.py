def create_unique_tuple(text):
    create_tuple = tuple(text.split())
    seen = set()
    result = []
    for item in create_tuple:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return ' '.join(result)


def test_create_unique_tuple():
    assert create_unique_tuple('Москва Москва Москва Москва') == 'Москва'
    assert create_unique_tuple('8 11 -5 -2 8 11 -5') == '8 11 -5 -2'