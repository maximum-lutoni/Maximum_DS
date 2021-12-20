var_1 = True   #1
ver_2 = False  #0

var_1 = 5 > 1  #тип данных bool
print(var_1)
print(type(var_1))

if True:
    print("Условие выполнилось")

if False:
    pass
else:
    print("Условие не выполнилось")

print( 0 and 0,  #0 False
       0 and 1,  #0 False
       1 and 0,  #0 False
       1 and 1 ) #1 True

print( 0 or 0,  #0 False
       0 or 1,  #1 True
       1 or 0,  #1 True
       1 or 1 ) #1 True

print( not 0,  #1 True
       not 1)  #0 False

print(not not 0) #0 False
