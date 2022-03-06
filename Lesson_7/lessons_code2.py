import random

class Tank:
    """Template fo tanks"""

    def __init__(self, model, armor, min_damage, max_damage, check, helth):   #функция инициализации класса
        self.model = model   #модель
        self.armor = armor   #броня
        self.damage = random.randint(min_damage, max_damage)  #урон
        self.health = helth  #здоровье
        self.check = check #пробитие
    
    # метод вывода информации о танке
    def print_info(self):    
        print(f"{self.model} имеет броню {self.armor}мм при {self.health}ед. здоровья и урон в {self.damage}")

    # метод получения урона по танку
    def health_down(self, enemy_damage):   
        self.health -= enemy_damage
        print(f"\n{self.model}")
        print(f"Командир по экипажу {self.model} попали, у нас осталось {self.health} очков здоровья")
    
    # метод возгорания танка
    def fire(self):
        a = random.randint(0,100)   # a = 0, 1, 2, .... , 99
        if a < 10:
            print(f"\n{self.model}")
            print(f"Танк {self.model} горит")
            self.health_down(2)

    # метод сстрельбы    
    def shot(self, enemy):
        if enemy.armor >= self.check:
            enemy.armor -= self.check
            print(f"\n{self.model}")
            print(f"Попали в броню, у противника {enemy.model} осталось {enemy.armor} единиц брони")
            return
        print("yes")
        if enemy.health <= 0 or self.damage >= enemy.health:
            enemy.health = 0
            print(f"Экипаж танка {enemy.model} уничтожен")
        enemy.health_down(self.damage)
        enemy.fire()

        print(f"\n{self.model}")
        print(f"Точно в цель, у противника {enemy.model} осталось {enemy.health} единиц здоровья")
    


class SuerTank(Tank):
    """Template fo tanks"""
    def __init__(self, model, armor, min_damage, max_damage, check, helth):
        super().__init__(model, armor, min_damage, max_damage, check, helth)
        self.forceArmor = True

    def health_down(self, enemy_damage):
        super().health_down(enemy_damage/2)