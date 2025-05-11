

def str_to_dict(s):
    pairs = s.split()  # ['one=1', 'two=2', 'three=3']
    d = {}
    for pair in pairs:
        key, value = pair.split('=')
        d[key] = int(value)
    return d

def test_str_to_dict():
    result_dict = str_to_dict(s='one=1 two=2 three=3')
    result_list = sorted(result_dict.items())
    result_str = ' '.join(str(x) for x in result_list)
    assert result_str == "('one', 1) ('three', 3) ('two', 2)"

