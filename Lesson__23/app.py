def find_max(matrix):
    t = matrix[0][0]
    for i in range(len(matrix)):
        for e in range(len(matrix[i])):
            if t < matrix[i][e]:
                t = matrix[i][e]
    return t


d = [
    [132, 4658, 982],
    [1578, 2547, 6879],
    [651567, 0, 654678]
]
# print(find_max(d))

def find_min(matrix):
    t = matrix[0][0]
    for i in range(len(matrix)):
        for e in range(len(matrix[i])):
            if t > matrix[i][e]:
                t = matrix[i][e]
    return t
# print(find_min(d))

def find_summa(matrix):
    t = 0
    for i in range(len(matrix)):
        for e in range(len(matrix[i])):
            t += matrix[i][e]

    return t
print(find_summa(d))
