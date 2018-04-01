from array import array
import math


class Vector2d:
    typecode = 'd'

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        class_name = type(self).__name__
        return '{} {!r}, {!r}'.format(class_name, *self)

    def __str__(self):
        return "str ({}, {})".format(*self)

    def __bytes__(self):
        return (bytes([ord(self.typecode)]) +
                bytes(array(self.typecode, self)))

    def __eq__(self, other):
        return tuple(self) == tuple(other)

    def __abs__(self):
        return math.hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    @classmethod
    def frombytes(cls, octets):
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(*memv)

    def __format__(self, format_spec=''):
        # components = (format(c, format_spec) for c in self)
        # return '{}, {}'.format(*components)
        if format_spec.endswith('p'):
            format_spec = format_spec[:-1]
            coords = (abs(self), self.angle())
            out_fmt = '<{}, {}>'
        else:
            coords = self
            out_fmt = '({}, {})'
        components = (format(c, format_spec) for c in coords)
        return out_fmt.format(*components)

    def angle(self):
        return math.atan2(self.x, self.y)

    def __iter__(self):
        return (i for i in (self.x, self.y))

    def __hash__(self):
        return hash(tuple(self))


v1 = Vector2d(1, 2)
print(abs(v1))
print(bytes(v1))
print(format(v1, '0.4f'))
print(v1.angle())
print(format(v1, '0.4fp'))
print(hash(v1))
print(str(v1))
for v in v1:
    print(v)

# __iter__ 将Vector2d 对象变为可迭代的
# 魔法方法里面传递的self 是类的实例 等同于 v1对象
