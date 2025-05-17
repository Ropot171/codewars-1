def birthday_list(text):
    d = {}
    for pair in text:
        key, value = pair.split(maxsplit=1)
        if key in d:
            d[key].append(value)
        else:
            d[key] = [value]
    return d

def test_birthday_list():
    input_data = [
        "3 Сергей",
        "5 Николай",
        "4 Елена",
        "7 Владимир",
        "5 Юлия",
        "4 Светлана"
    ]

    expected_output = {
        "3": ["Сергей"],
        "4": ["Елена", "Светлана"],
        "5": ["Николай", "Юлия"],
        "7": ["Владимир"]
    }

    assert birthday_list(input_data) == expected_output

