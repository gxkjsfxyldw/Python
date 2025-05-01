# Matplotlib数据可视化

## 1、Matplotlib简介

Matplotlib是非常强大的python画图工具

Matplotlib可以画图线图、散点图、等高线图、条形图、柱形图、3D图形、图形动画等。

## 2、Matplotlib安装

```
pip3 install matplotlib   #python3
```

## 2.1 numpy一些常用函数

```python
numpy.linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None, axis=0)

#(在start和stop之间返回均匀间隔的数据)

#(返回的是 [start, stop]之间的均匀分布)

```

```python
start:返回样本数据开始点
stop:返回样本数据结束点
num:生成的样本数据量，默认为50
endpoint：True则包含stop；False则不包含stop
retstep：If True, return (samples, step), where step is the spacing between samples.(即如果为True则结果会给出数据间隔)
dtype：输出数组类型
axis：0(默认)或-1
```

```python
>>> np.linspace(2.0, 3.0, num=5)
array([ 2.  ,  2.25,  2.5 ,  2.75,  3.  ])
>>> np.linspace(2.0, 3.0, num=5, endpoint=False)
array([ 2. ,  2.2,  2.4,  2.6,  2.8])
>>> np.linspace(2.0, 3.0, num=5, retstep=True)
(array([ 2.  ,  2.25,  2.5 ,  2.75,  3.  ]), 0.25)

```



## 3、 窗口实现

### 3.1 figure语法及操作

* figure语法说明

```python
figure(num=None, figsize=None, dpi=None, facecolor=None, edgecolor=None, frameon=True)
```

```
num:图像编号或名称，数字为编号 ，字符串为名称
figsize:指定figure的宽和高，单位为英寸；
dpi参数指定绘图对象的分辨率，即每英寸多少个像素，缺省值为80      1英寸等于2.5cm,A4纸是 21*30cm的纸张 
facecolor:背景颜色
edgecolor:边框颜色
frameon:是否显示边框
```

* demo 1

```python
import matplotlib.pyplot as plt
#创建自定义图像
fig=plt.figure(figsize=(4,3)) #创建指定大小的窗口
plt.show() #打开matplotlib查看器，并显示绘制图形
```

### 3.2 subplot()

在matplotlib中，一个Figure对象可以包含多个子图，可以使用subplot()来创建子图，subplot的语法格式如下。

```python
subplot(numRows, numCols, plotNum)
```

- 图表的整个绘图区域被分成 `numRows` 行和 `numCols` 列
- 然后按照从左到右，从上到下的顺序对每个子区域进行编号，左上的子区域的编号为1
- `plotNum` 参数指定创建的 `Axes` 对象所在的区域

如果 `numRows ＝ 2, numCols ＝ 3`, 那整个绘制图表样式为 `2X3` 的图片区域, 用坐标表示为

```
(1, 1), (1, 2), (1, 3)
(2, 1), (2, 2), (2, 3)
```

这时, 当 `plotNum ＝ 3` 时, 表示的坐标为(1, 3), 即第一行第三列的子图

* demo 1

```python
import matplotlib.pyplot as plt
'''使用figure创建一块自定义大小的画布(窗口)，使得后面的图形输出在这块规定了大小的画布上，其中参数figsize设置画布大小'''
plt.figure(figsize=(8,8)) 
'''将figure设置的画布分成多个部分，参数'221'表示将画布分成两行两列的4块区域，1表示选择4块区域中的第一块作为输出区域，如果参数设置为subplot(111)，则表示图形直接输出在整块画布上，画布不分割成小块区域'''
plt.subplot(221) 
plt.subplot(222) 
plt.subplot(223) 
plt.subplot(224) 
plt.show()
```

![1](图\1.png)

* demo 2

