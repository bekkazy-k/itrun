"""
Написать функцию sum_func, которая принимает 2 параметра и возвращает их сумму.
Обработать все возможные ошибки
"""


def sum_func(a, b):
    if type(a) and type(b) not in(str, int):
        return False

    try:
        return int(a) + int(b)
    except:
        return False


"""
num_is_palindrome
"""
def num_is_palindrome(a, b):
    pass
    try:
        if a == str(a) or a == int(a) and b == str(b) or b == int(b):
            if a == True or a == False or b == True or b == False:
                return False
            return int(a) + int(b)
        return False
    except:
        return False
