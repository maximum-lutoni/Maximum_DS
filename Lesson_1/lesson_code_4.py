def add(x,y):
    return x + y

var = add(10,5) # 10 + 5
print(var)
print(add(10, 15))

def hello():
    name = input("Как тебя зовут? ")
    print("Приятно познакомиться " + name)
    hello()
hello()

    
