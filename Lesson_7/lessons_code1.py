class A:
    def one(self):
        print(1)
    
    def two(self):
        print(2)


class B(A):
    def two(self):
        print("two")

    def three(self):
        print(3)


print("B")
b = B()
b.one()
b.two()
b.three()

print("A")
a = A()
a.one()
a.two()
#a.three() вот тут уже ошибка
