"""
Написать функцию sum_func, которая принимает 2 параметра и возвращает их сумму.
Обработать все возможные ошибки
"""

def sum_func(x, y):
    if x or y == int:
        return x + y
    else:
        return False

print(sum_func(5, 10))