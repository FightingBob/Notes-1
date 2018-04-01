# 如果你要构建一个纸牌类你会如何做呢?
# 建立一个 数字型 字母形 王 还是什么
# 我可以说无从下手
# 让我来看下实例

import collections

from random import choice

Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck:
    # ranks 扑克牌的A, K, 2, 3...
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    # 扑克牌的花色
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                       for rank in self.ranks]
        # 仅通过列表推到就生成了 52 个扑克牌对象 并存在其必须的属性

    def __len__(self):
        return len(self._cards)
        # 返回 纸牌的数量

    def __getitem__(self, position):
        return self._cards[position]


f = FrenchDeck()

for card in f:
    # 仅实现了__getitem__ f 就变成可以迭代的了
    print(card)
print("------")
print(choice(f))
# 随机抽取一张牌

# 可以使用 in 操作符 / __contains__
print(Card("A", "hearts") in f)

print(Card("A", "bearts") in f)
