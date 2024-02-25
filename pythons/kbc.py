questions = [
    ["what is your name", "dinesh", "adhikari", "ascol", "pokhara", 1],
    ["what is your lname", "dinesh", "adhikari", "ascol", "pokhara", 2],
    ["where did you study", "dinesh", "adhikari", "ascol", "pokhara", 3],
    ["what are you from", "dinesh", "adhikari", "ascol", "pokhara", 4],
    ["what is your name", "dinesh", "adhikari", "ascol", "pokhara", 1],
    ["what is your name", "dinesh", "adhikari", "ascol", "pokhara", 1],
    ["what is your name", "dinesh", "adhikari", "ascol", "pokhara", 1],
]


# print(count)
# print(len(questions))
# for i in range(0, len(questions)):
def kbc(i):

    temp = [1000, 10000, 20000, 50000, 100000, 320000, 5000000, 100000]
    return temp[i]


count = 0
# temp = [1000,10000,20000,50000]
x = 0
for i in questions:

    a = int(input(f"{i[0]}\n1.{i[1]}\n2.{i[2]}\n3.{i[3]}\n4.{i[4]}"))
    if a == i[5]:

        if x >= 0:
            temp = kbc(x)
            count = count + temp
            x = x + 1
        #   print(count)
    else:
        break

print(count)


# print(count)
# print(len(questions))
# for i in range(0, len(questions)):
# def kbc(i):
#    temp = [1000,10000,20000,50000]
#    return temp[i]
