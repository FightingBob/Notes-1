def arg(*args):
    print("args is {}".format(args))
    for index, item in enumerate(args):
        print("{}->{}".format(index, item))


def kwargs(**kwargs):
    print("kwargs is {}".format(kwargs))
    for k in kwargs:
        print("key is {}, value is {}".format(k, kwargs[k]))


if __name__ == '__main__':
    arg((1, 2, 3))
    arg('1', '2', '3')
    arg(*(1, 2, 3))
    arg(*{"one": 1, "two": 2})
    # 可以看到args是一个元祖
    # 允许 你传入任意参数
    # 也可以使用 * iterable 传入 避免写很多参数

    print("-" * 20)

    kwargs(one=1, two=2)
    kwargs(**{"one": 1, "two": 2})
    # 可以看到**kwargs 是一个字典
    # 允许你传入 one=1, two=2 这种

    # 需要注意的是 当一起用的时 *args, **kwargs
    # *args 需要在 **kwargs 前面
