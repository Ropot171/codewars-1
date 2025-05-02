from add_meeting import email


def person_new(name, age, city):
    person = {'name': name, 'age': age, 'city': city}
    return person

def print_person():
    person = person_new("Иван", 26, "Москва")
    print("Имя:", person["name"])
    print("Возраст:", person["age"])
    print("Город:", person["city"])

def check_name():
    if "email" in person_new("Иван", 26, "Москва"):
        return "Есть email"
    else:
        return "Нет email"

person = {'name': "Иван", 'age': 26, 'city': "Москва"}

def get_name():
    return person.get("email", "unknown")

def cycle_keys():
    for k in person:
        print(k)

def all_items():
    for k,v in person.items():
        print(k, "=", v)

def all_items_i():
    for k,v in person.items():
        print(k, ":", v)

def student_new():
    student = {
    "name": "Anna",
    "grades": {
        "math": 5,
        "english": 4
    }
}
    return student

def get_english_grade():
    student = student_new()  # Получаем словарь студента
    return student["grades"]["english"]  # Получаем оценку по английскому

key = "color"
value = "blue"

def new_color(key, value):
    return {key: value}


