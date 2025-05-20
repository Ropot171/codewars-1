def highlighting_parts_of_names(text):
    new_tuples = tuple(text.split())
    my_list = list(new_tuples)
    lower_names = [name.lower() for name in my_list]
    new_list = []
    for name in lower_names:
        if name[:2] ==  "ва":
            new_list.append(name)
    return ' '.join(new_list)

def test_highlighting_parts_of_names():
    assert highlighting_parts_of_names('Петя Варвара Венера Василиса Василий Федор') == 'варвара василиса василий'

