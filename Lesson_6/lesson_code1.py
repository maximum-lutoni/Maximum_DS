name = "Ваня"

height = 178
weight = 70


# f - строки. Аналог форматирования строки - .format()
# "{}".format(a)    "{}{}".format(a,b)
# f"{a}"            f"{a}{b}"

def breath():
    print("{} дышит".format(name))

def thinks():
    print(f"{name} думает...")

class Human:
    # инициализация класса
    def __init__(self, name, height, weight,color_of_hair):
        self.name = name
        self.height = height
        self.weight = weight
        self.color_of_hair = color_of_hair

human1 = Human(name="Ivan", height=178, weight=70, color_of_hair="red")
human1.name = "Sasha"
human1.height += 10
print(f"{human1.name} весит {human1.weight}кг при росте {human1.height}см")

human2 = Human(name="Дмитрий", height=190, weight=90, color_of_hair="black")
print(f"{human2.name} весит {human2.weight}кг при росте {human2.height}см")

#__название__ - магические методы