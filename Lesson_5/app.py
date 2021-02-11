num_list = [12, 45, 10, 89, 88, 56, -4, 5]

# sum_of_list = 0
#
# for i in num_list:
#     sum_of_list = sum_of_list + i
#
# print(sum_of_list / len(num_list))

"""
[12, 45, 10, 89, 88, 56, -4, 5]
 0   1    2   3   4   5   6  7
 
Результат: 12, 10, 88, -4

"""

# for i in range(len(num_list)):
#     if i % 2 == 0:
#         print(num_list[i])
#
#
# for i in range(0, len(num_list), 2):
#     print((num_list[i]))

# for i in num_list:
#     if i % 2 == 0:
#         print(i)
#
# for i in range(len(num_list)):
#     if num_list[i] % 2 == 0:
#         print(num_list[i])

"""
[12, 45, 10, 89, 88, 56, -4, 5]

Результат: 45, 89, 5

"""

for i in range(len(num_list)):
    if i > 0 and num_list[i] > num_list[i-1]:
        print(num_list[i])

