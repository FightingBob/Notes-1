

def log(func):
    def decorator():
        print("call %s()" % func.__name__)
        return func()
    return decorator


@log
def now():
    print("2018/2/2")

now()

"""
just like
"""
def log(func):
    print("call %s()" % func.__name__)
    func()



def now():
    print("2018/2/2")

log(now)

print("----")
def a(f):
    def decorator():
        print(f)
        print(f.__name__)
        return f() # 执行 传进来的函数
    f() # 用到装饰器时就会执行这个 f()
    return decorator

@a
def b():
    print("2")

# b()