from Deck import AdventurerDeck, DungeonDeck
from PlayerClasses import Pawn, Adventurer

ADVENTURER_CSV = 'adventurer-deck.csv'
DUNGEON_CSV = 'dungeon-deck.csv'

adventurer_deck = AdventurerDeck(ADVENTURER_CSV)
dungeon_deck = DungeonDeck(DUNGEON_CSV)

adventurer_deck.shuffle()

adventurer = Adventurer({
    'name': 'Topher',
    'health': 20,
    'damage': 1,
})

adventurer.who_am_i()
print(len(adventurer_deck.cards) + 1)
adventurer.draw(adventurer_deck)
for card in adventurer.cards:
    print(f'{card.name}')

print(len(adventurer_deck.cards) + 1)
