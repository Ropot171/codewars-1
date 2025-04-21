def make_censored(text, censored):
    separator = " "
    new_text = text.split(separator)
    censored_text = []

    for word in new_text:
        if word in censored:
            censored_text.append('$#%!')
        else:
            censored_text.append(word)

    return separator.join(censored_text)

def test_make_censored():
    sentence = 'When you play the game of thrones, you win or you die'
    actual = make_censored(sentence, ['die'])
    expected = 'When you play the game of thrones, you win or you $#%!'
    assert actual == expected

    sentence = 'chicken chicken? chicken! chicken'
    actual = make_censored(sentence, ['chicken'])
    expected = '$#%! chicken? chicken! $#%!'
    assert actual == expected

    sentence = 'chicken chicken? chicken! ? chicken'
    actual = make_censored(sentence, ['?', 'chicken'])
    expected = '$#%! chicken? chicken! $#%! $#%!'
    assert actual == expected

    sentence = 'chicken chicken? chicken! ? ! @ chicken'
    actual = make_censored(sentence, ['?', '!', '@', 'chicken'])
    expected = '$#%! chicken? chicken! $#%! $#%! $#%! $#%!'
    assert actual == expected
