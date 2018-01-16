# vim设置tab为4个空格

1. vim /etc/vimrc

| num | operation |
| --- | --------- |
| 1   | set ts=4  |
| 2   | set sw=4  |

2. vim /etc/vimrc

| num | operation      |
| --- | -------------- |
| 1   | set ts=4       |
| 2   | set expandtab  |
| 3   | set autoindent |

Note:
```
推荐使用第二种，按tab键时产生的是4个空格，这种方式具有最好的兼容性。
```

