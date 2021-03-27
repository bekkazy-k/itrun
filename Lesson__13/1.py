def num_is_palindrome(n):
    n= str(n)
    if n[::1] == n[::-1]:
        return True
    return False
    # if n not in (int, float):
    #     return False
    # s = str(n)
    #
    # try:
    #     if s[::1] == s[::-1]:
    #         return True
    # except:
    #     return False

# a= num_is_palindrome(535)
# print(a)
#
# x= 356
# y =str(x)
#
# print(y[::-1])
