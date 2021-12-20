def calculate ():
    print('Укажите интересующую вас операцию')
    print('* - умножение')
    print('/ - деление')
    print('+ - сложение')
    print('- - вычитаение')

    operation = input()

    if operation == '*':
        num1 = input("Введите первое число: ")
        num2 = input("Введите второе число: ")
        try:
            res = int(num1) * int(num2)
        except ValueError:
            print("Неизвестные значения")
        else:
            print(res)
    elif operation == '/':
        num1 = input("Введите первое число: ")
        num2 = input("Введите второе число: ")
        try:
            res = int(num1) / int(num2)
        except ValueError:
            print("Неизвестные значения")
        else:
            print(res)
    elif operation == '+':
        num1 = input("Введите первое число: ")
        num2 = input("Введите второе число: ")
        try:
            res = int(num1) + int(num2)
        except ValueError:
            print("Неизвестные значения: ")
        else:
            print(res)
    elif operation == '-':
        num1 = input("Введите первое число: ")
        num2 = input("Введите второе число: ")
        try:
            res = int(num1) - int(num2)
        except ValueError:
            print("Неизвестные значения: ")
        else:
            print(res)
    else:
        print('Операция неизвестна, повторите ввод')

    print(" ")

    calculate()

calculate()