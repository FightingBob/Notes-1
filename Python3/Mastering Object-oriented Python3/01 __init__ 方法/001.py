

class Card:
    def __init__(self, rank, suit):
        self.suti = suit
        self.rank = rank
        self.hard, self.point = self._point


class NumberCard(Card):
    def _point(self):
        return int(self.rank), int(self.rank)


class AceCard(Card):
    def _point(self):
        return 1, 11


class FaceCard(Card):
    def _point(self):
        return 10, 10

# a = A()
# print(a)