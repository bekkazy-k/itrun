# d = {}
#
# s = "If the implementation is hard to explain, it's a bad idea."
#
#
# for key in s:
#     if key.lower() not in d:
#         d[key.lower()] = 0
#         # d["i"] = 0
#         # d["f"] = 0
#         # d[" "] = 0
#         # d["t"] = 0
#         # d["h"] = 0
#     d[key.lower()] = d[key.lower()] + 1
# print(d)

"""
name
age
группа крови
рост
пол
образование

мама
    name
    age
    группа крови
    рост
    пол
    образование
папа
    name
    age
    группа крови
    рост
    пол
    образование

"""

d = {
    'name': input("input name"),
    'age': input("input age")
}

name = input("input name")
age = input("input age")
moms_name = input("input name")
moms_age = input("input age")
d = {
    'name': name,
    'age': age,
    'mom': {
        'name': moms_name,
        'age': moms_age
    }
}

print(d)




townspeople = [
    "Шабдан",
    "Аскат",
    "Эсенбек",
    "Аманбек",
    "Ильяз",
    "Данияр",
    "Байэл",
    "Саматова",
    "Алан",
    "Арли",
    "Аким",
    "Бакдоолот",
    "Азиза",
    "Айнура"
]
candidates = [
    "Бекказы",
    "Асылбек"
]

# цикл
    # input your name
    # если имя есть в списке просим выбрать за кого голосует
    # если он выбрал кандидата удаляем его из списка голосующих и увеличиваем
    # у кандидата количество проголосовавших за него (dict)

