class Adventurer:
    def __init__(self):
        self.health = 20
        self.equipment = {
            'hands': [],
            'armor': None,
            'amulet': None,
        }
        self.damage = 0
        self.defense = 0

        for item in self.equipment['hands']:
            if item.type['type'] == 'damage':
                self.damage += item.type['amount']
            if item.type['type'] == 'defense':
                self.defense += item.type['amount']
        self.hand = []

    def modify_damage(self, amount):
        self.damage += amount
    def modify_health(self, amount):
        self.health += amount
    def modify_defense(self, amount):
        self.defense += amount
    def modify_swings(self):
        pass
    def roll_check(self):
        pass
    def toggle_item(self):
        pass
    def discard(self):




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