my_list = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]


def find_max(matrix):
    s = matrix[0][0]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if s < matrix[i][j]:
                s = matrix[i][j]
    return s
# print(find_max(my_list))

def find_min(matrix):
    s = matrix[0][0]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if s > matrix[i][j]:
                s = matrix[i][j]
    return s
# print(find_min(my_list))

def find_summa(matrix):
    s = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            s += matrix[i][j]

    return s
# print(find_summa(my_list))