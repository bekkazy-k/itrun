"""
Написать функцию sum_func, которая принимает 2 параметра и возвращает их сумму.
Обработать все возможные ошибки
"""

def sum_func(a, b):
    if type(a) and type(b) not in  (int, str):
        return False

    try:
        return int(a) + int(b)
    except:
        return False

print(sum_func(5, 6))
print(sum_func("5", "6"))

