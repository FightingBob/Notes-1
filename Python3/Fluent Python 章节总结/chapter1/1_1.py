import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])

card = Card("a", 'b')
print(card)
print(card.rank)
print(card.suit)
print(list('JQKA'))
print([str(n) for n in range(2, 11)] + list('JQKA'))