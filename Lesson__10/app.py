import os

# os.getcwd() - текущая рабочая директория.
# os.path.join(dir_name, 'file_1.txt') - связывает 2 пути

# curr_dir = os.getcwd()
# filename = 'hello.txt'
#
# print(os.path.join(curr_dir, filename))
#
# f = open(filename, 'r')
# print("Текущая позиция:", f.tell())
# print(f.read(5))
# print("Текущая позиция:", f.tell())
# print(f.read(7))
# print("Текущая позиция:", f.tell())
# f.close()

def read_from_file(filename):
    f = open(filename, 'r')
    for line in f:
        print(line, end="")
    print()


"""
Написать функцию write_to_file, которая принимает 2 параметра 
file_name и text. Функция записывает в текушеф директории файл, 
название которой принимает в параметре file_name и записывает 
в нее текст полученный в параметре text. Возвращает True при 
успешной записи, False при ошибке
"""

def write_to_file(file_name, text):
    try:
        f = open(file_name, 'x')
        f.write(text)
        f.close()
        return True
    except:
        return False


def write_to_file2(file_name, text):
    try:
        with open(file_name, 'w') as f:
            f.write(text)
        return True
    except:
        return False


"""
Написать функцию read_from_file, которая принимает 1 параметр 
file_name, читает файл из текушей директории и возвращает его содержимое
"""

def read_from_file(file_name):
    with open(file_name, 'r') as f:
        t = f.read()
    return t

# print(read_from_file("file_1.txt"))


"""
Написать функцию read_by_count, которая принимает 2 параметра 
file_name и cnt, читает файл из текущей директории и возвращает 
cnt количество символов
"""
def read_by_count(file_name, cnt):
    with open(file_name, 'r') as f:
        t = f.read(cnt)
    return t


# print((lambda x, y: x + y)(5, 12))
# #
# # l1 = [i for i in range(15)]
# # l2 = [i ** 2 for i in range(15)]
# # l3 = [(lambda x: x ** 2)(i) for i in range(15)]
# # print(l1)
# # print(l2)
# # print(l3)

# Рекурсия

def my_func(numb):
    if numb >= 5:
        return
    else:
        numb += 1
        print(numb)


my_func(0)
