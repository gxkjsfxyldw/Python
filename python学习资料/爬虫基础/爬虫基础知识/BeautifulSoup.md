# BeautifulSoup

BeautifulSoup是一个模块，该模块用于接收一个HTML或XML字符串，然后将其进行格式化，之后遍可以使用他提供的方法进行快速查找指定元素，从而使得在HTML或XML中查找指定元素变得简单。

```python
from bs4 import BeautifulSoup
 
html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
asdf
    <div class="title">
        <b>The Dormouse's story总共</b>
        <h1>f</h1>
    </div>
<div class="story">Once upon a time there were three little sisters; and their names were
    <a  class="sister0" id="link1">Els<span>f</span>ie</a>,
    <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
    <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</div>
ad<br/>sf
<p class="story">...</p>
</body>
</html>
"""
 
soup = BeautifulSoup(html_doc, features="lxml")
# 找到第一个a标签
tag1 = soup.find(name='a')  #find,获取匹配的第一个标签
# 找到所有的a标签
tag2 = soup.find_all(name='a')#find_all,获取匹配的所有标签
# 找到id＝link2的标签
tag3 = soup.select('#link2')
```

