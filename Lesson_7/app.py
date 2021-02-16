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


def dispaly_upper(text):
    print(text.upper())


