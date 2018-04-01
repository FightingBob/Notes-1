from decorate1 import clock
import functools

"""
[0.00000064s] fibonacci(0) -> 0
[0.00000064s] fibonacci(1) -> 1
[0.00006094s] fibonacci(2) -> 0
[0.00000032s] fibonacci(1) -> 1
[0.00000064s] fibonacci(0) -> 0
[0.00000032s] fibonacci(1) -> 1
[0.00002053s] fibonacci(2) -> 0
[0.00004041s] fibonacci(3) -> 0
[0.00012188s] fibonacci(4) -> 0
[0.00000032s] fibonacci(1) -> 1
[0.00000032s] fibonacci(0) -> 0
[0.00000032s] fibonacci(1) -> 1
[0.00001860s] fibonacci(2) -> 0
[0.00003753s] fibonacci(3) -> 0
[0.00000032s] fibonacci(0) -> 0
[0.00000064s] fibonacci(1) -> 1
[0.00001860s] fibonacci(2) -> 0
[0.00000032s] fibonacci(1) -> 1
[0.00000064s] fibonacci(0) -> 0
[0.00000032s] fibonacci(1) -> 1
[0.00001956s] fibonacci(2) -> 0
[0.00003785s] fibonacci(3) -> 0
[0.00007409s] fibonacci(4) -> 0
[0.00012957s] fibonacci(5) -> 0
[0.00027005s] fibonacci(6) -> 0
[0.00000032s] fibonacci(1) -> 1
[0.00000032s] fibonacci(0) -> 0
[0.00000032s] fibonacci(1) -> 1
[0.00001892s] fibonacci(2) -> 0
[0.00003720s] fibonacci(3) -> 0
[0.00000032s] fibonacci(0) -> 0
[0.00000032s] fibonacci(1) -> 1
[0.00001860s] fibonacci(2) -> 0
[0.00000032s] fibonacci(1) -> 1
[0.00000032s] fibonacci(0) -> 0
[0.00000064s] fibonacci(1) -> 1
[0.00001860s] fibonacci(2) -> 0
[0.00003688s] fibonacci(3) -> 0
[0.00007345s] fibonacci(4) -> 0
[0.00012829s] fibonacci(5) -> 0
[0.00000000s] fibonacci(0) -> 0
[0.00000032s] fibonacci(1) -> 1
[0.00001828s] fibonacci(2) -> 0
[0.00000032s] fibonacci(1) -> 1
[0.00000032s] fibonacci(0) -> 0
[0.00000064s] fibonacci(1) -> 1
[0.00002213s] fibonacci(2) -> 0
[0.00004105s] fibonacci(3) -> 0
[0.00007730s] fibonacci(4) -> 0
[0.00000032s] fibonacci(1) -> 1
[0.00000032s] fibonacci(0) -> 0
[0.00000032s] fibonacci(1) -> 1
[0.00001860s] fibonacci(2) -> 0
[0.00003720s] fibonacci(3) -> 0
[0.00000032s] fibonacci(0) -> 0
[0.00000032s] fibonacci(1) -> 1
[0.00001828s] fibonacci(2) -> 0
[0.00000032s] fibonacci(1) -> 1
[0.00000064s] fibonacci(0) -> 0
[0.00000032s] fibonacci(1) -> 1
[0.00001956s] fibonacci(2) -> 0
[0.00003785s] fibonacci(3) -> 0
[0.00007409s] fibonacci(4) -> 0
[0.00012893s] fibonacci(5) -> 0
[0.00022419s] fibonacci(6) -> 0
[0.00037012s] fibonacci(7) -> 0
[0.00065845s] fibonacci(8) -> 0
[0.00000032s] fibonacci(1) -> 1
[0.00000032s] fibonacci(0) -> 0
[0.00000032s] fibonacci(1) -> 1
[0.00001828s] fibonacci(2) -> 0
[0.00003688s] fibonacci(3) -> 0
[0.00000000s] fibonacci(0) -> 0
[0.00000032s] fibonacci(1) -> 1
[0.00001860s] fibonacci(2) -> 0
[0.00000032s] fibonacci(1) -> 1
[0.00000032s] fibonacci(0) -> 0
[0.00000032s] fibonacci(1) -> 1
[0.00001860s] fibonacci(2) -> 0
[0.00003656s] fibonacci(3) -> 0
[0.00007345s] fibonacci(4) -> 0
[0.00012797s] fibonacci(5) -> 0
[0.00000032s] fibonacci(0) -> 0
[0.00000064s] fibonacci(1) -> 1
[0.00001860s] fibonacci(2) -> 0
[0.00000032s] fibonacci(1) -> 1
[0.00000032s] fibonacci(0) -> 0
[0.00000032s] fibonacci(1) -> 1
[0.00001860s] fibonacci(2) -> 0
[0.00003688s] fibonacci(3) -> 0
[0.00007248s] fibonacci(4) -> 0
[0.00000032s] fibonacci(1) -> 1
[0.00000032s] fibonacci(0) -> 0
[0.00000032s] fibonacci(1) -> 1
[0.00001860s] fibonacci(2) -> 0
[0.00003688s] fibonacci(3) -> 0
[0.00000032s] fibonacci(0) -> 0
[0.00000032s] fibonacci(1) -> 1
[0.00001828s] fibonacci(2) -> 0
[0.00000032s] fibonacci(1) -> 1
[0.00000353s] fibonacci(0) -> 0
[0.00000032s] fibonacci(1) -> 1
[0.00002277s] fibonacci(2) -> 0
[0.00004041s] fibonacci(3) -> 0
[0.00007633s] fibonacci(4) -> 0
[0.00013086s] fibonacci(5) -> 0
[0.00022162s] fibonacci(6) -> 0
[0.00036691s] fibonacci(7) -> 0
[0.00000032s] fibonacci(0) -> 0
[0.00000032s] fibonacci(1) -> 1
[0.00001860s] fibonacci(2) -> 0
[0.00000000s] fibonacci(1) -> 1
[0.00000000s] fibonacci(0) -> 0
[0.00000032s] fibonacci(1) -> 1
[0.00001860s] fibonacci(2) -> 0
[0.00003624s] fibonacci(3) -> 0
[0.00007248s] fibonacci(4) -> 0
[0.00000032s] fibonacci(1) -> 1
[0.00000032s] fibonacci(0) -> 0
[0.00000032s] fibonacci(1) -> 1
[0.00001828s] fibonacci(2) -> 0
[0.00003592s] fibonacci(3) -> 0
[0.00000032s] fibonacci(0) -> 0
[0.00000032s] fibonacci(1) -> 1
[0.00001828s] fibonacci(2) -> 0
[0.00000064s] fibonacci(1) -> 1
[0.00000032s] fibonacci(0) -> 0
[0.00000064s] fibonacci(1) -> 1
[0.00002181s] fibonacci(2) -> 0
[0.00005869s] fibonacci(3) -> 0
[0.00152923s] fibonacci(4) -> 0
[0.00158375s] fibonacci(5) -> 0
[0.00167355s] fibonacci(6) -> 0
[0.00000032s] fibonacci(1) -> 1
[0.00000032s] fibonacci(0) -> 0
[0.00000064s] fibonacci(1) -> 1
[0.00001828s] fibonacci(2) -> 0
[0.00003688s] fibonacci(3) -> 0
[0.00000032s] fibonacci(0) -> 0
[0.00000032s] fibonacci(1) -> 1
[0.00001796s] fibonacci(2) -> 0
[0.00000032s] fibonacci(1) -> 1
[0.00000032s] fibonacci(0) -> 0
[0.00000032s] fibonacci(1) -> 1
[0.00001796s] fibonacci(2) -> 0
[0.00003656s] fibonacci(3) -> 0
[0.00007216s] fibonacci(4) -> 0
[0.00012669s] fibonacci(5) -> 0
[0.00000032s] fibonacci(0) -> 0
[0.00000064s] fibonacci(1) -> 1
[0.00001796s] fibonacci(2) -> 0
[0.00000000s] fibonacci(1) -> 1
[0.00000032s] fibonacci(0) -> 0
[0.00000032s] fibonacci(1) -> 1
[0.00001828s] fibonacci(2) -> 0
[0.00003656s] fibonacci(3) -> 0
[0.00007184s] fibonacci(4) -> 0
[0.00000032s] fibonacci(1) -> 1
[0.00000032s] fibonacci(0) -> 0
[0.00000032s] fibonacci(1) -> 1
[0.00001828s] fibonacci(2) -> 0
[0.00004041s] fibonacci(3) -> 0
[0.00000032s] fibonacci(0) -> 0
[0.00000032s] fibonacci(1) -> 1
[0.00001828s] fibonacci(2) -> 0
[0.00000032s] fibonacci(1) -> 1
[0.00000064s] fibonacci(0) -> 0
[0.00000032s] fibonacci(1) -> 1
[0.00001924s] fibonacci(2) -> 0
[0.00003720s] fibonacci(3) -> 0
[0.00007281s] fibonacci(4) -> 0
[0.00013054s] fibonacci(5) -> 0
[0.00021970s] fibonacci(6) -> 0
[0.00036370s] fibonacci(7) -> 0
[0.00205490s] fibonacci(8) -> 0
[0.00243977s] fibonacci(9) -> 0
[0.00311811s] fibonacci(10) -> 0
"""


