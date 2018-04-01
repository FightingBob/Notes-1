# page is 67

# 列表推导

from collections import namedtuple


def to_list():
    s = "123456789"
    l = [i for i in s]
    return l


def to_list_unusual():
    s = "123456789"
    l = []
    for i in s:
        l.append(i)
    return l


def use_to_list():
    s = "123456789"
    l = [i ** 3 for i in s]
    return l


def tuple_come():
    # 生成器逐个生成元素
    s = "123456789"
    t = (int(i) ** 2 for i in s)
    return t


def come():
    *a, b = range(5)
    print(a, b)


def lan():
    # 具名元组
    buglan = namedtuple('buglan', ['age', 'weight'])
    print(buglan)
    b = buglan('22', '120')
    print(b)
    print(b._fields)
    print(b._asdict())


def come2(l):
    l.append(4)
    return None


if __name__ == '__main__':
    print(to_list())
    print(to_list_unusual())
    for i in tuple_come():
        print(i)
    come()
    lan()
    l = [1, 2, 3]
    come2(l)
    print(l)
