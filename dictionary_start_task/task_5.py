def numbers_read(number):
    my_list = number.split()
    unique_dict = {x: True for x in my_list}
    unique_values = list(unique_dict.keys())
    string = ''
    for el in unique_values:
        string += el + ' '
    return string.strip()

def test_number_read():
    assert numbers_read('8 11 -4 5 2 11 4 8') == '8 11 -4 5 2 4'
    assert numbers_read('1 2 3 4 5 6 7 8 9 10') == '1 2 3 4 5 6 7 8 9 10'

