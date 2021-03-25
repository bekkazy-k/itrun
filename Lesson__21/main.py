"""
Написать функцию sum_func, которая принимает 2 параметра и возвращает их сумму.
Обработать все возможные ошибки
"""

def sum_func(a, b):
    if type(a) or type(b) != int or str:
        return False
    return int(a) + int(b)
print(sum_func(5, 6))


"""
num_is_palindrome
"""
def num_is_palindrome():
    pass