```python
import matplotlib.pyplot as plt
#先创建窗口，再创建子图
fig = plt.figure(num=1, figsize=(15, 8),dpi=80)  #创建窗口并设置大小、分辨率
ax1 = fig.add_subplot(211)   #通过fig添加子图，参数：行数，列数，第几个
ax2 = fig.add_subplot(2,1,2)   #通过fig添加子图，参数：行数，列数，第几个
#设置子图的基本元素
ax1.set_title('Python-drawing',fontsize=14)   #设置图标题，并设置标题字体大小
ax1.set_xlabel('x-name',fontsize=14)        #设置x轴标签,并设置标签字体大小
ax1.set_ylabel('y-name',fontsize=14)        #设置y轴标签,并设置标签字体大小
plt.axis([-6,6,-10,10])   #设置横、纵坐标轴范围，可分解为下面两个函数
ax1.set_xlim(-5,5)     #设置横轴范围，会覆盖上面的横坐标轴范围
ax1.set_ylim(-10,10)   #设置纵轴范围，会覆盖上面的纵坐标轴范围
plt.savefig(r'E:\科师\2021春资料\课程\python\课件\第十章 实现数据可视化\图\3.png', dpi=400) #保存绘制的图像并设置分辨率
plt.show()            #打开matplotlib查看器，并显示绘制的图形


```

![3](图\3.png)

### 3.3 plot()

参数说明

```python
#单条线：
plot([x], y, [fmt], data=None, **kwargs)
#多条线一起画
plot([x], y, [fmt], [x2], y2, [fmt2], ..., **kwargs)
```

可选参数[fmt] 是一个字符串来定义图的基本属性如：颜色（color），点型（marker），线型（linestyle），

具体形式  `fmt = [color][marker][line]`

fmt接收的是每个属性的单个字母缩写，例如：

```python
plot(x, y, 'bo-')  # 蓝色圆点实线
```

也可以对关键字参数color赋十六进制的RGB字符串如 color='#900302'

```python
    'b'         blue 蓝
    'g'         green 绿
    'r'         red 红
    'c'         cyan 蓝绿
    'm'         magenta 洋红
    'y'         yellow 黄
    'k'         black 黑
    'w'         white 白
```

如：marker='+' 这个只有简写，英文描述不被识别

```python
 '.'          point marker
 ','          pixel marker
 'o'          circle marker
 'v'          triangle_down marker
 '^'          triangle_up marker
 '<'          triangle_left marker
 '>'          triangle_right marker
 '1'          tri_down marker
 '2'          tri_up marker
 '3'          tri_left marker
 '4'          tri_right marker
 's'          square marker
 'p'          pentagon marker
 '*'          star marker
 'h'          hexagon1 marker
 'H'          hexagon2 marker
 '+'          plus marker
 'x'          x marker
 'D'          diamond marker
 'd'          thin_diamond marker
 '|'          vline marker
 '_'          hline marker
```

线型参数，linestyle='-'

```python
'-'         solid line style 实线
'--'        dashed line style 虚线
'-.'        dash-dot line style 点画线
':'         dotted line style 点线
""			无线条

```

设置坐标范围：

```python
plt.axis([xmin,xmax,ymin,ymax]) #设定x轴y轴的取值范围
xlim(xmin,xmax)和ylim(ymin,ymax) #调整x轴y轴的取值范围
```



* demo 3

```python
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 100)

plt.subplot(221)
plt.plot(x, x)

plt.subplot(222)
plt.plot(x, -x)

plt.subplot(223)
plt.plot(x, x ** 2)

plt.subplot(224)
plt.plot(x, np.log(x))

plt.show()
```

![2](图\2.png)

* demo 4

```python
import matplotlib.pyplot as plt
plt.plot([1,2,3,4],'ko--')
plt.title('$hello')
plt.xlabel('xx')
plt.ylabel('yy')
plt.show()
```

![4](图\4.png)



# 作业

## 1、画一个原点为圆心的单位圆

ps:  (x-a)²+(y-b)²=r²

## 2、试画出下面函数的图像

$$
x=16sin^3t
$$

$$
y=13cost-5cos(2t)-2cos(3t)-cos(4t)
$$

