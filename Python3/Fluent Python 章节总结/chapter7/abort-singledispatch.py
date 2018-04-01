from functools import singledispatch
from collections import abc
import numbers
import html


@singledispatch
def htmlize(obj):
    content = html.escape(repr(obj))
    return '<pre>{}<.pre>'.format(content)


@htmlize.register(str)
def _(text):
    content = html.escape(text).replace('\n', '<br>\n')
    return '<p>{0}</p>'.format(content)


@htmlize.register(numbers.Integral)
def _(n):
    return '<pre>{0} (0x{0:x})</pre>'.format(n)


@htmlize.register(tuple)
@htmlize.register(abc.MutableSequence)
def _(seq):
    inner = '<l1>\n</li>'.join(htmlize(item) for item in seq)
    return '<ul>\n<l1>' + inner + '<li>\n<.l1>'


# 。@singledispath 的优点是支持模块化扩展：各个模块可以为
# 它支持的各个类型注册一个专门函数

if __name__ == '__main__':
    print(htmlize(1))
