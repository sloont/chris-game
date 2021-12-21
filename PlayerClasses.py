class Adventurer:
    def __init__(self):
        self.health = 20
        self.equipment = {
            'hands': [],
            'armor': None,
            'amulet': None,
        }
        self.hand = []



class Dungeon:
    def __init__(self):
        self.monsters = []
        self.traps = []
        self.hand = []


class Encounter:
    def __init__(self):
        self.powerLevel = 0

        self.adventurerBoard = None
        self.dungeonBoard = []