class n:
    def __init__(self, num):
        self.num = num

    def __str__(self):
        return str(self.num)

    def __add__(self, other):
        return self.num + other.num

a = n(1)
b = n(2)
c = a+b
print(a)
print(b)
print(c)
