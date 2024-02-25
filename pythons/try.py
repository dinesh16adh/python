# try:
#     i = int(input("enter any value"))

# except Exception as e:
#     print(e)
try:
    num = int(input("enter the index of array you want to accessed\n"))
    i = [1, 2, 3, 4, 5]
    print(i[num])
except IndexError:
    print(" invalid index \n")
except ValueError:
    print("the number doesnot exist\n")
