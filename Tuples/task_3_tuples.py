
def convert_to_tuples_without_city(text):
    new_tuples = tuple(text.split())
    if 'Ульяновск' in new_tuples:
        list_tuples = list(new_tuples)
        upgrade_list = list_tuples.remove('Ульяновск')
        my_tuple = tuple(list_tuples)
        return ' '.join(my_tuple)
    return ' '.join(new_tuples)

def test_convert_to_tuples_without_city():
    assert convert_to_tuples_without_city('Ульяновск Москва') == 'Москва'
    assert convert_to_tuples_without_city('Ульяновск Москва Уфа') == 'Москва Уфа'
    assert convert_to_tuples_without_city('Ульяновск Уфа Москва') == 'Уфа Москва'
    assert convert_to_tuples_without_city('Ульяновск Уфа Москва Уфа') == 'Уфа Москва Уфа'
    assert convert_to_tuples_without_city('Ульяновск Уфа Москва Уфа Ульяновск') == 'Уфа Москва Уфа Ульяновск'

