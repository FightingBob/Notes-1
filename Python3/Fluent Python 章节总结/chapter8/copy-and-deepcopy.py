import copy


class Bus:

    def __init__(self, passengers=None):
        # 不要使用可变类型的参数作为默认值
        # 小心可变对象
        if passengers is None:
            self.passengers = []
        else:
            self.passengers = list(passengers)

    def pick(self, name):
        self.passengers.append(name)

    def drop(self, name):
        self.passengers.remove(name)

    def __repr__(self):
        return "<Bus %r>" % str(self.passengers)


if __name__ == '__main__':
    bus1 = Bus(['a', 'b', 'c', 'd'])
    print(bus1)
    bus2 = copy.copy(bus1)
    bus3 = copy.deepcopy(bus1)
    print(id(bus1), id(bus2), id(bus3))
    bus1.drop('a')
    print(bus2)
    print(bus3)
    # 可见bus3 是深复制 引用的是另一个列表
