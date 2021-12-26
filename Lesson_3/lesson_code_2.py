#Работа с файлами
#
#r - чтение
#w - запись
#a - добавление
#r+ - запись и чтение

my_file = open("file.txt",'w')
my_file.write("Какой-то текст")
my_file.close()

my_file = open("file.txt", "r")
my_text = my_file.read()
print(my_text)
my_file.close()