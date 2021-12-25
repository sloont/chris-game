import random
from Attack import Attack

class Pawn:
    #we could honestly just use this parent as the class for monsters
    def __init__(self,stats):
        self.name = stats['name']
        self.health = int(stats['health'])
        self.damage = int(stats['damage'])
        self.defense = 0
        self.can_attack = True
        self.is_dead = False

    def get_name(self):
        return self.name
    def get_health(self):
        return self.health
    def get_damage(self):
        return self.damage
    def get_defense(self):
        return self.defense

    def modify_health(self, amount):
        self.health += amount
    
    def attack(self, target):
        attack = Attack(self, target)
        attack.attack(target)
        return attack.log_combat()

    def defend(self, target):
#
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
        self.cards = []

    def draw(self, deck):
        
        while len(self.cards) < 7:
            self.cards.append(deck.draw())

    def summon(self, card, encounter):
        encounter.dungeon_summon(card)
        self.cards.remove(card)


class Encounter:
    def __init__(self, adventurer, dungeon):
        self.power_level = 0

        self.adventurer = adventurer
        self.dungeon = dungeon
        self.dungeon_board = []
        self.adventurer_board = []


    def dungeon_summon(self, card):
        self.dungeon_board.append(Pawn({
            'name': card.get_name(),
            'health': card.get_health(),
            'damage': card.get_damage(),
        }))

    def update_adventurer(self, adventurer):
        self.adventurer_board = [adventurer]