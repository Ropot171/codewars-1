# Функция get_same_count()

## Описание
Функция `get_same_count()` принимает два списка и возвращает количество общих уникальных значений, встречающихся в обоих списках. Реализация выполнена с использованием вложенных циклов, в учебных целях.

## Синтаксис
```python
def get_same_count(list1, list2):
    unique1 = []
    for item in list1:
        if item not in unique1:
            unique1.append(item)

    unique2 = []
    for item in list2:
        if item not in unique2:
            unique2.append(item)

    count = 0
    for item in unique1:
        for other in unique2:
            if item == other:
                count += 1
                break

    return count
```

## Примеры использования
```python
# Общие уникальные элементы: 1, 3, 2
print(get_same_count([1, 3, 2, 2], [3, 1, 1, 2, 5]))  # 3

# Общие уникальные элементы: 4
print(get_same_count([1, 4, 4], [4, 8, 4]))  # 1

# Общие уникальные элементы: 1, 10
print(get_same_count([1, 10, 3], [10, 100, 35, 1]))  # 2

# Нет элементов
print(get_same_count([], []))  # 0
```

## Подсказка
Для удаления дубликатов вручную используем списки и условные проверки внутри циклов, а не встроенные функции Python, такие как `set()`, чтобы лучше понять основы.

---

