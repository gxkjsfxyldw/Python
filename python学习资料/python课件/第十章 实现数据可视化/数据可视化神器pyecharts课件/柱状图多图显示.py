from pyecharts.charts import Bar
from pyecharts import options as opts
from pyecharts.charts import Page, Bar
cata = ['apple','Huawei','xiaomi','oppo','samsung']
data1 = [123,153,89,107,98]
data2 = [56,77,93,68,45]
page = Page()
bar = (
    Bar()
    .add_xaxis(cata)  #设置x宙的数据
    .add_yaxis('线上渠道',data1)  #线上渠道的数据
    .add_yaxis('线下渠道',data2)  #线下渠道的数据
    .set_global_opts(title_opts=opts.TitleOpts(title='Bar-基本示例',subtitle='我是副标题'),
                     toolbox_opts=opts.ToolboxOpts(),#可以理解为工具栏
                     legend_opts=opts.LegendOpts(is_show=True) #图例要不要展示出来
                     )
      )
#再jupyter notebook总渲染
l1=['星期一','星期二','星期三','星期四','星期五','星期七','星期日']
l2=[100,200,300,400,500,400,300]
l3=[300,400,500,400,300,200,100]
bar1 = (
    Bar()
    .add_xaxis(l1)
    .add_yaxis("l2", l2)
    .add_yaxis("l3", l3)
    .set_global_opts(title_opts=opts.TitleOpts(title="Bar-基本示例", subtitle="我是副标题"),
                    toolbox_opts=opts.BrushOpts(),)
)
page.add(bar)
page.add(bar1)
page.render('zhu3.html')














