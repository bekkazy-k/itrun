from random import randint

def get_name(tail=""):
    if tail == "":
        name = input("Введите ваше имя:")
    else:
        name = input("Введите ваше имя. " + tail)
    return name

"""
get_result
a - number
b - number
c - default = +, [+,-,/,*]

Результат арифметической операции
"""

def get_result(a, b, c="+"):
    if c not in(["+", "-", "/", "*"]):
        return False

    if type(a) != int or type(b) != int:
        return False

    if c == '/':
        return a / b
    elif c == '*':
        return a * b
    elif c == '-':
        return a - b
    else:
        return a + b


"""
import random # randint(start, stop)

game(from_number, to_number, cnt)

"""

def game(from_number, to_number, cnt):
    print(f"Привет друг! Я загадал число от {from_number} до {to_number}")
    print(f"Попробуй угадать за {cnt} попыток")
    random_number = randint(from_number, to_number)
    count_tries = 0
    while count_tries < cnt:
        input_number = int(input("Введи число: "))
        if random_number > input_number:
            print("Загаданное число больше")
        elif random_number < input_number:
            print("Загаданное число меньше")
        elif random_number == input_number:
            break
        count_tries = count_tries + 1

    if random_number == input_number:
        print(f"Поздравляю, ты угадал число за {count_tries + 1} раз")
    else:
        print("Ты проиграл, попробуй еще раз!")


def my_func(townspeople, candidates):
    cnt = len(townspeople)
    result = dict()

    for i in candidates:
        result[i] = 0

    while True:
        if len(townspeople) <= 0:
            break

        name = input("Введите ваше имя: ")
        if name == "exit":
            break

        if name in townspeople:
            c = input("Выберите кандитата: " + ", ".join(candidates) + " : ")
            if c in candidates:
                # result[c] = result[c] + 1
                result[c] += 1
                townspeople.remove(name)
            else:
                print(f"Имени {c} нет в списке кандидатов. Проверьте корректность")
        else:
            print(f"Имени {name} нет в списке голосующих. Проверьте корректность")

    if len(townspeople) > 0:
        cnt = cnt - len(townspeople)

    for key, value in result.items():
        print(f"За кандидата {key} проголосовало {value} людей. Это {(value / cnt) * 100}% избирателей")
