# 实现一个向量类Vector
# 使其实现 + - *

from math import hypot


class Vector:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __sub__(self, other):
        x = self.x - other.x
        y = self.y - other.x
        return Vector(x, y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

    def __abs__(self):
        # 返回欧氏方程，sqrt（x * x + y * y）
        return hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    def __repr__(self):
        return "Vector(%r, %r)" % (self.x, self.y)
        # return "Vector({}, {})".format(self.x, self.y)


# __init__
v1 = Vector(1, 2)
print(v1)

# __add__
v2 = v1 + v1
print(v2)

# __sub__
v3 = v2 - v1
print(v3)

# __mul__
v4 = v1 * 2
print(v4)

# __bool__
print(bool(v4))
