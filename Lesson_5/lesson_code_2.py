div_5_list = []

for x in range(2,100):
    if x % 5 == 0:
        div_5_list.append(x)  # list.append(x) - добавление элемента x в список list

print(div_5_list)

# Генератор списков
# [x for x in list if smth]
div_5_list_2 = [x if x > 50 else x**3  for x in range(2,100) if x % 5 == 0]

print(div_5_list_2, len(div_5_list_2))

x = "orange"
a = len(x)  # len() - Нахождение длины списка, строки и тд.

# Генератор словарей
# {x:x for x in list}
a = {x: len(x) for x in ["orange", "red", "blue", "green"]}
a = {x: x**2 for x in range(2,100)}
print(a)

div_30_and_31_list = []
for x in range(0, 1000):
    if x % 30 == 0 and x % 31 == 0:
        div_30_and_31_list.append(x)

div_30_and_31_list = [x for x in range(0, 1000) if x % 30 == 0 and x % 31 == 0]


