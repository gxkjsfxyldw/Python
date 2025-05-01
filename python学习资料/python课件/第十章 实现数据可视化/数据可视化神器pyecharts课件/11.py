cata = ['访问','收藏','加入购物车','提交单位支付','付款成功']
data1 = [30398,15230,10045,8109,5700]
b =zip(cata,data1)
for i in b:
    print(list(i))
# [list(z) for z in zip(cata,data1)]


# a=[i*2   for i in [1,2,3]]
# print(a)
