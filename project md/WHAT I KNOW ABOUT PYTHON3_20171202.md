# 最了解自己的是自己, 最不了解的也是自己
Base in Python3
> It is better tu konw yourself

### Round number
```python
>>> a = 1
>>> a
1
>>> type(a)
<class 'int'>
>>> 
```
### string
```python
>>> a = "a"
>>> a
'a'
>>> type(a)
<class 'str'>
```
### list
```python
>>> a = [1,2,"a"]
>>> a
[1, 2, 'a']
>>> type(a)
<class 'list'>
```
### set
```python
>>> a = {"1", "a", 100}
>>> a
{100, 'a', '1'}
>>> type(a)
<class 'set'>
```
> I found i didn't understand set or tuple
> my founddation is weak

### Bulid-in Functions
```python
# abs(x)
>>> abs(-1)
1
# all(iterable)
>>> a = [1, 2,"a", 1.2, [1]]
>>> type(a)
<class 'list'>
>>> all(a)
True
>>> a.append([])
>>> a
[1, 2, 'a', 1.2, [1], []]
>>> all(a)
False
"""
# Equivalent to:

def all(iterable):
    for element in iterable:
        if not element:
            return Flase
    return True
"""
# any(itrtable)
>>> a = [1, 2, 'a', 1.2, [1], []]
>>> any(a)
True
>>> b = [[],[]]
>>> any(b)
False
>>>
"""
# Equivatent to:
def any(iterable):
    for element in iterable:
        if element:
            return True
    return Fase
""" 
# bin(x)
>>> bin(1)
'0b1'
>>> bin(2)
'0b10'
>>> bin(a)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    bin(a)
TypeError: 'list' object cannot be interpreted as an integer
# integer converts to binary

# format (str.format())

>>> "{}".format("a")
'a'
>>> "{}  {}".format("a", "b")
'a  b'
# user dict
>>> c = {"name":"lan", "age": "18"}
>>>> "name: {name}, age: {age}".format(**c)
'name: lan, age: 18' 
# use list '0' is necessary
>>> d = [1, 2]
>>> "{0[0]} + {0[1]}".format(d)
'1 + 2'
...
# help([object])
>>>> help('sys')
...
>>>> help('os')
...
>>>> a = [1, 2, 3]
>>>> help(a)
...

# int
"""
# 原型
class int(x, base=10)
# base 默认为10禁止
"""

int ()
Out[3]: 0
int(3)
Out[4]: 3
int(3.6)
Out[5]: 3
int('12', 16)
Out[6]: 18
int('0xa', 16)
Out[7]: 10
int('10', 8)
Out[8]: 8

# input()

a = input("input:")
input:>? 123
type(a)
Out[11]: str

# isinstance(object, classinfo)
# object--实例对象 classinfo--类名

In[13]: a = 2
In[14]: isinstance(a, int)
Out[14]: True
In[15]: isinstance(a, str)
Out[15]: False
In[16]: isinstance(a, (int, str, list))
Out[16]: True
In[17]: isinstance(a, {int, str})
Traceback (most recent call last):
  File "D:\python35\lib\site-packages\IPython\core\interactiveshell.py", line 2910, in run_code
    exec(code_obj, self.user_global_ns, self.user_ns)
  File "<ipython-input-17-340eb7c782e6>", line 1, in <module>
    isinstance(a, {int, str})
TypeError: isinstance() arg 2 must be a type or tuple of types\

# len() --返回对象长度

In[2]: a = [1, 2, 3]
In[3]: len(a)
Out[3]: 3
In[4]: b = "123456"
In[5]: len(b)
Out[5]: 6

# list() tuple -> list

In[6]: a = (1, 2, 3)
In[7]: a.append("3")
Traceback (most recent call last):
  File "D:\python35\lib\site-packages\IPython\core\interactiveshell.py", line 2910, in run_code
    exec(code_obj, self.user_global_ns, self.user_ns)
  File "<ipython-input-7-421aa5b365fb>", line 1, in <module>
    a.append("3")
AttributeError: 'tuple' object has no attribute 'append'
In[8]: b = list(a)
In[9]: b
Out[9]: [1, 2, 3]
In[10]: b.append("4")
In[11]: b
Out[11]: [1, 2, 3, '4']

# class long(x, base=10)
# 将数字或字符串转换为一个长整型。

# map(function, iterable, ...)

a = [1, 2, 3]
def square(x):
    return x**2
b = map(square, a)
for i in b:
    print(i)

1
4
9

# max(x, y, z, ...)

max(1, 3, 4)
Out[2]: 4
max([1,2,3])
Out[3]: 3
max((1,2,3))
Out[4]: 3

# min(x, y, z, ...)

min(1, 3, 4)
Out[5]: 1
min({1,2,3})
Out[6]: 1

# iter(object[, sentinel])
# next(iterator[, default])

# 生成迭代器

lst = [1, 2, 3]
iter(lst)
Out[8]: <list_iterator at 0x1a497320b38>
next(lst)
Traceback (most recent call last):
  File "D:\python35\lib\site-packages\IPython\core\interactiveshell.py", line 2910, in run_code
    exec(code_obj, self.user_global_ns, self.user_ns)
  File "<ipython-input-9-825f57446ad8>", line 1, in <module>
    next(lst)
TypeError: 'list' object is not an iterator
b = iter(lst)
next(b)
Out[11]: 1
next(b)
Out[12]: 2
next(b)
Out[13]: 3
next(b)
Traceback (most recent call last):
  File "D:\python35\lib\site-packages\IPython\core\interactiveshell.py", line 2910, in run_code
    exec(code_obj, self.user_global_ns, self.user_ns)
  File "<ipython-input-14-adb3e17b0219>", line 1, in <module>
    next(b)
StopIteration

# oct(x)
# 将一个整数转换成8进制

oct(10)
Out[2]: '0o12'
oct(1)
Out[3]: '0o1'

# open(name[, mode[, buffering]])

f = open('test.txt')
print(f.read())

11111

# ocd(c)
# 接受一个字符装换成ascii码

ord('a')
Out[3]: 97
ord('A')
Out[4]: 65

# range()

range(10)
Out[6]: range(0, 10)
range(1,11)
Out[7]: range(1, 11)

for i in range(1, 11):
    print(i)
    
1
2
3
4
5
6
7
8
9
10

for i in range(len(name)):
    print(name[i])
    
b
u
g
l
a
n

```

### Bulid-in Constants

1. False
2. True
3. None



