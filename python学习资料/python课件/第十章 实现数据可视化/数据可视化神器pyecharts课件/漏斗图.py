from pyecharts.charts import Funnel
from pyecharts import options as opts

cata = ['访问','收藏','加入购物车','提交单位支付','付款成功']
data1 = [30398,15230,10045,8109,5700]

pie = (
    Funnel()
    .add('用户数',[list(z) for z in zip(cata,data1)],
         sort_='ascending',
         label_opts=opts.LabelOpts(position='inside')
         )
    .set_global_opts(title_opts=opts.TitleOpts(title='Funnel-基本示例',subtitle='我是副标题'))
    #.set_series_opts(label_opts=opts.LabelOpts(formatter='{b}:{d}%'))#数据展现的格式
      )


#总渲染
pie.render('漏斗图.html')