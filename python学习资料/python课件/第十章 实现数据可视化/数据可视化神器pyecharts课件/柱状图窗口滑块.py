from pyecharts.charts import Bar
from pyecharts import options as opts

cata = ['apple','Huawei','xiaomi','oppo','samsung']
data1 = [123,153,89,107,98]
data2 = [56,77,93,68,45]

bar = (
    Bar()
    .add_xaxis(cata)  #设置x宙的数据
    .add_yaxis('线上渠道',data1)  #线上渠道的数据
    .add_yaxis('线下渠道',data2)  #线下渠道的数据
    .set_global_opts(title_opts=opts.TitleOpts(title='Bar-基本示例',subtitle='我是副标题'),
                     toolbox_opts=opts.ToolboxOpts(),#可以理解为工具栏
                     legend_opts=opts.LegendOpts(is_show=True), #图例要不要展示出来
                     datazoom_opts=opts.DataZoomOpts()  #设置窗口滑块
                     )
      )
#总渲染
bar.render('zhu2.html')