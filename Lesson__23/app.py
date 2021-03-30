massive = [[2, 8, 37, 50, 12, 9, 45], [8, 19, 28, 36, 28, 4,], [71, 35, 34, 57, 8, 29, 4]]

def find_max(matrix):
    max_value = matrix[0][0]
    for i in range(len(massive)):
        for j in range(len(massive[i])):
            if max_value < matrix[i][j]:
                max_value = matrix[i][j]
    return max_value

def find_min(matrix):
    min_value = matrix[0][0]
    for i in range(len(massive)):
        for j in range(len(massive[i])):
            if min_value > matrix[i][j]:
                min_value = matrix[i][j]
    return min_value

def get_sum(matrix):
    summ = matrix[0][0]
    for i in range(len(massive)):
        for j in range(len(massive[i])):
            summ = sum(matrix[i][j])
    return summ

print(find_max(massive))
print(find_min(massive))
print(get_sum(massive))