# 今天看到帖子说Python是没有变量作用域这个东东的
# 特来验证一下


def validation1():
    for i in range(1, 11):
        print(i)
    print("------")
    # 可见在for 循环的外部依旧可以访问带 i 这个变量
    # 且 i的值 为 最后赋值的值
    print(i)


try:
    print(i)
except NameError as e:
    # i is not define
    print(e)

"""
百度之后发现python是存在4种作用域的
1. L （Local） 局部作用域
2. E （Enclosing） 闭包函数外的函数中
3. G （Global） 全局作用域
4. B （Built-in） 内建作用域
"""

if __name__ == '__main__':
    validation1()
