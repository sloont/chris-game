import random, csv

from CardClasses import AdventurerCard, DungeonCard

class Deck:
    def __init__(self, file):
        self.cards = []
        self.file = file

        

#i think we can further consolidate these child classes when there is a more clear cut print structure.

class AdventurerDeck(Deck):
    def __init__(self,file):

        super().__init__(file)

        with open(file, newline='') as deckCSV:
            reader = csv.DictReader(deckCSV, delimiter=',')
            for row in reader:
                self.cards.append(AdventurerCard(row))

    def deck_list(self):
        for card in self.cards:
            print(f'{card.name}\n{card.id}\n{card.type}\n{card.value}\n{card.description}\n\n')

class DungeonDeck(Deck):
    def __init__(self,file):

        super().__init__(file)

        with open(file, newline='') as deckCSV:
            reader = csv.DictReader(deckCSV, delimiter=',')
            for row in reader:
                self.cards.append(DungeonCard(row))

    def deck_list(self):
        for card in self.cards:
            print(f'{card.name}\n{card.id}\n{card.type}\n{card.damage}\n{card.health}\n{card.power}\n\n')