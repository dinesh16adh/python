# try:
#     k = 5 // 2
#     print(k)
# except ZeroDivisionError:
#     print("cant divide by zero")
# finally:
#     print("this is always executed")
def func():
    try:
        k = 5 // 0
        print(k)
        return 1
    except ZeroDivisionError:
        print("cant divide by zero")
        return 0
    finally:
        print("this is always executed")


x = func()
print(x)
