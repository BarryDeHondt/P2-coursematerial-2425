from util import *



group_by_suit = lambda cards: group_by(cards, lambda card: card.suit)
group_by_value =  lambda cards: group_by(cards, lambda card: card.value)
partition_by_color = lambda cards: partition(cards, lambda card: card.suit in ['spades', 'clubs'])
