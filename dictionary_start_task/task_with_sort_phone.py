from unittest.mock import patch
import builtins

def str_to_dict_2():
    s = input().split()
    d = {}
    for pair in s:
        key, value = pair[:2], pair
        if key in d:
            d[key].append(value)
        else:
            d[key] = [value]
    return d


def test_str_to_dict_2():
    test_input = '+71234567890 +71234567854 +61234576890 +52134567890 +21235777890 +21234567110 +71232267890'
    expected_output = {
        '+7': ['+71234567890', '+71234567854', '+71232267890'],
        '+6': ['+61234576890'],
        '+5': ['+52134567890'],
        '+2': ['+21235777890', '+21234567110']
    }

    with patch.object(builtins, 'input', lambda: test_input):
        result = str_to_dict_2()
        assert result == expected_output, f"Expected {expected_output}, but got {result}"

test_str_to_dict_2()
print("Тест пройден успешно.")