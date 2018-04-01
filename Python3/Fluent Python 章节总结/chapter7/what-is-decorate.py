"""
@decorate
def target():
    print("running target")

==

def target():
    print(" running target")

target = decorate(target)
"""


# example1
def deco(func):
    def inner():
        print("running inner")

    return inner


@deco
def target():
    print("running target")


target()

print(target)
# ---------
# 装饰器是一个语法糖
# 传入一个函数， 返回一个装饰了的函数
