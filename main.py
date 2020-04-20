import random

list_nanes = ['Joe', 'Alex', 'Andr', 'Max', 'Volok', 'Bilbo', 'Kattar', 'Volk', 'Delf', 'Jorje',
              'Hulk', 'Bastard', 'Lexx', 'Botfort', 'Letter', 'Smirnov', 'Serega', 'Broman', 'Barmen', 'Pertro', ]


class Thing:
    def __repr__(self):
        self.name = f'Thing{random.randint(1,2020)}'
        return self.name

    count = 0

    def __init__(self, defence=0, attack=0, hp=0):
        while self.count < 5:
            self.defence = defence or random.randint(1, 5)/300
            self.attack = attack or random.randint(1, 10)
            self.hp = hp or random.randint(80, 100)
            self.count += 1


things = [Thing() for x in range(50)]


class Person:

    def __init__(self, hp, name, attack, defence):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.defence = defence

    def setThings(self, things):
        things_count = random.randint(1, 5)
        things = things[:things_count]  # от 1 до 4 вещей в одни руки
        for thing in things:
            thing = random.choice(things)
            self.hp += thing.hp
            self.attack += thing.attack
            self.defence += thing.defence

    def attacks(self, attack):
        self.hp = self.hp - attack


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


#пока не придумал ,как автоматизировать создание 10 персонажей ниже, просьба подсказать =)
classes = [Paladin, Warrior]  # классы
rand = random.randint(1, 10)  # начальные характеристики для персонажа
rand_def = random.randint(1, 2)/500  # начальная защита
hero_1 = random.choice(classes)(
    rand, random.choice(list_nanes), rand, rand_def)
hero_2 = random.choice(classes)(
    rand, random.choice(list_nanes), rand, rand_def)
hero_3 = random.choice(classes)(
    rand, random.choice(list_nanes), rand, rand_def)
hero_4 = random.choice(classes)(
    rand, random.choice(list_nanes), rand, rand_def)
hero_5 = random.choice(classes)(
    rand, random.choice(list_nanes), rand, rand_def)
hero_6 = random.choice(classes)(
    rand, random.choice(list_nanes), rand, rand_def)
hero_7 = random.choice(classes)(
    rand, random.choice(list_nanes), rand, rand_def)
hero_8 = random.choice(classes)(
    rand, random.choice(list_nanes), rand, rand_def)
hero_9 = random.choice(classes)(
    rand, random.choice(list_nanes), rand, rand_def)
hero_10 = random.choice(classes)(
    rand, random.choice(list_nanes), rand, rand_def)
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

hero_in_arena = [hero_1, hero_2, hero_3, hero_4,
                 hero_5, hero_6, hero_7, hero_8, hero_9, hero_10]


def battle():
    while len(hero_in_arena) > 1:
        attack_hero = random.choice(hero_in_arena)
        defence_hero = random.choice(hero_in_arena)
        while attack_hero == defence_hero:
            defence_hero = random.choice(hero_in_arena)
        print(
            f'Атака - {attack_hero.name}, Защита - {defence_hero.name}\n{attack_hero.hp}- здоровье нападающего, {defence_hero.hp} - здоровье защитника')
        log_def_attack = 0  # считаем урон по защитнику в рамках 1 боя
        log_attack_attack = 0  # считаем урон по атакующему в рамках 1 боя
        while attack_hero.hp > 0 or defence_hero.hp > 0:
            attack = (attack_hero.attack -
                      attack_hero.attack*defence_hero.defence)
            defence_hero.attacks(defence_hero.attack)
            log_def_attack += attack
            print(
                f'{attack_hero.name} наносит удар по {defence_hero.name} на  {attack} урона')
            attack = (defence_hero.attack -
                      defence_hero.attack*attack_hero.defence)
            attack_hero.attacks(attack_hero.attack)
            log_attack_attack += attack
            print(
                f'{defence_hero.name} наносит удар по {attack_hero.name} на  {attack} урона')
        if attack_hero.hp <= 0 and attack_hero.hp < defence_hero.hp:
            print(
                f'Атакующий {attack_hero.name} внезапно проигрывает этот бой!')
        elif defence_hero.hp <= 0 and defence_hero.hp < attack_hero.hp:
            print(
                f'Защита героя {defence_hero.name} не выстояла перед натиском {attack_hero.name} и он выбывает из игры!')

        print(f'{int(log_def_attack)}- нанесено урона нападающему, {int(log_attack_attack)} - нанесено урона защитнику')
        print('======================================')
        if defence_hero.hp <= 0:
            hero_in_arena.remove(defence_hero)
            # после боя, победитель восстанавливает начальный уровень здоровья
            attack_hero.hp += log_def_attack
        elif attack_hero.hp <= 0:
            hero_in_arena.remove(attack_hero)
            # после боя, победитель восстанавливает начальный уровень здоровья
            defence_hero.hp += log_attack_attack
    print(f'Победитель турнира {hero_in_arena[0].name}!')


battle()
