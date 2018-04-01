# 计算移动平均值高阶函数

"""
def make_averager():
    count = 0
    total = 0

    def averager(new_value):
        count += 1
        total += new_value
        return total / count

    return averager


avg = make_averager()
avg(10)

error:
Traceback (most recent call last):
  File "E:/杂项/FluentPython/chapter7/what-is-nonlocal.py", line 17, in <module>
    avg(10)
  File "E:/杂项/FluentPython/chapter7/what-is-nonlocal.py", line 9, in averager
    count += 1
UnboundLocalError: local variable 'count' referenced before assignment

原因：
当 count 是数字或任何不可变类型时，count += 1 语句的作
用其实与 count = count + 1 一样。因此，我们在 averager 的定义
体中为 count 赋值了，这会把 count 变成局部变量。total 变量也受
这个问题影响。
"""


def make_averager():
    count = 0
    total = 0

    def averager(new_value):
        nonlocal count, total
        count += 1
        total += new_value
        return total / count

    return averager


avg = make_averager()
print(avg(10))
print(avg(11))
print(avg(12))
# 7.7
