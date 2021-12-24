from Deck import AdventurerDeck, DungeonDeck
from PlayerClasses import Adventurer, Dungeon

ADVENTURER_CSV = 'adventurer-deck.csv'
DUNGEON_CSV = 'dungeon-deck.csv'

adventurer_deck = AdventurerDeck(ADVENTURER_CSV)
dungeon_deck = DungeonDeck(DUNGEON_CSV)

adventurer_deck.shuffle()
dungeon_deck.shuffle()

adventurer = Adventurer({
    'name': 'Topher',
    'health': 20,
    'damage': 1,
})

dungeon = Dungeon()

adventurer.who_am_i()

adventurer.draw(adventurer_deck)
dungeon.draw(dungeon_deck)

for card in adventurer.cards:
    print(f'{card.name}')

print('\n\n')

for card in dungeon.cards:
    print(f'{card.name}')

