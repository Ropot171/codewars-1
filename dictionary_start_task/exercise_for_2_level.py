
person = {'name': "Иван", 'age': 26, 'city': "Москва"}

def pop_element():
   return person.pop("age", "Ключ не найден")

def update_dictionary():
    cart = {"apples": 3, "bananas": 2}
    addon = {"bananas": 5, "cherries": 7}
    cart.update(addon)
    return cart


def copy_dictionary():
    person = {'name': "Иван", 'age': 26, 'city': "Москва"}
    person_2 = person.copy()
    person_2.update({'name': "Иван"})
    return person_2

def clear_dictionary():
    person = {'name': "Иван", 'age': 26, 'city': "Москва"}
    person.clear()
    return person
