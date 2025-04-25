def bubble_sort(coll):
    # Функция изменяет входящий список coll
    steps_count = len(coll) - 1
    # Объявляем переменную swapped, значение которой показывает,
    # был ли совершен обмен элементов во время перебора списка
    swapped = True
    # Цикл while
    while swapped:
        swapped = False
        # Перебираем список и меняем местами элементы, если предыдущий
        # больше, чем следующий
        for i in range(steps_count):
            if coll[i] > coll[i + 1]:
                # Используем множественное присваивание для обмена элементов
                coll[i], coll[i + 1] = coll[i + 1], coll[i]
                # Если была совершена перестановка,
                # присваиваем swapped значение True
                swapped = True
        # Уменьшаем счетчик на 1, т.к. самый большой элемент уже находится
        # в конце списка
        steps_count -= 1

    return coll


print(bubble_sort([3, 2, 10, -2, 0]))  # => [-2, 0, 2, 3, 10]
print(bubble_sort([1, 2, 3, 4, 5]))  # => [1, 2, 3, 4, 5]