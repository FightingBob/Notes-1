"""
registry = []


def register(func):
    print('running regiter(%s)' % func)
    registry.append(func)
    return func


@register
def f1():
    print('running f1()')
"""
# 不带参数的装饰器


registry = set()


def register(active=True):
    def decorate(func):
        print('running register (active=%s) - > decorate(%s)' % (active, func))
        if active:
            registry.add(func)
        else:
            registry.discard(func)
        return func

    return decorate


@register()
def f1():
    print('running f1()')


if __name__ == '__main__':
    print('running main')
    f1()
