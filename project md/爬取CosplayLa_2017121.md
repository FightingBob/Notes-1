time : 20171202 24点前完成
url = "http://cosplay.la/photo"
### 环境
```
# windows 10
# vs code
# python3.5
```


### 创建虚拟环境
```
pyvenv -m venv venv
```
### 思路
1. 先分析页面看链接是否动态生成
2. 创建通用的函数DownloadPage和DownloadFile
3. 使用链接测试通用函数
4. 分析页面创建解析函数
5. 工厂模式包装定向爬虫
6. 测试可行性
7. debug

##### 单线程爬虫速度慢 对于错误的url处理经验不够 只是不停的for in soup 完全没有效率对于re模块的使用也不够熟练只会(.*?) 和 .*? 文件的创建也模模糊糊 '\' 和 '/'的使用也分不清

### 创建辅助函数
```python
# Support.py
import requests


def DownloadPage(url, **kwargs):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36"
    }
    num = 5
    while num > 0:
        try:
            r = requests.get(url, headers=headers, timeout=3)
            r.raise_for_status()
        except:
            print("Link Error")
            num = num - 1 
        else:
            r.encoding = r.apparent_encoding
            return r.text
        

def DownloadFile(url, filepath, **kwargs):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36"
    }
    num = 2
    while num > 0:
        try:
            r = requests.get(url,headers=headers, timeout=10)
            r.raise_for_status()
        except:
            print(url + "Download Fail")
            num = num - 1
        else:
            with open(filepath, "wb") as f:
                f.write(r.content)
            return True

```

### main函数
```python
# main.py
from Support import *
from bs4 import BeautifulSoup
import re
import os
import time


def parser(content):
    soup = BeautifulSoup(content, 'html.parser')
    items = soup.find_all('li', attrs={'class': 'font12 fleft'})
    ret = []

    for item in items:
        ret.append("http://cosplay.la/" + item.a.attrs['href'])

    return ret # 图集的地址列表


def parser2(content):
    soup = BeautifulSoup(content, 'html.parser')
    div = soup.find_all('div', attrs={'class': 'talk_pic hauto'})[0]
    ret = []

    for item in div.find_all('p', attrs={'class':'mbottom10'}):
        ret.append(item.a.img.attrs['src'])
    return ret # 图片地址的列表


def getPageList(content):
    soup = BeautifulSoup(content, 'html.parser')
    div = soup.find_all('div', attrs={'class': 'pagen tcenter mbottom20 font16'})[0]
    page = div.find_all('a')[-2].get_text()
    pageList = []

    for i in range(int(page) + 1):
        pageList.append("http://cosplay.la/photo/index/0-0-{}".format(i))

    return pageList # 所有页面的列表


def getName(url):
    name = re.findall(r'http://img.cosplay.la//(.*?)\?imageView.*?', url)[0]
    return name


def main():
    root_url = "http://cosplay.la/photo" 

    html = DownloadPage(root_url)

    pages = getPageList(html)
    for url in pages[:10]: # 前十页
        html = DownloadPage(url)
        page_list = parser(html)

        for page in page_list: #一页20条
            html = DownloadPage(page)

            for img in parser2(html): # 一条多个图片
                try:
                    filepath = os.path.join(os.getcwd(), 'images', getName(img))
                    DownloadFile(img, filepath)
                except OSError as e:
                    print(e)

               
if __name__ == "__main__":
    main()
```
