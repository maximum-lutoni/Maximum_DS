home_list = ["Спальня","Гостинная","Кухня","Ванная","Комната"]
print(home_list)
home_list[4] = "Детская"
print(home_list[2:5])
print(len(home_list))

for i in range(5): # range(0,5,1):
    print('какая-то строка')
for i in range(10,1,-3):
    print(i)
for i in home_list:
    print(i)