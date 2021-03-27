
n=input()

if str(n)[::1] == str(n)[::-1]:
    print("ok")
    return True
else:
    print("no")


