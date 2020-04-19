import random

list_nanes = ['Joe', 'Alex', 'Andr', 'Max', 'Volok', 'Bilbo', 'Kattar', 'Volk', 'Delf', 'Jorje', 'Hulk', 'Bastard', 'Lexx', 'Botfort', 'Letter', 'Smirnov', 'Serega', 'Broman', 'Barmen', 'Pertro',]

class Thing:
    def __repr__(self):
        self.name = f'Thing{random.randint(1,2020)}'
        return self.name

    count = 0

    def __init__(self, defence=0, attack=0, hp=0):
        while self.count < 5:
            self.defence = defence or random.randint(1, 50)
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

class Paladin(Person):
    def __init__(self, hp, name, attack, defence):
        super().__init__(hp, name, attack, defence)
        self.hp *= 2
        self.defence *= 2


class Warrior(Person):
    def __init__(self, hp, name, attack, defence):
        super().__init__(hp, name, attack, defence)
        self.attack *= 2

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


print('======================================')
print(f'Сегодня у нас встречается непобедимый {hero_1.name} с атакой {hero_1.attack}, защитой {hero_1.defence}\n и непорившийся {hero_2.name} с  атакой {hero_2.attack}, защитой {hero_2.defence}!')
print('======================================')

