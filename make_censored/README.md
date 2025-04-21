# 🔒 Функция `make_censored`

## 📌 Описание

Реализуйте функцию `make_censored()`, которая заменяет каждое вхождение указанных слов в предложении на последовательность "`$#%!`" и возвращает полученную строку.

## 🧾 Аргументы

- **text** (`str`): входной текст, в котором нужно произвести замену.
- **censored** (`list[str]`): список стоп-слов, которые нужно заменить на "`$#%!`".

Словом считается **любая непрерывная последовательность символов, включая любые спецсимволы (без пробелов).**

## 🧪 Примеры

```python
sentence = 'When you play the game of thrones, you win or you die'
result = make_censored(sentence, ['die', 'play'])
print(result)
# Вывод: 'When you $#%! the game of thrones, you win or you $#%!'

sentence2 = 'chicken chicken? chicken! chicken'
result2 = make_censored(sentence2, ['?', 'chicken'])
print(result2)
# Вывод: '$#%! chicken? chicken! $#%!''