# 发现其存在很多相同的函数， 但这些相同的函数都不是必须需要运算的
# functools.lru_cache 是非常实用的装饰器，它实现了备忘
# （memoization）功能。这是一项优化技术，它把耗时的函数的结果保存
# 起来，避免传入相同的参数时重复计算

@clock
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 2) * fibonacci(n - 1)


@functools.lru_cache()
@clock
def fibonacci2(n):
    if n < 2:
        return n
    return fibonacci2(n - 2) * fibonacci2(n - 1)


"""
[0.00000032s] fibonacci2(0) -> 0
[0.00000032s] fibonacci2(1) -> 1
[0.00003688s] fibonacci2(2) -> 0
[0.00000096s] fibonacci2(3) -> 0
[0.00005741s] fibonacci2(4) -> 0
[0.00000096s] fibonacci2(5) -> 0
[0.00007762s] fibonacci2(6) -> 0
[0.00000096s] fibonacci2(7) -> 0
[0.00009750s] fibonacci2(8) -> 0
[0.00000064s] fibonacci2(9) -> 0
[0.00011707s] fibonacci2(10) -> 0
"""

# 明显需要传入的参数不会是重复的了
# 效率变得更高了

if __name__ == '__main__':
    # fibonacci(32)
    fibonacci2(32)
