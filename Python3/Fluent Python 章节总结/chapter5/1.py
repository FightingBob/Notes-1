import random


def factorial(n):
    """return n!"""
    return 1 if n < 2 else n * factorial(n - 1)


print(factorial(42))

print(factorial.__doc__)


class BingoCage:

    def __init__(self, items):
        self._items = list(items)
        random.shuffle(self._items)

    def pick(self):
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError('pick from empty BingoCage')

    def __call__(self):
        return self.pick()


items = [1, 2, 34]
bingo = BingoCage(items)
print(bingo())
print(bingo.pick())
