def build_definition_list(text):
    if not text:
        return ""
    parts = []
    for item in text:
        parts.append(f"<dt>{item[0]}</dt><dd>{item[1]}</dd>")
    inner_value = "".join(parts)
    result = f"<dl>{inner_value}</dl>"
    return result

def test_build_definition_list_empty():
    result = build_definition_list([])
    assert result == ''


def test_build_definition_list_single():
    definitions = [("Python", "A programming language.")]
    result = build_definition_list(definitions)
    expected = '<dl><dt>Python</dt><dd>A programming language.</dd></dl>'
    assert result == expected


def test_build_definition_list_multiple():
    definitions = [
        ("Python", "A programming language."),
        ("JavaScript", "A web programming language."),
        ("HTML", "A markup language.")
    ]
    result = build_definition_list(definitions)
    expected = (
        '<dl>'
        '<dt>Python</dt><dd>A programming language.</dd>'
        '<dt>JavaScript</dt><dd>A web programming language.</dd>'
        '<dt>HTML</dt><dd>A markup language.</dd>'
        '</dl>'
    )
    assert result == expected



# test1<dl><dt>Блямба</dt><dd>Выпуклость, утолщение на поверхности чего-либо</dd><dt>Бобр</dt><dd>Животное из отряда грызунов</dd></dl>