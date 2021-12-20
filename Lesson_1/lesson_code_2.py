try:
    input_first_var = int(input("Введите число: ")) #25
    input_second_var = int(input("Введите число: ")) # 3
except ValueError:
    print("Вы ввели неправильное значение")
else:
    print(input_first_var+input_second_var)
    print(input_first_var / input_second_var)
    print(type(input_first_var))

    if input_first_var > input_second_var:
        print(input_first_var, "больше", input_second_var)
    elif input_second_var > input_first_var:
        print(input_second_var, "больше", input_first_var)
    else:
        print(input_first_var, "=", input_second_var)

try:
    "код который мы хоти выполнить"
except "тип ошибки":
    "Действие программ если ошибку нашли"
else:
    "Действие если ее не возникло"