class Newclass:
    name = "dinesh"

    def func(self):
        print(f"h4ello world {self.name}")

    def func1(self, address):
        print(f"are you from {address}")


obj = Newclass()
obj.name = "hello"
obj.func()
print(Newclass.name)
obj.func1("hello")
