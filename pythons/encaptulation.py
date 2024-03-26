class Me:
    name = "dinesh"
    __age = 21
    age = __age

    def __func(self):
        return "this is test method"

    def func(self):
        return self.__func()


class Test(Me):
    test = "hello world"


obj = Test()
print(obj.func())
