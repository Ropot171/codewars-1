t = (3.4, -56.7)

def create_new_tuple(text):
    convert_str_to_tuple = tuple(map(int, text.split()))
    result = t + convert_str_to_tuple
    return result

def test_create_new_tuple():
    text = '8 11 -5 2'
    assert create_new_tuple(text) == (3.4, -56.7, 8, 11, -5, 2)
    assert create_new_tuple('1 2 3 4 5') == (3.4, -56.7, 1, 2, 3, 4, 5)
    assert create_new_tuple('1 2 3 4 5 6 7 8 9 10') == (3.4, -56.7, 1, 2, 3,
                                                        4, 5, 6, 7, 8, 9, 10)


