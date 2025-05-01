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
    .set_series_opts(
                    label_opts=opts.LabelOpts(is_show=False),
                    markpoint_opts=opts.MarkPointOpts(  #图形标记组件，
                        data=[
                            opts.MarkPointItem(type_='max',name='最大值'),
                            opts.MarkPointItem(type_='min',name='最小值'),
                            opts.MarkPointItem(type_='average',name='平均值')
                              ]
                                                     ),
                    markline_opts=opts.MarkLineOpts(
                        data=[
                            opts.MarkLineItem(type_='min',name='最小值'),#标记线与标记点最大最小值，以及平均值
                            opts.MarkLineItem(type_='max',name='最大值')
                        ]
                    )
                    )
    .set_global_opts(
                     title_opts=opts.TitleOpts(title='最大最小值的展现',subtitle='我是副标题'),
                     toolbox_opts=opts.ToolboxOpts() #可以理解为工具栏
                     )
      )

#渲染,可视化
bar.render()

















