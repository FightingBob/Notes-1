# 迭代器

list = [1, 2, 3, 4]

for i in list:
    print(i)

# 迭代器将值放在内存中, 存在太多值时会消耗太多内存

# generators 生成器

print('-' * 20)
generators = (x for x in list)
for g in generators:
    print(g)

for g in generators:
    print(g)

# 生成器只能迭代一次, 其值并不是全部存放在内存中
# 只在需要调用的时候在内存中生成
print('-' * 20)


def create_generators():
    list = range(5)
    for i in list:
        yield i ** 2


generators = create_generators()

for i in generators:
    print(i)
