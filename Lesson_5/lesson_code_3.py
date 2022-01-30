a = list()  #[]
b = tuple() #() - неизменяемый список

some_dict ={
    (1,2,3) : "Hello"
}

a = some_dict[(1,2,3)]
print(a) 

some_tuple = (1,2,3)
print(some_tuple, type(some_tuple))
some_list = list(some_tuple)
print(some_list, type(some_list))

some_tuple = ([1,2,3], "qwe")
print(some_tuple)
some_tuple[0].append(4)
print(some_tuple)

a = [1,2,3,4]
b = ["a","b","c","d"]

for x in zip(a,b):
    print(x, type(x))

def f(x):
    return x*x

# lambda аргументы : возвращаемое значение
f = lambda x : x*x
f = lambda x, y: x + y
f = lambda : True

# map(функция, итерируемый объект(список, строка, range() etc))
# применяет функцию к каждому элементу объекта
L = [1,2,3,4,5]
a = list(map(lambda x: x**2, L))

def if_even(x):
    return x%2 == 0


# filter(функция, итерируемый объект(список, строка, range() etc))
# отбирает элементы объекта если функция = True
a = list(filter(lambda x: x%2 == 0, L))
print(a)
