Реализуйте функцию ```length_of_last_word()```, которая возвращает длину последнего слова переданной на вход строки. Словом считается любая последовательность не содержащая пробелы, символы перевода строки ```\n``` и табуляции ```\t```.
```python 
length_of_last_word('') # 0
length_of_last_word('man in Black') # 5
length_of_last_word('hello, world!     ') # 6
length_of_last_word('hello\t\nworld') # 5
```