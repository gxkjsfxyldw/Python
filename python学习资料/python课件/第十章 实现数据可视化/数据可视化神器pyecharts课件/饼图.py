from pyecharts.charts import Pie
from pyecharts import options as opts

cata = ['apple','Huawei','xiaomi','oppo','samsung']
data1 = [123,153,89,107,98]
# a=[['apple',123],['hu',153]]
pie = (
    Pie()
    .add('lll',[list(z) for z in zip(cata,data1)],radius='100%') #radius表示圆的半径
    .set_global_opts(title_opts=opts.TitleOpts(title='Pie-基本示例',subtitle='我是副标题'))
    .set_series_opts(label_opts=opts.LabelOpts(formatter='{b}:{d}%'))#数据展现的格式
      )


#总渲染
pie.render('b.html')
