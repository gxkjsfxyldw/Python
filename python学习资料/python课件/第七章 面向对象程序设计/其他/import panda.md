```Python
import pandas as pd
pf = pd.read_excel('11.xls', sheet_name='Sheet1')
print(pf)
```

我们在这里使用了`pd.read_excel()`函数来读取excel，来看一下`read_excel()`这个方法的API，这里只截选一部分经常使用的参数:

```
pd.read_excel(io, sheet_name=0, header=0, names=None, index_col=None, usecols=None)
io：excel文件
sheet_name：返回指定sheet，默认索引0返回第一个，也可用名称，如果返回多个则可用列表，为None则返回全表
header：指定表头，也可用列表指定多行
names：自定义列名，长度和Excel列长度必须一致
index_col：用作索引的列            0是第一列
usecols：读取指定的列，参数为列表，如[0,1]表示第1和第2列
```

```
import pandas as pd
pf = pd.read_excel('11.xls', sheet_name='Sheet1',index_col=0)
print(len(pf))

print(pf.shape[0]) #行
print(pf.shape[1])
pf.loc['啊32','分数']=98        #先行再列
# pf['分数'][pf['名字'] == '啊32'] =99
print(pf)
pf.to_excel('11.xlsx', sheet_name='Sheet1', index=True, header=True)
```

data['列名称'] = [值1, 值2, ......]

新增行数据，这里行的num为excel中自动给行加的id数值
data.loc[行的num] = [值1， 值2， ...], (注意与`.iloc`的区别)

```
import pandas as pd
pf = pd.read_excel('11.xls', sheet_name='Sheet1',index_col=0)
print(len(pf))

print(pf.shape[0]) #行
print(pf.shape[1])
pf.loc['啊32','分数']=98
# pf['分数'][pf['名字'] == '啊32'] =99
pf.loc['啊321','QQ':'分数']=[1,2,3]
print(pf)
print('爱爱爱' in pf)
pf.to_excel('11.xlsx', sheet_name='Sheet1', index=True, header=True)
```