class Number:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return Number(self.value + other.value)

    def __sub__(self, other):
        return Number(self.value - other.value)

    def display(self):
        print(self.value)

num1 = Number(20)
num2 = Number(10)

result1 = num1 + num2
result2 = num1 - num2

result1.display()
result2.display()