import csv

from CardClasses import AdventurerCard, DungeonCard
adventurerDeck = []
dungeonDeck = []

with open('adventurer-deck.csv', newline='') as adventurerDeckCSV:
    adventurerReader = csv.DictReader(adventurerDeckCSV, delimiter=',')
    for row in adventurerReader:
        adventurerDeck.append(AdventurerCard(row))

for card in adventurerDeck:
    print(f'{card.name}\n{card.id}\n{card.type}\n{card.value}\n{card.description}\n\n')


with open('dungeon-deck.csv', newline='') as dungeonDeckCSV:
    dungeonReader = csv.DictReader(dungeonDeckCSV, delimiter=',')
    for row in dungeonReader:
        dungeonDeck.append(DungeonCard(row))

for card in dungeonDeck:
    print(f'{card.name}\n{card.id}\n{card.type}\n{card.damage}\n{card.health}\n{card.power}\n\n')