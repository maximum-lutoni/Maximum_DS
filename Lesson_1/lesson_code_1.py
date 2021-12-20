first_var = 5 #Тип данных int
second_var = 3.14 #Тип данных float

print(first_var + second_var)
print(first_var - second_var)
print(first_var * second_var)
print(first_var / second_var)

print(type(first_var), type(second_var))

third_var = first_var + second_var
print(third_var)

str_var = "Hello, world!" #тип данных str
test_str = str_var[4:8]
print(test_str)
sub_string_hello = str_var[:5]
sub_string_world = str_var[7:12]
print("W" + sub_string_world[1:] + " h" + sub_string_hello[1:])
print(str_var[0],str_var,str_var[0:6])

name = "Даша"
age = 16
hello = "Привет, меня зовут {}, мне {} лет".format(name, age)
print(hello)