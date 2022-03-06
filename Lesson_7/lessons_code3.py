a = "Hello" + " " + "word" + "!"
b = 1 + 2 + 3 + 4 + 5

print(id(1), type(1))
print(id(id), type(id))
print(id(type), type(type))

class A:
    def public(self):
        return 2022
    
    def _private(self):
        return "private"
    def __protect(self):
        return True
    def wrapper(self):
        return self.__protect()


a = A()
print(a.public())
print(a._private())
print(a._A__protect())
#print(a.__protect()) ошибка

