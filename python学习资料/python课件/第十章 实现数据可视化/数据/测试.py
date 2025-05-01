from pyecharts.charts import Bar
from pyecharts import options as opts
import pandas as pd
from collections import Counter

df = pd.read_csv(r'C:\Users\Administrator\Desktop\che\python\课件\爬虫基础\爬虫11\豆瓣评论抓取+情感分析+云词\douban_movie2.csv')
#统计打分数量
recommend_list = df['recommend'].values.tolist()
a = Counter(recommend_list)
print(a)
a1=[]
a2=[]
print(a.most_common())
for i,j in a.most_common():
    a1.append(str(i)+'星')
    a2.append(j)
print(a1)
print(a2)
bar = (
    Bar()
    .add_xaxis(a1)  #设置x宙的数据
    .add_yaxis('星级数',a2)  #线上渠道的数据
    #.add_yaxis('线下渠道',data2)  #线下渠道的数据
    .set_global_opts(title_opts=opts.TitleOpts(title='Bar-基本示例',subtitle='我是副标题'),
                     toolbox_opts=opts.ToolboxOpts(),#可以理解为工具栏
                     legend_opts=opts.LegendOpts(is_show=True) #图例要不要展示出来
                     )
      )
#再jupyter notebook总渲染
bar.render('1.html')
