def func(a, b, *args, **kwargs):    # *args - неименованные аргументы 1, 2, 123
    c = kwargs.get("c",3)           # **args - именованные аргументы  с = 4, one = 1
    print(a)
    print(b)
    print(c)
    print(args)
    print(kwargs)


func(1, 2, 123, 77, True, c=4, one=1, two=2)

age = 18

# Тернарный оператор if
# c = a if условие else b
# if условие:
#     c = a
# else:
#     c = b

# Вариант 1 - обычный if
if age >= 18:
    is_allow = True
else:
    is_allow = False
# Вариант 2 - тернарный if
is_allow = True if age >= 18 else False
# Вариант 3
is_allow = age >= 18 

print(is_allow)


# Обработка None
val = None            
# Вариант 1
if val is None:                    
    res = []
else:
    res = val
# Вариант 2
res = [] if val is None else val
# Вариант 3
res = val or res