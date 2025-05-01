import pandas as pd
from collections import  Counter
'''
from collections import Counter 导入计数包
先读取文件，再统计每个评分的打分数量并显示。
按每个评分得出情感平均值。
'''

#读取csv文件
df = pd.read_csv('douban_movie1.csv')

#统计打分数量
recommend_list = df['recommend'].values.tolist()
num_count = Counter(recommend_list)           #统计出现次数
print(num_count)

#分组求平均值
grouped = df.groupby('recommend').describe().reset_index()  #分类聚合
print(grouped)
recommend = grouped['recommend'].values.tolist()
print(recommend)

#根据用户打分的分组，对每组的情感值求平均
sentiment_average = df.groupby('recommend')['score'].mean()
sentiment_scores = sentiment_average.values
print(sentiment_scores)