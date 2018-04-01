class Vector:

    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y


v = Vector(1, 2)
print(v.x)
# 使 属性 x y 无法被修改
print(v.__dict__)
