def convert_to_tuples_with_city(text):
    new_tuples = tuple(text.split())
    return_to_str = ' '.join(new_tuples)
    if 'Москва' not in new_tuples:
        return return_to_str + ' Москва'
    return return_to_str


def test_convert_to_tuples_with_city():
    assert convert_to_tuples_with_city('Уфа Казань Самара') == 'Уфа Казань Самара Москва'
    assert convert_to_tuples_with_city('Тверь Подольск Москва Тува') == 'Тверь Подольск Москва Тува'
    assert convert_to_tuples_with_city('Москва') == 'Москва'

