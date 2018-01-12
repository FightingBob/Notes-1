### 安装

```bash
pip install BeautifulSoup4
```


### 解析器

Python标准库

使用方法:
BeautifulSoup(markup, "html.parser")

优势:
- Python的内置标准库
- 执行速度适中
- 文档容错能力强

劣势:
- Python 2.7.3 or 3.2.2)前 的版本中文档容错能力差

lxml HTML 解析器

使用方法:
BeautifulSoup(markup, "lxml")

优势:
- 速度快
- 文档容错能力强

劣势:
- 需要安装C语言库

lxml XML 解析器

使用方法:

- BeautifulSoup(markup, ["lxml", "xml"])
- BeautifulSoup(markup, "xml")

优势:
- 速度快
- 唯一支持XML的解析器

劣势:
- 需要安装C语言库

html5lib

使用方法:
BeautifulSoup(markup, "html5lib")

优势:
- 最好的容错性
- 以浏览器的方式解析文档
- 生成HTML5格式的文档

劣势:
- 速度慢
- 不依赖外部扩展

### 第一次使用

```python
from bs4 import BeautifulSoup

# s = html
soup = BeautifulSoup(html, 'html.parser')

```

### BeautifluSoup 对象

- Tag
- NavigableString
- BeautifulSoup
- Comment

### Tag

```python
"""
不使用解析器会出现waring

"""
>>> from bs4 import BeautifulSoup
>>> soup = BeautifulSoup('<b class="boldest">Extremely bold</b>')

Warning (from warnings module):
  File "D:\python35\lib\site-packages\bs4\__init__.py", line 181
    markup_type=markup_type))
UserWarning: No parser was explicitly specified, so I'm using the best available HTML parser for this system ("lxml"). This usually isn't a problem, but if you run this code on another system, or in a different virtual environment, it may use a different parser and behave differently.

The code that caused this warning is on line 1 of the file <string>. To get rid of this warning, change code that looks like this:

 BeautifulSoup(YOUR_MARKUP})

to this:

 BeautifulSoup(YOUR_MARKUP, "lxml")

>>> soup
<html><body><b class="boldest">Extremely bold</b></body></html>
>>> type(soup)
<class 'bs4.BeautifulSoup'>
>>> tag = soup.b
>>> tag
<b class="boldest">Extremely bold</b>
>>> type(tag)            
<class 'bs4.element.Tag'>
```

### 节点

#### 子节点





