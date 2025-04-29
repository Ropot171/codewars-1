def length_of_last_word(items):
    list_items = items.split()
    if not list_items:
        return 0
    elif len(list_items) == 1:
        return len(list_items[0])
    else:
        return len(list_items[-1])



def test_length_of_last_word():
    assert length_of_last_word('') == 0
    assert length_of_last_word(' \t\n') == 0
    assert length_of_last_word('hi') == 2
    assert length_of_last_word('Hexlet, hi') == 2
    assert length_of_last_word('  cat') == 3
    assert length_of_last_word('man in black') == 5
    assert length_of_last_word('hello, world!') == 6
    assert length_of_last_word('hello, wOrLd!    ') == 6
    assert length_of_last_word('hello\t\nworld') == 5


