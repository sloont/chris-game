import csv

from CardClasses import AdventurerCard 
deck = []
with open('adventurer-deck.csv', newline='') as adventurerDeck:
    adventurerReader = csv.DictReader(adventurerDeck, delimiter=',')
    for row in adventurerReader:
        deck.append(AdventurerCard(row))

for card in deck:
    print(f'{card.name}\n{card.id}\n{card.type}\n{card.value}\n{card.description}\n\n')