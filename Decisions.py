import random



class Dungeon_AI:
    #this will pull highest single value with priority over a higher PL on board consisting of lower single value monsters
    def __init__(self, encounter):
        self.encounter_power = 8 #encounter.getPL()  8 is test con
        self.power_on_board = 0

    def priority_summon(self, dungeon, encounter):
        monsters = []    
        for card in dungeon.cards:
                if card.type == 'monster':
                    monsters.append(card)
        
        for card in monsters:
            print(card.name, card.power)
        
        #fake stop condition
        z = 1
        while z <= 7:
        
            i = 0
            
            if self.power_on_board < self.encounter_power and len(monsters) > 0:
                maxPL = 0
                flag = False
                for x in range(0, len(monsters)):
                    
                    if self.power_on_board + monsters[x].power <= self.encounter_power and monsters[x].power > maxPL:
                            i = x
                            maxPL = monsters[i].power
                            flag = True

                
                if flag or self.power_on_board + monsters[i].power <= self.encounter_power:
                    dungeon.summon(monsters[i], encounter)
                    monsters.remove(monsters[i])
                    self.power_on_board += maxPL
                
            z += 1



class Adventurer_AI:

    def __init__(self, adventurer):
        pass
