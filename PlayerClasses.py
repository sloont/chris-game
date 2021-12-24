import random

class Pawn:
    #we could honestly just use this parent as the class for monsters
    def __init__(self,stats):
        self.name = stats['name']
        self.health = stats['health']
        self.damage = stats['damage']
        self.defense = 0
        self.can_attack = True
        self.is_dead = False

    def modify_health(self, amount):
        self.health += amount
    
    def attack(self, target):

        pass

    def defend(self, target):

        pass

    def death_check(self):
        if self.health < 1:
            self.is_dead = True

    def who_am_i(self):
        print(f'Name: {self.name}\nHealth: {self.health}\nDamage: {self.damage}\n')


class Adventurer(Pawn):

    def __init__(self, stats):

        self.equipment = {
            'hands': [],
            'armor': None,
            'amulet': None,
        }

        self.cards = []

        super().__init__(stats)

    def draw(self, deck):

        while len(self.cards) < 5:
            self.cards.append(deck.draw())

    def modify_damage(self, amount):
        self.damage += amount


    def modify_defense(self, amount):
        self.defense += amount

    def roll_check(self, roll_to_beat):
        return random.randint(1,6) >= roll_to_beat

    def equip(self, slot, card):
        pass

    #could we just make this the default for the equip method?
    def unequip(self, slot):
        pass

    #trying to decide whether the Adventurer class (and Dungeon) need this method
    #probably because we would have to change the hand (self.cards) property in tandem
    def discard(self, card):
        #i think we have this method call card.discard() as well.
        pass

    #instead of setting a default number of attacks, i think we just have basic attack as a bool
    #you have either attacked or not. then create a stack of attack instances that we can add to
    #with special keywords like cleave or double spell


class Dungeon:
    def __init__(self):
        self.monsters = []
        self.traps = []
        self.hand = []


class Encounter:
    def __init__(self):
        self.power_level = 0

        self.adventurer_board = None
        self.dungeon_board = []