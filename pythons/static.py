class Math:
    def __init__(self, num):
        self.num = num

    @staticmethod
    def add(a, b):
        return a + b


result = Math.add(4, 7)
print(result)
