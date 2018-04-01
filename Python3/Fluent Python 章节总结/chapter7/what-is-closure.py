"""
实现
avg(10)
10
avg(11)
11.5
avg(12)
11.0
这样一个函数你会如何实现?
"""


# 实现1： 类
class Averager:
    def __init__(self):
        self.series = []

    def __call__(self, new_value):
        self.series.append(new_value)
        total = sum(self.series)
        return total / len(self.series)


avg = Averager()

print(avg(10))
print(avg(11))
print(avg(12))

print("-" * 20)


# 实现2：高阶函数
def make_averager():
    series = []

    def averager(new_value):
        series.append(new_value)
        total = sum(series)
        return total / len(series)

    return averager


avg = make_averager()

print(avg(10))
print(avg(11))
print(avg(12))

# 问题是avg 就是make_averager
# 返回的是averager 调用的时候返回的是 total / len(series)
# averger 函数作用域是如何找到 series 的 毕竟 make_averager 早return 了 averager


print(avg.__code__.co_varnames)  # 局部变量
print(avg.__code__.co_freevars)  # 自由变量

print(avg.__closure__)
print(avg.__closure__[0].cell_contents)

# 综上，闭包是一种函数，它会保留定义函数时存在的自由变量的绑定，
# 这样调用函数时，虽然定义作用域不可用了，但是仍能使用那些绑定
