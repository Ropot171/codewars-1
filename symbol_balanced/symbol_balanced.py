def are_symbols_balanced(expression):
    stack = []
    open_brackets = ["(", "[", "{", "<"]
    close_brackets = [")", "]", "}", ">"]

    for symbol in expression:
        if symbol in open_brackets:
            stack.append(symbol)
        elif symbol in close_brackets:
            if not stack:
                return False
            # Ищем индекс закрывающей скобки, чтобы понять, какая открывающая ей соответствует
            index = close_brackets.index(symbol)
            if stack[-1] == open_brackets[index]:
                stack.pop()
            else:
                return False
    return len(stack) == 0


def test_are_symbols_balanced():
    assert are_symbols_balanced('()') is True
    assert are_symbols_balanced('[()]') is True
    assert are_symbols_balanced('({}[])') is True
    assert are_symbols_balanced('(<><<{[()]}>>)') is True
    assert are_symbols_balanced('') is True

    assert are_symbols_balanced('((') is False
    assert are_symbols_balanced('[[()]') is False
    assert are_symbols_balanced('({}}[]') is False
    assert are_symbols_balanced('(<><<{[()]}>>>)') is False
    assert are_symbols_balanced('}') is False
    assert are_symbols_balanced('([)]') is False
    assert are_symbols_balanced('([))') is False

    assert are_symbols_balanced('()') is True
    assert are_symbols_balanced('[()]') is True
    assert are_symbols_balanced('({}[])') is True
    assert are_symbols_balanced('(<><<{[()]}>>)') is True
    assert are_symbols_balanced('') is True






