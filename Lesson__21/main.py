"""
Написать функцию sum_func, которая принимает 2 параметра и возвращает их сумму.
Обработать все возможные ошибки
"""

# <<<<<<< HEAD
# def sum_func(a, b):
# <<<<<<< Updated upstream
# =======
#     if type(a) and type(b) not in (str, int):
#         return False
#
# >>>>>>> Stashed changes
#     try:
#         return a+b
#     except:
# <<<<<<< Updated upstream
#         pass
# =======
# =======
#
# def sum_func(a, b):
#     if type(a) and type(b) not in(str, int):
#         return False
#
#     try:
#         return int(a) + int(b)
#     except:
# >>>>>>> 5fb696cdc50456c303f78ad9902b01422a105b12
#         return False


"""
num_is_palindrome
"""
def num_is_palindrome(n):
    try:
        n = str(n)
        if n[::1] == n[::-1]:
            return True
        return False
    except:
        EOFError

        # if n not in (int, float):
    #     return False
    # try:
    #     if str(n)[::1] == str(n)[::-1]:
    #         return True
    # except:
    #     return False
# =======
#     if type(a) == str:
#         if a.isdigit():
#             a = int(a)
#         else:
#             return False
#
#     if type(b) == str:
#         if b.isdigit():
#             b = int(b)
#         else:
#             return False
#
#     return a + b
