import pandas as pd
from snownlp import SnowNLP
from snownlp import sentiment
import matplotlib.pyplot as plt
#读取抓取的csv文件，标题在第3列，序号为2
df = pd.read_csv('douban_movie1.csv',header=None,usecols=[2])

#将dataframe转换为list

contents = df.values.tolist()
#数据长度
print(len(contents))
#定义空列表存储情感分值
score=[]
for content in contents:
    try:
        s = SnowNLP(content[0])
        score.append(s.sentiments)
    except:
        print('something is wrong')
        score.append(0.5)
#显示情感得分长度，与数据长度比较
print(len(score))
#存储
data2 = pd.DataFrame(score)
data2.to_csv('sentiment.csv',header=False,index=(False),mode='a+')






















