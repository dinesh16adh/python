class Newclass:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def func(cls, string):
        name, age = string.split("-")
        return cls(name, age)


obj = Newclass.func("dinesh-21")
print(obj.name)
print(obj.age)
