def some_name(username, age):  # Параметры
    print(f"{username}, ваш возраст {age}, вы молодой")

"""
Напишите функцию make_shirt, которая получает размер футболки и 
текст. Функция должна выводить сообщение с размером и текстом. 
Вызовите функцию с использованием позиционных аргументов. 
Вызовите функцию во второй раз с использованием именованных 
аргументов.

Измените функцию make_shirt, чтобы размер футболок 
по умолчанию был L, а надпись I love Python
"""


def make_shirt(size="L", text="I love Python"):
    print(size, text)


# make_shirt('XL', "Python")  # Позиционно
# make_shirt(size='XL', text="Python")  # Именованно
# make_shirt()

def maximum(a, b):
    if a > b:
        return a
    elif a < b:
        return b
    else:
        return False


def display_upper(text):
    print(text.upper())

# display_upper("hello world")


"""
Написать функцию math_operation которая принимает 
3 аргумента a b и operation. В зависимости от операции 
выводит результат математической операции
"""
def math_operation(a, b, operation="+"):
    if operation == '+':
        return a + b
    elif operation == '-':
        return a - b
    elif operation == '*':
        return a * b
    elif operation == "/":
        return a / b
    else:
        "incorrect operation"

# print(math_operation(5, 10, "+")) # 15
# print(math_operation(5, 10, "-")) # -5
# print(math_operation(5, 10, "*")) # 50
# print(math_operation(5, 10)) # 15


"""
Напишите функцию max_in_list, которая принимает 
список чисел и возвращает максимальный элемент
"""

def max_in_list(inner_list):
    s = inner_list[0]
    for i in inner_list:
        if s < i:
            s = i
    return s

def min_in_list(inner_list):
    s = inner_list[0]
    for i in inner_list:
        if s > i:
            s = i
    return s

my_list = [0, 4, 5, 3, 7, 9, 2]
my_list_2 = [4, 5, 3, 7, 9, 2, 22]
my_list_3 = [0, 4, -5, 36, 7, 9, 2, 22]

print(max_in_list(my_list)) # 9
print(max_in_list(my_list_2)) # 22
print(max_in_list(my_list_3)) # 36

print(min_in_list(my_list)) # 0
print(min_in_list(my_list_2)) # 2
print(min_in_list(my_list_3)) # -5