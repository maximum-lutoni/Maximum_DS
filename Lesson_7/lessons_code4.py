class Sngeleton(object):
    def __new__(cls):
        if not hasattr(cls, 'instans'):
            cls.instance = super(Sngeleton,cls).__new__(cls)
        return cls.instance

def f():
    return 2+2

q = f
print(q())

def repair_deco(func): # постоянный аргумент это func
    def wrapper(a,b): # аргумкенты которые получает функция
        return func(a,b) - 1
    return wrapper # возвращаем внутреннюю функцию


@repair_deco
def wrong_func(a,b):
    return a + b + 1

print(f"2 + 2 = {wrong_func(2,2)}")
print(f"5 + 6 = {wrong_func(5,6)}")