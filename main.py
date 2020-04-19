import random


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
        list_nanes = ['Joe', 'Alex',
                      'Andr', 'Max', 'Volok']
        self.name = name or random.choice(list_nanes)
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
    def __init__(self):
        self.hp = self.hp * 2
        self.defence = self.defence * 2

class Warior(Person):
    def __init__(self):
        self.hp = self.attack * 2


a1 = Person()
a2 = Person()
a1.setThings(things)
a2.setThings(things)

print(f'Сегодня у нас встречается непобедимый {a1.name} с атакой {a1.attack}, защитой {a1.defence}\n и непорившийся {a2.name}с  атакой {a2.attack}, защитой {a2.defence}!')


