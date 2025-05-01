# 1 Tkinter概述

## 1.1 Tkinter 模块元素简要说明

| 组件类       | 元素       | 说明描述                                                   |
| ------------ | ---------- | ---------------------------------------------------------- |
| Label        | 标签       | 用于显示不可编辑的文本或图标                               |
| Button       | 按钮       | 点击时执行一个动作                                         |
| Canvas       | 画布       | 提供绘图功能(直线、椭圆、多边形、矩形) 可以包含图形或位图  |
| Entry        | 单行文本框 | 显示一行文本                                               |
| Frame        | 框架       | 用来承载放置其他GUI元素，就是一个容器                      |
| Listbox      | 列表框     | 一个选项列表,用户可以从中选择                              |
| Menu         | 菜单       | 点下菜单按钮后弹出的一个选项列表,用户可以从中选择          |
| Message      | 消息框     | 类似于标签,但可以显示多行文本                              |
| Radiobuttion | 单选框     | 允许用户从多个选项中选取一个                               |
| Scale        | 进度条     | 线性“滑块”组件,可设定起始值和结束值,会显示当前位置的精确值 |
| Scrollbar    | 滚动条     | 对其支持的组件(文本域、画布、列表框、文本框)提供滚动功能   |
| Text         | 多行文本框 | 显示多行文本                                               |
| Toplevel     | 顶层       | 类似框架,为其他的控件提供单独的容器                        |

上述大部分组件共有的属性如下表所示

| 属性名(别名)        | 说明描述                                                     |
| ------------------- | ------------------------------------------------------------ |
| background(**bg**)  | 设定组件的背景景色                                           |
| borderwidth(**bd**) | 设置边框宽度                                                 |
| Font                | 设定组件内部文字的字体                                       |
| foreground(**fg**)  | 设定组件的前景色                                             |
| relief              | 设定组件3D效果                                               |
| width               | 设定组件宽度，如果≤0，则组件会选择一个能够容纳目前字符的宽度 |

## 1.2  用户界面的构成

下面创建了第一个GUI程序，运行代码可以感受一下

```python
from tkinter import *
# 创建根窗口
root = Tk()
#设置窗口标题
root.title("Hello")
#设置窗口大小
root.geometry("300x200")
#在窗体中创建一个框架，用它来	承载其他小部件
app = Frame(root)
#设置布局管理器
app.grid()

label = Label(app, text="hello word!")
label.grid()

btn = Button(app)
btn.grid()

#小部件的任何选项都可以通过configure()方法操作
btn.configure(text="click")

root.mainloop() #循环窗口
```



上面的代码中，首先获得了我们的画板，也就是根窗体root，然后又创建了一个容器Frame，也就是我们的画布，在创建Frame时，我们很清楚画布必须放在画板上面，所以传入了一个参数root，通常所有的tkinter组件实例化时，第一个参数都是指定父控件，就是表示自己放哪里。如Label和Button，指定放在Frame上面。


## 1.3 GUI之tkinter布局管理

所谓布局，就是指控制窗体容器中各个控件（组件）的位置关系。tkinter 共有三种几何布局管理器，分别是：pack布局，grid布局，place布局。

### 1.3.1 pack布局

使用 pack布局，将向容器中添加组件，第一个添加的组件在最上方，然后是依次向下添加

```python
from tkinter import *
root = Tk()
#创建三个 Label 分别添加到root窗体中 
#Label是一种用来显示文字或者图片的组件
Label(root,text = 'pack1',bg = 'red').pack() 
Label(root, text = 'pack2', bg = 'blue').pack() 
Label(root, text = 'pack3', bg = 'green').pack()
root.mainloop()
```

![pack1](图\pack1.png)

**pack常用属性**

![pack属性](pack属性.png)

north北方 （N）			west西方 （W）				east东方 （E）					south南方（S）
southeast东南（SE） 	southwest西南 （SW）	northwest西北 （NW）	northeast东北 （NE）

```python
from tkinter import *  # 注意模块导入方式，否则代码会有差别
class App:
    def __init__(self, master):
        # 使用Frame增加一层容器
        fm1 = Frame(master)
        # Button是一种按钮组件，与Label类似，只是多出了响应点击的功能
        Button(fm1, text='Top').pack(side=TOP, anchor=W, fill=X, expand=YES)
        Button(fm1, text='Center').pack(side=TOP, anchor=W, fill=X, expand=YES)
        Button(fm1, text='Bottom').pack(side=TOP, anchor=W, fill=X, expand=YES)
        fm1.pack(side=LEFT, fill=BOTH, expand=YES)

        fm2 = Frame(master)
        Button(fm2, text='Left').pack(side=LEFT)
        Button(fm2, text='This is the Center button').pack(side=LEFT)
        Button(fm2, text='Right').pack(side=LEFT)
        fm2.pack(side=LEFT, padx=10)


root = Tk()
root.title("Pa  ck - Example")
display = App(root)
root.mainloop()

```

![1](图\1.png)

如上，创建一个Frame容器fm1，将三个垂直排列的Button组件使用pack布局放入fm1容器中，然后创建fm2容器，同样将三个水平排列的Button组件放入，最后将两个Frame容器当做组件，使用pack布局放入根窗体容器中。如此分层布局，实现了相对复杂一些的界面需求。

### 1.3.2 grid布局

grid布局又被称作网格布局，是最被推荐使用的布局。程序大多数都是矩形的界面，我们可以很容易把它划分为一个几行几列的网格，然后根据行号和列号，将组件放置于网格之中。使用grid 布局时，需要在里面指定两个参数，分别用row 表示行，column 表示列。需要注意的是 row 和 column 的序号都从0 开始。

grid属性设置

![grid属性设置](grid属性设置.png)

```python
import tkinter as tk

window = tk.Tk()
window.title('my window')
window.geometry('500x600')

for i in range(4):
    for j in range(3):
        tk.Label(window, text='放置', bg='green').grid(row=i, column=j, ipadx=10, ipady=10, padx=10, pady=10)
        # 摆放的位置坐标    内部位置大小      外部位置大小

window.mainloop()
```

<img src="图\grid演示.png" alt="grid演示" style="zoom:50%;" />

### 1.3.3 place方式

最简单最灵活的一种布局，使用组件坐标来放置组件的位置。但是不太推荐使用，在不同分辨率下，界面往往有较大差异。

place() 主要采用的是绝对的摆放方式，主要是方式由两种 第一种x， y, width, height 和 relx, rely, relwidth, relheight 按照比例进行摆放 

```python
import tkinter
# 创建主窗口对象
root = tkinter.Tk()

root.minsize(500, 500)
# root.geometry('500x300+500+200') # 设置固定窗口的大小

btn1 = tkinter.Button(root, text='按钮1')
btn1.place(relx=100 / 500, rely = 50 / 500, )

btn2 = tkinter.Button(root, text='按钮2')
btn2.place(relx=200/500, rely=50/500, relwidth=0.1, relheight=0.3)

root.mainloop()
```



<img src="图\place.png" alt="place" style="zoom:50%;" />

anchor属性的值和意义

<img src="图\anchor.png" alt="anchor" style="zoom:67%;" />

