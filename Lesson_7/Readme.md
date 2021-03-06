# Функции
Функции — это такие участки кода, которые изолированы от остальный программы и выполняются только тогда, когда вызываются.

`def` - ключевое слово, сообщает Python что вы определяете функцию. Далее идёт имя функции
```python
def greet_user():
    print("Hello!")

greet_user()
# Hello!
```

При некобходимости, функция может принимать данные и работать с ними. 
Входящие в функцию параметры определяются внутри скобок через запятую, такие параметры называются позиционные аргументы.
```python
def greet_user(name):
    print(F"Hello, {name}!")

greet_user("Bekkazy")
# Hello, Bekkazy!

greet_user("Asylbek")
# Hello, Asylbek!
```

Несколько входящих параметров:
```python
def greet_user(name, age):
    print(F"Hi {name}, you are {age} years old!")

greet_user("Bekkazy", 26)
# Hi Bekkazy, you are 26 years old!

greet_user("Asylbek", 20)
# Hi Asylbek, you are 20 years old!
```

## Упражнения 
- Напишите функцию `display_message` которая принимает текст и выводит его
- Напишите функцию `display_user_info` которая принимает 3 параметра `имя` `фамилию` и `возраст` и выводит сообщение `Привет [имя], твоя фамилия [фамилия], твой возраст [возраст]`


## Именованные аргументы
Именованный аргумент представляет собой пару `имя - значение` передаваемую функции.
```python
def greet_user(name, age):
    print(F"Hi {name}, you are {age} years old!")

greet_user(name="Bekkazy", age=26)
# Hi Bekkazy, you are 26 years old!

greet_user(age=26, name="Bekkazy")
# Hi Bekkazy, you are 26 years old!
```

## Значения по умолчанию
Для каждого параметра в вашей функции можно определить значение по умолчанию. 
Если при вызове функции передается аргумент, то используется этот аргумент. 
Если значение не передается, используется значение по умолчанию
```python
def describe_pet(pet_name, animal_type='dog'):
    print(F"I have a {animal_type}")
    print(F"My {animal_type}'s name is {pet_name}")

describe_pet("Willie", "cat")
# I have a cat
# My cat's name is Willie

describe_pet("Alex")
# I have a dog
# My dog's name is Alex
```
> Если вы используете значени по умолчанию, они должны быть обьявлены после параметров, у которых нет значений по умолчанию

## Упражнения 
- Напишите функцию `make_shirt`, которая получает размер футболки и текст. Функция должна выводить сообщение с размером и текстом. Вызовите функцию с использованием позиционных аргументов. Вызовите функцию во второй раз с использованием именованных аргументов.
- Измените функцию `make_shirt`, чтобы размер футболок по умолчанию был `L`, а надпись `I love Python`

## Возвращаемое значение
Функция может возвращает значение. 
Команда `return` говорит функции прекратить работу и вернуть значение
```python
def summa(a, b):
    return a + b

result = summa(5, 10)
print(result)
# 15

print(summa(2, 7))
# 9
```

## Практика
#### Верхний регистр
Написать функцию `display_upper`, которая принимает строку и выводит его в верхнем регистре.

#### Арифметические операции
Написать функцию `math_operation` которая принимает 3 аргумента `a` `b` и `operation`.
В зависимости от операции выводит результат математической операции

#### Арифметические операции 2
Измените функцию `math_operation` так, чтобы она возвращала результат и по умолчанию была операция `+`

#### Максимальный в списке
Напишите функцию `max_in_list`, которая принимает список чисел и возвращает максимальный элемент

#### Минимальный в списке
Напишите функцию `min_in_list`, которая принимает список чисел и возвращает минимальный элемент

#### Сумма максимального и минимального
Напишите функцию `sum_max_min`, которая принимает список чисел и возвращает сумму максимального и минимального элемента

#### Разделение словаря
Напишите функцию `segmentation`, которая принимает словарь и выводит его ключи и значения по отдельности

