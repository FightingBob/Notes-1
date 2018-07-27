# python data sructure cn 读后总结


1. 编写易于阅读和理解的程序
2. 使用常见的数学公式


### 简单求和
```python
def sum_of_n(n):
    sum = 0
    for i in range(1, n+1):
        sum += 1
    return sum
```

```python
def sum_of_n(n):
    retun (n * n(n + 1)) / 2
```


因为存在这样的数学公式: ![](https://facert.gitbooks.io/python-data-structure-cn/2.%E7%AE%97%E6%B3%95%E5%88%86%E6%9E%90/2.2.%E4%BB%80%E4%B9%88%E6%98%AF%E7%AE%97%E6%B3%95%E5%88%86%E6%9E%90/assets/%E6%B1%82%E5%92%8C.png)

### 大O表示法: 算法表示法

```
n+1 -> O(n)
n^2+n+1 -> O(n^2)
log2n -> O(log)
nlog2n -> O(nlog)
n^n -> O(n^n)
```
