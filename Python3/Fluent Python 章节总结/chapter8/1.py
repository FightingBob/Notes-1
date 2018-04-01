t1 = (1, 3, [30, 40])
t1[2].append(20)
print(t1)

l1 = [3, [55, 44], (1, 2, 3)]
l2 = list(l1)
print(l2 is l1, l2 == l1)
# list() 创建副本

l2 = l1[:]
print(l2 is l1, l2 == l1)
# l1[:] 创建副本

print('-' * 20)

# 但list() 和 l1[:] 是浅复制仅仅复制了最外围的容器
# 当元素的引用为可变序列时， 会发生意象不到的问题


l2 = l1[:]
print(l1)
print(l2)

l1[1].append(20)
print(l1)
print(l2)


# 现在更改了l1中索引为1的list
# l2 是l1 的副本 但是l2 依旧改变了
# 这就是浅复制： 仅仅复制了最外围的容器


class User:
    id = None
    name = None

    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __repr__(self):
        return "<User %r>" % self.name


l = []
for i in range(1, 11):
    user = User(id=i, name=i)
    l.append(user)

print(l)
l3 = l[:]
print(l3)

l[0].name = 2
print(l)
print(l3)
