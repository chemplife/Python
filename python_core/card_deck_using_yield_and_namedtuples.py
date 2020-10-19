from collections import namedtuple
from itertools import cycle

Cards = namedtuple('Cards', 'Suit Rank')

def card_deck():
	ranks = tuple(str(num) for num in range(2,11)) + tuple('JQKA')
	suits = ('Spades', 'Hearts', 'Diamonds', 'Clubs')

	for suit in suits:
		for rank in ranks:
			yield Cards(suit, rank)

print('Deck of Cards:\n',list(card_deck()))

hands = [list() for _ in range(4)]

index_of_hand = 0

for card in card_deck():
	index_of_hand = index_of_hand % 4
	hands[index_of_hand].append(card)
	index_of_hand += 1

print('All hands:\n', hands)

# Using cycle function
print('\n-------------------------------- Cycle --------------------------------')

hands = [list() for _ in range(4)]

index_cycle = cycle([0,1,2,3])

for card in card_deck():
	hands[next(index_cycle)].append(card)

# By list comprehension: hands = [ for card in card_deck()]
print('All hands:\n', hands)

# OR we can cycle through the hand directly

hands = [list() for _ in range(4)]
hands_cycle = cycle(hands)
for card in card_deck():
	next(hands_cycle).append(card)

print('All hands:\n', hands)