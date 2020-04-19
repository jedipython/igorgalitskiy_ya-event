import random

list_nanes = ['Joe', 'Alex', 'Andr', 'Max', 'Volok', 'Bilbo', 'Kattar', 'Volk', 'Delf', 'Jorje', 'Hulk', 'Bastard', 'Lexx', 'Botfort', 'Letter', 'Smirnov', 'Serega', 'Broman', 'Barmen', 'Pertro',]

class Thing:
    def __repr__(self):
        self.name = f'Thing{random.randint(1,2020)}'
        return self.name

    count = 0

    def __init__(self, defence=0, attack=0, hp=0):
        while self.count < 5:
            self.defence = defence or random.randint(1, 5)/100
            self.attack = attack or random.randint(1, 50)
            self.hp = hp or random.randint(50, 100)
            self.count += 1


things = [Thing() for x in range(50)]


class Person:

    def __init__(self, hp=0, name=None, attack=0, defence=0):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.defence = defence

    def setThings(self, things):
        things = things[:4]
        for thing in things:
            thing = random.choice(things)
            self.hp += thing.hp
            self.attack += thing.attack
            self.defence += thing.defence

    def minus_hp(self):
        pass


class Paladin(Person):
    def __init__(self, hp, name, attack, defence):
        super().__init__(hp, name, attack, defence)
        self.hp *= 2
        self.defence *= 2
        self.class_name = 'Paladin'


class Warrior(Person):
    def __init__(self, hp, name, attack, defence):
        super().__init__(hp, name, attack, defence)
        self.attack *= 2
        self.class_name = 'Warrior'

classes = [Paladin, Warrior] #классы
rand = random.randint(1, 10) #начальные характеристики для персонажа
hero_1 = random.choice(classes)(rand, random.choice(list_nanes), rand, rand)
hero_2 = random.choice(classes)(rand, random.choice(list_nanes), rand, rand)
hero_3 = random.choice(classes)(rand, random.choice(list_nanes), rand, rand)
hero_4 = random.choice(classes)(rand, random.choice(list_nanes), rand, rand)
hero_5 = random.choice(classes)(rand, random.choice(list_nanes), rand, rand)
hero_6 = random.choice(classes)(rand, random.choice(list_nanes), rand, rand)
hero_7 = random.choice(classes)(rand, random.choice(list_nanes), rand, rand)
hero_8 = random.choice(classes)(rand, random.choice(list_nanes), rand, rand)
hero_9 = random.choice(classes)(rand, random.choice(list_nanes), rand, rand)
hero_10 = random.choice(classes)(rand, random.choice(list_nanes), rand, rand)
hero_1.setThings(things)
hero_2.setThings(things)
hero_3.setThings(things)
hero_4.setThings(things)
hero_5.setThings(things)
hero_6.setThings(things)
hero_7.setThings(things)
hero_8.setThings(things)
hero_9.setThings(things)
hero_10.setThings(things)



print('======================================')
print(f'На арену вышли:\n{hero_1.name}, класса {hero_1.class_name}\n{hero_2.name}, класса {hero_2.class_name}\n{hero_3.name}, класса {hero_3.class_name}\n{hero_4.name}, класса {hero_4.class_name}\n{hero_5.name}, класса {hero_5.class_name}\n{hero_6.name}, класса {hero_6.class_name}\n{hero_7.name}, класса {hero_7.class_name}\n{hero_8.name}, класса {hero_8.class_name}\n{hero_9.name}, класса {hero_9.class_name}\n{hero_10.name}, класса {hero_10.class_name}')
print('======================================')

def battle():
    attack_hero = hero_1
    def_hero = hero_3