# a = input("enter the number: ")
# print(f"multiplication table of {a} is \n")
# try:
#     for i in range(1, 11):
#         print(f"{int(a)} x {i} = {int(a)*i} \n")
# except Exception as e:
#     print(e)


# print("some line of codes\n")
# print("end of program")
try:
    num = int(input("enter an integer: "))
    a = [6, 3]
    print(a[num])
except ValueError:
    print("number enter is not an integer")
except IndexError:
    print("index error")
