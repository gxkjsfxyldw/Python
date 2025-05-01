# XPath的使用方法： 

首先讲一下XPath的基本语法知识： 

``` 
1)  //  双斜杠 定位根节点，会对全文进行扫描，在文档中选取所有符合条件的内容，以列表的形式返回。 
2) / 单斜杠 寻找当前标签路径的下一层路径标签或者对当前路标签内容进行操作 
3) /text() 获取当前路径下的文本内容 
4) /@xxxx 提取当前路径下标签的属性值 
5) | 可选符 使用|可选取若干个路径 如//p | //div 即在当前路径下选取所有符合条件的p标签和div标签。 
6) . 点 用来选取当前节点 
7) .. 双点 选取当前节点的父节点 

```



![20180812122241534](图\20180812122241534.png)





![2](图\2.png)



![3](图\3.png)



我们发现，网页里面有很多`<li>...</li>`标签,而且每一个标签里面都有一个电影的信息。我们想要的就是标签里面的文字信息。

![4](图\4.png)



![5](图\5.png)



`所有的信息都在class属性为info的div标签里，可以先把这个节点取出来 //*[@id=“content”]/div/div[1]/ol`



![6](图\6.png)



````
知道xpath的用法后，我们就可以轻松的拿到我们想要的信息了！！！
影片名称 ：title = i.xpath('div[@class="hd"]/a/span[@class="title"]/text()')[0]
导演演员信息：info = i.xpath('div[@class="bd"]/p[1]/text()')
评分：rate = i.xpath('//span[@class="rating_num"]/text()')[0]
评论人数：comCount = i.xpath('//div[@class="star"]/span[4]/text()')[0]

````

已经知道如何获取电影信息了，现在的任务是找到请求网址，我们可以翻页寻找网址的规律，看看第二页，第三页……网址是什么样的。

![7](图\7.png)

![8](图\8.png)

![9](图\9.png)

不难发现规律，只是每页网址的start=发生变化。我们可以使用for循环来请求每页网址，

```python
for i in range(10): 
    url = f'https://movie.douban.com/top250?start={i*25}&filter='
```

### 完整代码

```python
import requests
#import xpath
#import pymysql
from lxml import html
k = 1
headers={
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
}
for i in range(10): 
    print(f'第{i}页开始爬')
    info = []
    #url = 'https://movie.douban.com/top250?start={}&filter='.format(i*25) 
    url = f'https://movie.douban.com/top250?start={i*25}&filter='
    con = requests.get(url,headers=headers).content #也可以.text
    sel = html.fromstring(con)
    # 所有的信息都在class属性为info的div标签里，可以先把这个节点取出来 //*[@id="content"]/div/div[1]/ol
    for i in sel.xpath('//div[@class="info"]'):
		m = []
        # 影片名称
        title = i.xpath('div[@class="hd"]/a/span[@class="title"]/text()')[0] #text()返回文本的形式 [0]网页里面的第一个span的内容
        #print(title)
        info = i.xpath('div[@class="bd"]/p[1]/text()')#*****************  p[0]保存第一页？ 第一个电影的内容返回文本形式再提取内容
        # 导演演员信息
        info_1 = info[0].replace(" ", "").replace("\n", "")#class=“bd” [0] 里面的第一个p的内容分割空格 提取文本文字
        # 上映日期
        date = info[1].replace(" ", "").replace("\n", "").split("/")[0] #1994
        # 制片国家
        country = info[1].replace(" ", "").replace("\n", "").split("/")[1]#美国
        # 影片类型
        geners = info[1].replace(" ", "").replace("\n", "").split("/")[2]#犯罪 剧情
        # 评分
        rate = i.xpath('//span[@class="rating_num"]/text()')[0]#几个星星
        # 评论人数
        comCount = i.xpath('//div[@class="star"]/span[4]/text()')[0]#？
        
		m.extend([title, info_1, rate, date, country, geners, comCount ]) #将一个列表中每个元素分别添加到另一个列表中,只接受一个参数, 且该参数只能为列表list形式。
        info.append(m)#出错
        
     
    try:
        # 获取一个有效的数据库连接对象，此处填写你的数据库信息，特别注意charset一定要写成'utf8'，不能写成'utf-8'。
        filename = '豆瓣top 200(1).csv'

        dataframe = pd.DataFrame(info)
        dataframe.to_csv(filename, mode='a', index=False, sep=',', header=False)
		print(f'第{i}页爬完')
	except:

			print('事务回滚')


```

