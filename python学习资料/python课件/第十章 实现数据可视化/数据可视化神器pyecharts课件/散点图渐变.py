from pyecharts.charts import EffectScatter
from pyecharts import options as opts

cata = ['衬衫','毛衣','裤子','风衣','高登鞋','袜子']
data1 = [114,55,27,101,125,27,105]
data2 = [57,134,137,129,145,60,49]



pie = (
    EffectScatter()
    .add_xaxis(cata)
    .add_yaxis('商店A',data1,symbol_size=20)
    .add_yaxis('商店B',data2,symbol_size=30)
    .set_global_opts(title_opts=opts.TitleOpts(title='EffectScatter-基本示例',subtitle='我是副标题'),
                     toolbox_opts=opts.ToolboxOpts(),
                     visualmap_opts=opts.VisualMapOpts(is_show=True)#设置散点的颜色渐变
                     )
    #.set_series_opts(label_opts=opts.LabelOpts(formatter='{b}:{d}%'))#数据展现的格式
      )


#总渲染
pie.render('散点图渐变.html')