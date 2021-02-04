# Базовые типы
## Численные типы 
- int
- float

## Логический тип 
- Boolean

## Операторы сравнения
- `<` - Меньше — условие верно, если первый операнд меньше второго
- `>` - Больше — условие верно, если первый операнд больше второго.
- `<=` - Меньше или равно.
- `>=` - Больше или равно.
- `==` - Равенство. Условие верно, если два операнда равны.
- `!=` - Неравенство. Условие верно, если два операнда неравны.

## Строки
- Последовательность символов в строке
```python
a = "Hello world"

print(a[0])
# H

print(a[1])
# e
```
- Срезы строк `string[start, stop, step]`
```python
a = "Hello world"

print(a[0:4])
# Hell

print(a[0:11:2])
#Hlowrd
```
- Длина строки `len(string)`
```python
a = "Hello world"
print(len(a))
# 11
```
- Количество символов в строке `string.count([symbol])`
```python
a = "Hello world"

print(a.count('l'))
# 3

print(a.count('h'))
# 0

print(a.count('H'))
# 1
```

- Сделать заглавной первую букву `string.capitalize()`
```python
a = "hello world"

print(a.capitalize())
# 'Hello world'
print(a)
# 'hello world'
```
- Наличие подстроки в строке `string in string`
```python
a = "Hello world"

print('Hell' in a)
# True

print('hell' in a)
# False
```
- Замена подстроки в строке `string.replace(old, new, count)`
```python
a = "Hello world"
print(a.replace("l", "0"))
# He00o wor0d

print(a.replace("l", "0", 1))
# He0lo world

print(a.replace("l", "0", 2))
# He00o world
```
- Форматирование строки `string.format(...params)`
```python
a = "Меня зовут {}, я родился в {} году."
name = "Бекказы"
year = 1994
print(a.format(name, year))
# 'Меня зовут Бекказы, я родился в 1994 году'
```
- Именованное форматирование строки `string.format(...params)`
```python
a = "Меня зовут {name}, я родился в {year} году."
name = "Бекказы"
year = 1994
print(a.format(name=name, year=year))
# 'Меня зовут Бекказы, я родился в 1994 году'
```
- F строки
```python
name = "Бекказы"
year = 1994
print(f'Меня зовут {name}, я родился в {year} году.')
# Меня зовут Бекказы, я родился в 1994 году.
```

## None
Используется для того, чтобы подчеркнуть отсутствие значения

## коневертация типов данных
```python
int_number = 5 # Целочисленный тип данных
float_number = 6.6 # Число с плавающей точкой
str_string = "My string1" # Строковый тип данных
number_in_string = "10"

print(float(int_number))
# 5.0

print(int(float_number))
# 6

print(int(str_string)) 
# Error

print(int(number_in_string))
# 10
```


# Задачи
Дана строка: `Beautiful is better than ugly.`
- Сначала выведите третий символ этой строки
- Во второй строке выведите первые пять символов этой строки.
- В третьей строке выведите все символы в обратном порядке.
- В четвертой строке выведите длину данной строки.
- В пятой строке поменяйте слова better и ugly местами.
