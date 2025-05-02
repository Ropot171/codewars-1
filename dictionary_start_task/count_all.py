def count_all(text):
    dictionary_new = {}
    for i in text:
        if i not in dictionary_new:
            dictionary_new[i] = 1
        else:
            dictionary_new[i] += 1
    return dictionary_new

def test_count_empty():
    assert not count_all([])
    assert not count_all("")


def test_count_all():
    assert len(count_all("cat")) == 3
    assert len(count_all("foo")) == 2
    assert list(count_all("dog").values()) == [1, 1, 1]
    assert count_all("ololo")["o"] == 3



