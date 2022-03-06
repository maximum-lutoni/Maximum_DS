class A:              # объявление класса
    def one(self):
        print(1)
    
    def two(self):
        print(2)


class B(A):           # наследование класса
    def two(self):
        print("two")

    def three(self):
        print(3)


print("B")
b = B()        
b.one()          # 1
b.two()          # two
b.three()        # 3

print("A")
a = A()
a.one()          # 1
a.two()          # 2
#a.three() вот тут уже ошибка
