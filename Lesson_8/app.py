# WHITE = "\033[1;30m{}\033[0m"
# RED = "\033[1;31m{}\033[0m"
# GREEN = "\033[1;32m{}\033[0m"
# YELLOW = "\033[1;33m{}\033[0m"
# BLUE = "\033[1;34m{}\033[0m"
# MAGENTA = "\033[1;35m{}\033[0m"
# CYAN = "\033[1;36m{}\033[0m"

#
# def adder(a, b, c, d, e):
#     print(a + b + c + d + e)

# def adder(p1, p2, *args):
#     print("p1", p1)
#     print("p2", p2)
#     sum = p1 + p2
#     # sum = 0
#     for i in args:
#         sum = sum + i
#     print(sum)
#
# # adder(4, 7, 9, 3, 5)
# adder(4, 7, 9, 3, 5, 5, 6, 7, 8)


def my_func(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} in {value}")

def my_func_2(d):
    for key, value in d.items():
        print(f"{key} in {value}")


def my_func_3(p1, p2, *args, **kwargs):
    print("p1:", p1)
    print("p2:", p2)

    for i in args:
        print("args: ", i)

    for key, value in kwargs.items():
        print(f"Kwargs: {key} in {value}")

# my_func_3("param 1", "param 2", 55, "55 str", True, Name="Bekkazy", Age=26, ff=33, sdaf="fdsfsdf")


# 1
def some_func(*args):
    s = ""
    for i in args:
        s = s + i
    print(s)

# 2
def some_func_2(*args):
    for i in args:
        print(i, end="\n")
    print()
# \n - Перенос на новую строку

# 3
def some_func_3(*args):
    print("".join(args))

# some_func('B', 'e', 'k', 'k', 'a', 'z', 'y')
# some_func_2('B', 'e', 'k', 'k', 'a', 'z', 'y')
# some_func_3('B', 'e', 'k', 'k', 'a', 'z', 'y')


def summa(a):

    if type(a) != int:
        raise NameError("Incorrect number")

    try:
        print(int(a))
    except BaseException:
        print("Непредвиденная ошибка")
    else:
        print("ОК!")
    finally:
        print("Блок кода выполнится в любом случае!")


def my_f():
    try:
        summa(5)
    except NameError:
        print("Error")



"""
Напишите функцию reverse_order которая принимает любое количество строк и возвращает их в обратном порядке
"""
def reverse_order(*args):
    return args[::-1]

"""
Напишите функцию to_number которая пытается строку перевести в число и вернуть, если эту строку нельзя перевести в число возвращает False
"""

def to_number(a):
    try:
        return int(a)
    except BaseException:
        return False

def to_number_2(a):
    if not a.isdigit():
        return False
    else:
        return int(a)


# print(to_number('ss'))
# print(to_number('4'))
# print(to_number([1,2,3]))
# print(to_number_2('ss'))
# print(to_number_2('66'))
# print(to_number_2[1,2,3])


"""
Напишите функцию number_sum которая принимает любое количество чисел, складывает все числа, даже если числа были отправлены как строка
"""

def number_sum(*args):
    sum = 0
    for i in args:
        if to_number(i) != False:
            sum = sum + to_number(i)
    return sum

print(number_sum(3,5,7))
print(number_sum(3,5,7, '55'))
print(number_sum(3,5, 6, 'asdasd'))


"""
Напишите функцию animals_to_dict которая принимает любое количество 
животных с именами и возвращает один словарь с этими значениями

animals_to_dict(Dog="Alex", Cat="Mary")
{
    "Dog": "Alex", 
    "Cat": "Mary"
}
"""

def animals_to_dict(**kwargs):
    return kwargs

# print(animals_to_dict(Dog="Alex", Cat="Mary"))


"""
Напишите функцию is_palindrome которая проверяет является ли 
строка полиндромом. Палиндром — это слово или фраза, которые 
одинаково читаются слева направо и справа налево.


апа
заказ
"""

def is_palindrome(param):
    if param == param[::-1]:
        return True
    else:
        return False
    # return param == param[::-1]

is_palindrome("апа")
is_palindrome("Тут может быть предложение")


file_extension("курсовая.doc") # doc
file_extension("Фильм.mp4") # mp4