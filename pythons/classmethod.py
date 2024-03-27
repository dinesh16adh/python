class Newclass:
    name = "dinesh"

    def func(self):
        print(f"hello {self.name}")

    @classmethod
    def func1(cls, newname):
        cls.name = newname
        # print(f"are you from {cls.newaddress}")


obj = Newclass()
# obj.name = "hello"
# obj.func()
# print(Newclass.name)
obj.func1("Dinesh")
obj.func()
# obj.N
