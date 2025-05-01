# 常用Tkinter组件的使用

# 1 标签组件

Label（标签）组件用于在屏幕上显示文本或图像。Label 组件仅能显示单一字体的文本，但文本可以跨越多行。另外，还可以为其中的个别字符加上下划线。

## 1.1 参数

`Label(master=None, options)`

* master -- 父组件

* options -- 组件选项，下方表格详细列举了各个选项的具体含义和用法：

|       选项       |                             说明                             |
| :--------------: | :----------------------------------------------------------: |
| background又称bg |             1. 设置背景颜色 2. 默认值由系统指定              |
| foreground又称fg |     1. 设置 Label 的文本和位图的颜色 2. 默认值由系统指定     |
|      bitmap      | 1. 指定显示到 Label 上的位图 2. 如果指定了 image 选项，则该选项被忽略 |
|      image       | 1. 指定 Label 显示的图片 2. 该值应该是 PhotoImage，BitmapImage，或者能兼容的对象 3. 该选项优先于 text 和 bitmap 选项 |
|       text       | 1. 指定 Label 显示的文本 2. 文本可以包含换行符 3. 如果设置了 bitmap 或 image 选项，该选项则被忽略 |
|       font       | 1. 指定 Label 中文本的字体(注：如果同时设置字体和大小，应该用元组包起来，如（"楷体", 20） 2. 一个 Label 只能设置一种字体 3. 默认值由系统指定 |
|     justify      | 1. 定义如何对齐多行文本 2. 使用 "left"，"right" 或 "center" 3. 注意，文本的位置取决于 anchor 选项 4. 默认值是 "center" |
|      anchor      | 1. 控制文本（或图像）在 Label 中显示的位置 2. "n", "ne", "e", "se", "s", "sw", "w", "nw", 或者 "center" 来定位（ewsn 代表东西南北，上北下南左西右东） 3. 默认值是 "center" |
|    wraplength    | 1. 决定 Label 的文本应该被分成多少行 2. 该选项指定每行的长度，单位是屏幕单元 3. 默认值是 0 |
|     compound     | 1. 控制 Label 中文本和图像的混合模式<br/> 2. 默认情况下，如果有指定位图或图片，则不显示文本<br/>3. 如果该选项设置为 "center"，文本显示在图像上（文本重叠图像）<br/>4. 如果该选项设置为 "bottom"，"left"，"right" 或 "top"，那么图像显示在文本的旁边（如 "bottom"，则图像在文本的下方）<br/>5. 默认值是 NONE |
|      width       | 1. 设置 Label 的宽度 2. 如果 Label 显示的是文本，那么单位是文本单元 <br/>3. 如果 Label 显示的是图像，那么单位是像素（或屏幕单元） <br/>4. 如果设置为 0 或者干脆不设置，那么会自动根据 Label 的内容计算出宽度 |
|      height      | 1. 设置 Label 的高度 2. 如果 Label 显示的是文本，那么单位是文本单元  <br/>3. 如果 Label 显示的是图像，那么单位是像素（或屏幕单元） 4. 如果设置为 0 或者干脆不设置，那么会自动根据 Label 的内容计算出高度 |
|   textvariable   | 1. Label 显示 Tkinter 变量（通常是一个 StringVar 变量）的内容 2. 如果变量被修改，Label 的文本会自动更新 |

```python
from tkinter import *
root = Tk() 
root.title('NoteBook')
 #用PhotoImage()实例化一个图像对象，参数是文件地址，可惜这能用gif图片
photo = PhotoImage(file = r'图片路径\猫.gif')
the_Label = Label(root,text = '这是一只睡觉的小猫，\n王晓明看傻了！',
                  justify = LEFT, #左对齐，我的理解是如果出现两行以上，可以都让他们左对齐
                  image = photo,
                  compound = CENTER, #设置文本和图像的混合模式
                  font = ('黑体',10), #注意字体和字号用元组的形式
                  fg = 'black') #前景颜色
the_Label.pack(side = LEFT)
root.mainloop()

'''
                  compound:同时使用图像与文本, 指定文本(text)与图像
                  (bitmap/image)是如何在Label上显示，缺省为None， 
                  当指定image/bitmap时，文本(text)将被覆盖，只显示图像了。可以使用的值： 
                  left：    图像居左 
                  right:    图像居右 
                  top：     图像居上 
                  bottom：  图像居下 
                  center：文字覆盖在图像上
'''

```

![label运行图](图\label运行图.png)

书上159页例子：

`9-1.py`

```python
from tkinter import *
window=Tk()            #创建一个窗口，默认的窗口名为“tk”
#创建以window为父容器的标签
label1 = Label(window,fg = 'white',bg = 'grey',text="Hello Label1",width = 10,height = 2)  
label1.pack()             #将标签label1放进window窗口中
#compound = 'bottom'，指定图像位居文本下方
label2=Label(window,text = 'botton',compound = 'bottom',bitmap = 'error').pack()
#compound = 'left'，指定图像位居文本左方
label3=Label(window,text = 'left',compound = 'left',bitmap = 'error').pack()
#justify = 'left'指定标签中文本多行的对齐方式为左对齐
label4=Label(window,text = '对明天最好的准备就是把今天做到最好',fg='white',font=('楷体',13),bg = 'grey',width = 50,height = 3,wraplength = 130,justify = 'left').pack()
'''justify = 'center'指定标签中文本多行的对齐方式为居中对齐, anchor='sw'指定文本(text)在Label中的显示位置是西南'''
label5=Label(window, text = '对明天最好的准备就是把今天做到最好', fg='white', font=('隶书',13),bg = 'black', width = 50, height = 3, wraplength = 130, justify='center', anchor='sw').pack()
window.mainloop()        #创建事件循环
```

![9-1](图\9-1.png)



# 2 Button 按钮组件

## 2.1 简介
Button（按钮）组件用于实现各种各样的按钮。Button 组件可以包含文本或图像，你可以将一个 Python 的函数或方法与之相关联，当按钮被按下时，对应的函数或方法将被自动执行。

Button 组件仅能显示单一字体的文本，但文本可以跨越多行。另外，还可以为其中的个别字符加上下划线。默认情况下，tab 按键被用于在按钮间切换。

## 2.2 用法

普通的按钮是非常简单易用的。你所需要做的就是指定 Button 的内容（文本、位图或者图片），并且关联当按钮被按下时应该调用的函数或方法：

```Python
import tkinter as tk

master = tk.Tk()
def callback():
    print("我被调用了！")
b = tk.Button(master, text="执行", command=callback)
b.pack()
master.mainloop()
```

![执行](图\执行.png)



## 2.3 参数

`Button(master=None, options)`

* master -- 父组件

* options -- 组件选项，下方表格详细列举了各个选项的具体含义和用法：

| 选项         | 描述                                                         |
| ------------ | ------------------------------------------------------------ |
| compound     | 1. 控制 Button 中文本和图像的混合模式<br/>2. 默认情况下，如果有指定位图或图片，则不显示文本<br/>3. 如果该选项设置为 "center"，文本显示在图像上（文本重叠图像）<br/>4. 如果该选项设置为 "bottom"，"left"，"right" 或 "top"，那么图像显示在文本的旁边（如 "bottom"，则图像在文本的下方）<br/>5. 默认值是 NONE |
| relief       | 1. 指定边框样式 <br/>2. 通常当按钮被按下时是 "sunken"，其他时候是 "raised" <br/>3. 另外你还可以设置 "groove"、"ridge" 或 "flat" <br/>4. 默认值是 "raised" |
| state        | 1. 指定 Button 的状态  <br/>2. 默认值是 "normal"  <br/>3. 另外你还可以设置 "active" 或 "disabled" |
| borderwidth  | 1. 指定 Button 的边框宽度  <br/>2. 默认值由系统指定，通常是 1 或 2 像素 |
| textvariable | 1. Button 显示 Tkinter 变量（通常是一个 StringVar 变量）的内容 <br/>2. 如果变量被修改，Button 的文本会自动更新 |

书上161页例子

`9-2.py`

```python
from tkinter import *
def gs():
    global window
    s=Label(window,text='曾伴浮云归晚翠，犹陪落日泛秋声。世间无限丹青手，一片伤心画不成。', font='楷体', fg='white', bg='grey')
    s.pack()
def sc():
    global window
    s=Label(window,text='怒发冲冠，凭栏处、潇潇雨歇。抬望眼，仰天长啸，壮怀激烈。', fg='yellow', bg = 'red')
    s.pack()

def changeText():
   if button['text'] == 'text':
      v.set('change')
   else:
      v.set('text')
   print(v.get())

def statePrint():
   print('state')

window=Tk()#定义父窗口
v = StringVar()    #创建tkinter 的StringVar型数据对象
v.set('change')
'''command参数指定Button的事件处理函数,通过textvariable属性将Button与某个变量绑定，当该变量的值发生变化时，Button 显示的文本也随之变化'''
button = Button(window,textvariable = v,command = changeText)  #创建按钮
#relief参数指定外观效果
button1=Button(window,command=gs,text='古诗阅读',width=40,height=2,relief=RAISED)      
button2=Button(window,command=sc,text='宋词阅读',width=40,height=2,fg='yellow',bg = 'red',relief=SUNKEN)
button.pack()
button1.pack()
button2.pack()
#state参数用来指定按钮的状态,有normal、active、disabled三种状态
for r in ['normal','active','disabled']:
   Button(window,text = r,state = r, width = 20,command = statePrint).pack()
window.mainloop()
```

![9-2](图\9-2.png)

# 3 Radiobutton（单选按钮）组件

## 3.1 简介

Radiobutton（单选按钮）组件用于实现多选一的问题。Radiobutton 组件可以包含文本或图像，每一个按钮都可以与一个 Python 的函数或方法与之相关联，当按钮被按下时，对应的函数或方法将被自动执行。

Radiobutton 组件仅能显示单一字体的文本，但文本可以跨越多行。另外，还可以为其中的个别字符加上下划线。默认情况下，tab 按键被用于在按钮间切换。

每一组 Radiobutton 组件应该只与一个变量相关联，然后每一个按钮表示该变量的单一值。

## 用法

为了实现其“单选”行为，确保一组中的所有按钮的 variable 选项都使用同一个变量，并使用 value 选项来指定每个按钮代表什么值：

```python
import tkinter as tk
master = tk.Tk()

v = tk.IntVar()
v.set(2)
 
tk.Radiobutton(master, text="One", variable=v, value=1).pack(anchor="w")
tk.Radiobutton(master, text="Two", variable=v, value=2).pack(anchor="w")
tk.Radiobutton(master, text="Three", variable=v, value=3).pack(anchor="w")
master.mainloop()
```

![单选](图\单选.png)

上图是一个普通的单选按钮样式，如果将它的 indicatoron 选项设置为 False，Radiobutton 的样式就会变成普通按钮的样式了：

```python
import tkinter as tk

master = tk.Tk()

v = tk.IntVar()
v.set(2)

tk.Radiobutton(master, text="One", variable=1, value=1,indicatoron=False).pack(anchor="w")
tk.Radiobutton(master, text="Two", variable=1, value=2,indicatoron=False).pack(anchor="w")
tk.Radiobutton(master, text="Three", variable=1, value=3,indicatoron=False).pack(anchor="w")
master.mainloop()
```

![单选2](图\单选2.png)

Radiobutton(master=None, options)

* master -- 父组件

* options -- 组件选项，下方表格详细列举了各个选项的具体含义和用法：

| 选项         | 描述                                                         |
| ------------ | ------------------------------------------------------------ |
| command      | 1. 指定于该按钮相关联的函数或方法<br/> 2. 当按钮被按下时由 Tkinter 自动调用对应的函数或方法 <br/>3. 如果不设置此选项，那么该按钮被按下后啥事儿也不会发生 |
| variable     | 1. 与 Radiobutton 组件关联的变量  <br/>2. 同一组中的所有按钮的 variable 选项应该都指向同一个变量  <br/>3. 通过将该变量与 value 选项的值对比，即可判断用户选中了哪个按钮 |
| value        | 1. 标志该单选按钮的值  <br/>2. 在同一组中的所有按钮应该拥有各不相同的值  <br/>3. 通过将该值与 variable 选项的值对比，即可判断用户选中了哪个按钮 |
| selectcolor  | 1. 选择框的颜色 2. 默认值由系统指定                          |
| selectimage  | 1. 设置当 Radiobutton 为选中状态的时候显示的图片 2. 如果没有指定 image 选项，该选项被忽略 |
| textvariable | 1. Radiobutton 显示 Tkinter 变量（通常是一个 StringVar 变量）的内容 2. 如果变量被修改，Radiobutton 的文本会自动更新 |

书上163页例子

`9-4.py`

```python
from tkinter import *

Window = Tk(className='单选按钮选择')  # 创建'单选按钮'窗口
v = IntVar()
# 列表中存储的是元素是元组
language = [('Python', 0), ('C', 1), ('Java', 2)]


# 定义单选按钮的响应函数
def callRadiobutton():
    for i in range(3):
        if (v.get() == i):
            Window1 = Tk(className='选择的结果')
            Label(Window1, text='你的选择是' + language[i][0] + '语言', font=('楷体', 13), fg='white', bg='purple', width=40,
                  height=4).pack()
            Button(Window1, text='确定', width=6, height=2, command=Window1.destroy).pack(side='bottom')


Label(Window, text='选择一门你喜欢的编程语言').pack(anchor='center')
# for循环创建单选按钮
for lan, num in language:
    Radiobutton(Window, text=lan, value=num, command=callRadiobutton, variable=v).pack(anchor='w')
v.set(1)  # 将v的值设置为1，即选中选中value=1的按钮
Window.mainloop()
```

![9-4.1](图\9-4.1.png)

![9-4.2](图\9-4.2.png)

* 注意：variable选项的功能主要用于传参和绑定变量。variable是双向绑定的，即如果绑定的变量的值发生变化，则随之绑定的组件也会变化。variable绑定的变量的主要类型如下

```
x = StringVar()  #创建一个StringVar类型变量x，默认值为''
x = IntVar()  #创建一个IntVar类型变量x，默认值为1
x = BooleanVar()  #创建一个BooleanVar类型变量x，默认值为False
```

# 4 多行文本框组件

## 4.1 简介

Text(多行文本框)类用于显示和编辑多行文本，此外还可以用来显示网页链接、图片、HTML页面等。 因此, 也被当做简单的文本处理器, 文本编辑器或者网页浏览器来使用. 比如:IDLE就是Text组件构成的

可以使用Text实例的insert()方法，结合指定插入位置的INSERT或END属性来实现文本的插入。

## 4.2 用法

可以调用Text对象的insert()方法在指定的位置处插入文本，插入位置介绍如下

* INSERT：表示在光标位置插入
* CURRENT：表示在当前的光标位置插入，与INSERT功能类似
* END：表示在整个文本的末尾插入
* SEL_FIRST：表示在选中文本的开始插入
* SEL_LAST：表示在选中文本的最后插入

书上164页例子

`9-5.py`

```python
from tkinter import *
window = Tk()
t = Text(window, font='device')   #font设置文本的显示字体
t.insert(INSERT, '披绣闼，俯雕甍，山原旷其盈视，川泽纡其骇瞩。\
闾阎扑地，钟鸣鼎食之家；舸舰迷津，青雀黄龙之舳。云销雨霁，彩彻区明。\
落霞与孤鹜齐飞，秋水共长天一色。\
渔舟唱晚，响穷彭蠡之滨，雁阵惊寒，声断衡阳之浦。')
# 定义各个Button的回调函数，这些函数使用了内置的mark:INSERT/CURRENT/END/SEL_FIRST/SEL_LAST
def insertText():
    t.insert(INSERT, '（滕王阁序，王勃）')
def currentText():
    t.insert(CURRENT, '（滕王阁序，王勃）')
def endText():
    t.insert(END, '（滕王阁序，王勃）')
def sel_FirstText():
    t.insert(SEL_FIRST, '（滕王阁序，王勃）')
def sel_LastText():
    t.insert(SEL_LAST, '（滕王阁序，王勃）')
#在光标位置插入
Button(window,text='at INSERT insert',anchor = 'w',width=17,command=insertText).pack()
#在当前的光标位置插入
Button(window,text='at CURRENT insert',anchor = 'w', width=17, command=insertText).pack()
#在整个文本的末尾插入
Button(window,text='at END insert',anchor = 'w',width=17,command=endText).pack()
#在选中文本的开始插入,如果没有选中区域则会引发异常
Button(window,text='at SEL_FIRST insert',anchor = 'w', width=17, command=sel_FirstText).pack()
#在选中文本的最后插入，如果没有选中区域则会引发异常
Button(window,text='at SEL_LAST insert',anchor = 'w', width=17, command=sel_LastText).pack()
t.pack()
window.mainloop()
```

<img src="图\9-5.1.png" alt="9-5.1" style="zoom:50%;" />

加入图片的例子，书上165页

`9-6.py`

```python
from tkinter import *
window = Tk()
window.title('江南好风景')
text1 = Text(window, height=27, width=60)
photo=PhotoImage(file=r'E:\科师\2021春资料\课程\python\课件\第九章 '
                      r'图形用户界面设计\图\江南.gif')
text1.insert(END,'\n')
text1.image_create(END, image=photo)
text1.pack(side=LEFT)
text2 = Text(window, height=27, width=45)
#使用tag_configure()方法创建一个指定字体的Tag，名字为font1
text2.tag_configure('font1', font=('Verdana', 20, 'bold'))
#使用tag_configure()方法创建一个指定字体和前景色的Tag，名字为colorfont
text2.tag_configure('colorfont', foreground='#42426F', font=('Tempus Sans ITC', 13, 'bold'))
text2.insert(END,'\n       江南的雨江南的你\n', 'font1')
commentary = "      望不穿江南尽头谁在痴痴等待，只叹一别万年的窗外，你能否看见我的期待。\n  \
    你紫花裙的影迹，携带淡妆从朦胧雨帘中渐渐褪去。\
清风细雨，让心跳节奏到极致，我思念远方还在的你，\
让我走近一点，再走近一些，明白一切甚有味道。\n  \
    江南的风景，江南的你，夜幕的流水，多情的雨。原来都跟着烟花的记忆，也只是瞬间的美丽…… "
text2.insert(END, commentary, 'colorfont')
text2.pack(side=LEFT)
window.mainloop()
```

![9-6](图\9-6.png)

# 5 Checkbutton（多选按钮）组件

## 5.1 简介

Checkbutton（多选按钮）组件用于实现确定是否选择的按钮。Checkbutton 组件可以包含文本或图像，你可以将一个 Python 的函数或方法与之相关联，当按钮被按下时，对应的函数或方法将被自动执行。

Checkbutton 组件仅能显示单一字体的文本，但文本可以跨越多行。另外，还可以为其中的个别字符加上下划线。默认情况下，tab 按键被用于在按钮间切换。

## 5.2 参数

Checkbutton(master=None, options) 

* master -- 父组件

* options -- 组件选项，下方表格详细列举了各个选项的具体含义和用法：

| **选项** | **含义**                                                     |
| -------- | ------------------------------------------------------------ |
| command  | 1. 指定于该按钮相关联的函数或方法 2. 当按钮被按下时由 Tkinter 自动调用对应的函数或方法 3. 如果不设置此选项，那么该按钮被按下后啥事儿也不会发生 |
| variable | 1. 将 Checkbutton 跟一个 Tkinter 变量关联 2. 当按钮按下时，该变量在 onvalue 和 offvalue 之间切换 3. 这个切换的过程是完全自动的 |
| onvalue  | 1. 默认情况下，variable 选项设置为 1 表示选中状态，反之设置为 0 2. 设置 onvalue 的值可以自定义选中状态的值（详见上方用法举例） |
| offvalue | 1. 默认情况下，variable 选项设置为 1 表示选中状态，反之设置为 0 2. 设置 offvalue 的值可以自定义未选中状态的值（详见上方用法举例） |

书上167页例子

`9-7.py`

```
from tkinter import *
window=Tk(className='你最喜欢的城市') #创建'你最喜欢的城市'窗口
window.geometry("300x200")     #设定窗口大小
# 添加标签
Label(window,text='请选择自己喜欢的城市（多选）：',fg='blue').pack()
# 定义复选框的事件处理函数
def callCheckbutton():
    msg = ''
    if var1.get() == 1:     #因为var1是IntVar型变量，选中为1，不选为0
        msg += "西安\n"
    if var2.get() == 1:
        msg += "洛阳\n"
    if var3.get() == 1:
        msg += "北京\n"
    if var4.get() == 1:
        msg += "南京\n"
    '''清除text中的内容，0.0表示从第一行第一个字开始清除，END表示清除到最后结束'''
    text.delete(0.0,END)
    text.insert('insert',msg)  #INSERT表示在光标位置插入msg所指代的文本
#创建四个复选框
var1 = IntVar()       #创建IntVar型数据对象
Checkbutton(window,text='西安',variable=var1,command=callCheckbutton).pack()
var2 = IntVar()
Checkbutton(window,text='洛阳',variable=var2,command=callCheckbutton).pack()
var3 = IntVar()
Checkbutton(window,text='北京',variable=var3,command=callCheckbutton).pack()
var4 = IntVar()
Checkbutton(window,text='南京',variable=var4,command=callCheckbutton).pack()
# 创建一个文本框
text = Text(window,width=30,height=10)
text.pack()
window.mainloop()

```

![9-7](图\9-7.png)

书上168页例子

`9-8.py`

```python
from tkinter import *
window = Tk()
def callCheckbutton():
   #改变v1的值，即改变Checkbutton 的显示文本
   if v1.get()=='男':
      print("当前Checkbutton本身的值:", v2.get())
      v1.set('女')
      print("当前设置的按钮显示文本是:",v1.get())
   elif v1.get()=='女' :
      print("当前Checkbutton本身的值:", v2.get())
      v1.set('男')
      print("当前设置的按钮显示文本是:",v1.get())
v1 = StringVar()   #创建tkinter的StringVar型数据对象
v2 = IntVar()      #创建tkinter的IntVar型数据对象
#绑定v1到Checkbutton的属性textvariable，绑定v2到Checkbutton的属性variable
Checkbutton(window,text = '女',variable = v2,textvariable = v1,command = callCheckbutton).pack()
v1.set('男')
window.mainloop()
```

![9-8.1](图\9-8.1.png)

![9-8.2](图\9-8.2.png)

# 6 Listbox（列表框）组件

## 6.1 简介

Listbox（列表框）组件用于显示一个选择列表。Listbox 只能包含文本项目，并且所有的项目都需要使用相同的字体和颜色。根据组件的配置，用户可以从列表中选择一个或多个选项。

Listbox 组件通常被用于显示一组文本选项，Listbox 组件跟 Checkbutton和 Radiobutton 组件类似，不过 Listbox 是以列表的形式来提供选项的（后两个是通过按钮的形式）。

## 6.2 用法

当你创建一个 Listbox 组件的时候，它是空的，所以第一件要做的事就是添加一行或多行文本进去。我们使用 insert() 方法添加文本，该方法有两个参数：第一个参数是插入的索引号，第二个参数是插入的字符串。索引号通常是项目的序号（0 是列表中第一项的序号）。

```Python
import tkinter as tk
master = tk.Tk()
# 创建一个空列表
theLB = tk.Listbox(master)
theLB.pack()
# 往列表里添加数据
for item in ["鸡蛋", "鸭蛋", "鹅蛋", "李狗蛋"]:
   theLB.insert("end", item)

master.mainloop()
```

![9-9.1](图\9-9.1.png)

使用 delete() 方法删除列表中的项目，最常用的操作是删除列表中的所有项目`listbox.delete(0, "end")`

不过你也可以使用一些特殊的索引号：比如 ACTIVE 表示选中的项目（如果 Listbox 允许多选，那么它表示最后一个被选中的项目）；又如 END 表示 Listbox 的最后一行，所以当要插入一个项目到列表时可以使用 END：

```python
import tkinter as tk
master = tk.Tk()
# 创建一个空列表
theLB = tk.Listbox(master)
theLB.pack()

# 往列表里添加数据
for item in ["鸡蛋", "鸭蛋", "鹅蛋", "李狗蛋"]:
    theLB.insert("end", item)

theButton = tk.Button(master, text="删除", command=lambda x=theLB: x.delete("active"))
theButton.pack()

master.mainloop()
```

![9-9.2](图\9-9.2.png)

Listbox(master=None, options)

* master -- 父组件

* options -- 组件选项，下方表格详细列举了各个选项的具体含义和用法：

| **选项**     | **含义**                                                     |
| ------------ | ------------------------------------------------------------ |
| setgrid      | 1. 指定一个布尔类型的值，决定是否启用网格控制 2. 默认值是 False |
| selectmode   | 1. 决定选择的模式 <br/>2. 四种不同的选择模式："single"（单选）、"browse"（也是单选，但拖动鼠标或通过方向键可以直接改变选项）、"multiple"（多选）和 "extended"（也是多选，但需要同时按住 Shift 键或 Ctrl 键或拖拽鼠标实现）<br/>\3. 默认是 "browse" |
| listvariable | 1. 指向一个 StringVar 类型的变量，该变量存放 Listbox 中所有的项目 2. 在 StringVar 类型的变量中，用空格分隔每个项目，例如 var.set("鸡蛋 鸭蛋 鹅蛋 李狗蛋") |

令lb表示一个Listbox对象，常用的方法

| 方法                     | 描述                                                         |
| ------------------------ | ------------------------------------------------------------ |
| insert(index,item)       | -- 添加一个或多个项目到 Listbox 中<br/>-- 使用 lb.insert("end") 添加新选项到末尾 |
| delete(first, last=None) | -- 删除参数 first 到 last 范围内（包含 first 和 last）的所有选项<br/>-- 如果忽略 last 参数，表示删除 first 参数指定的选项 |
| get(first, last=None)    | -- 删除参数 first 到 last 范围内（包含 first 和 last）的所有选项<br/>-- 如果忽略 last 参数，表示删除 first 参数指定的选项 |
| size()                   | -- 返回 Listbox 组件中选项的数量                             |
| curselection()           | -- 返回一个元组，包含被选中的选项的序号（从 0 开始）<br/>-- 如果没有选中任何选项，返回一个空元组 |

创建多选的列表，书上170页

`9-10.py`

```python
from tkinter import *   
window = Tk()
#属性MULTIPLE允许多选，依次点击三个item，均显示为选中状态  
lb = Listbox(window, selectmode = MULTIPLE, font=('楷体', 14)) 
for item in ['Python','Java','C语言']:  
    lb.insert(END, item)  
lb.pack()  
window.mainloop()

```

![9-10](图\9-10.png)

书上170页9-11例子

`9-11.py`

```python
from tkinter import *   
window=Tk(className='Listbox使用举例') #创建'Listbox使用举例'窗口
Str=StringVar()
lb = Listbox(window, selectmode = MULTIPLE, font=('楷体', 14),listvariable=Str)
#属性MULTIPLE允许多选，依次点击三个item，均显示为选中状态
for item in ['Python','Java','C语言']:  
    lb.insert(END, item)
def callButton1():
    print(Str.get())
def callButton2():
    for i in lb.curselection():
        print(lb.get(i))
lb.pack()
Button(window,text='获取Listbox的所有内容',command=callButton1,width=20).pack()
Button(window,text='获取Listbox的选中内容',command=callButton2,width=20).pack()
window.mainloop()
```

![9-11](图\9-11.png)

# 7 Menu（菜单）组件

## 7.1 简介

Menu（菜单）组件用于实现顶级菜单、下拉菜单和弹出菜单。Menu 组件通常被用于实现应用程序上的各种菜单，由于该组件是底层代码实现，所以不建议你自行通过按钮和其他组件来实现菜单功能。

## 7.2 参数

Menu(master=None, options) 

* master -- 父组件

* options -- 组件选项，下方表格详细列举了各个选项的具体含义和用法：

| 选项        | 描述                                                         |
| ----------- | ------------------------------------------------------------ |
| postcommand | 将此选项与一个方法相关联，当菜单被打开的时候该方法将自动被调用 |
| font        | 指定 Menu 中文本的字体                                       |
| foreground  | 设置 Menu 的前景色                                           |

**add_command(\**options)**
-- 添加一个普通的命令菜单项
-- 相当于 add("command", **options)

**add_checkbutton(\**options)**
-- 添加一个多选按钮的菜单项
-- 相当于 add("checkbutton", **options)

**add_radiobutton(\**options)**
-- 添加一个单选按钮的菜单项
-- 相当于 add("radiobutton", **options)

**insert_separator(index, \**options)**
-- 在 index 参数指定的位置添加一条分割线
-- 相当于 insert("separator", **options)

**insert_cascade(index, \**options)**
-- 在 index 参数指定的位置添加一个父菜单
-- 相当于 insert("cascade", **options)



* 例子1

创建一个顶级菜单，你需要先创建一个菜单实例，然后使用 add() 方法将命令和其它子菜单添加进去：

```
import tkinter as tk
root = tk.Tk()
def callback():
    print("~被调用啦~")

# 创建一个顶级菜单
menubar = tk.Menu(root)
menubar.add_command(label="Hello", command=callback)
menubar.add_command(label="Quit", command=root.quit)

# 显示菜单
root.config(menu=menubar)
root.mainloop()
```

![9-11.1](图\9-11.1.png)

* 例子2

创建一个下拉菜单（或者其他子菜单），方法也是大同小异，最主要的区别是它们最后需要添加到主菜单上（而不是窗口上）：

```python
import tkinter as tk

root = tk.Tk()
def callback():
    print("~被调用了~")
# 创建一个顶级菜单
menubar = tk.Menu(root)

# 创建一个下拉菜单“文件”，然后将它添加到顶级菜单中
filemenu = tk.Menu(menubar, tearoff=False)
filemenu.add_command(label="打开", command=callback)
filemenu.add_command(label="保存", command=callback)
filemenu.add_separator()
filemenu.add_command(label="退出", command=root.quit)
menubar.add_cascade(label="文件", menu=filemenu)

# 创建另一个下拉菜单“编辑”，然后将它添加到顶级菜单中
editmenu = tk.Menu(menubar, tearoff=False)
editmenu.add_command(label="剪切", command=callback)
editmenu.add_command(label="拷贝", command=callback)
editmenu.add_command(label="粘贴", command=callback)
menubar.add_cascade(label="编辑", menu=editmenu)

# 显示菜单
root.config(menu=menubar)

root.mainloop()
```

![9-11.2](图\9-11.2.png)

书上173页例子9-13

`9-13.py`

```python
from tkinter import *
window = Tk()
menubar = Menu(window)    # 窗口下创建一个主菜单
fsubmenu = Menu(menubar)   #在主菜单下创建子菜单
#在子菜单下创建添加菜单项
for item in ['New file','Open','Save']:
    fsubmenu.add_command(label=item)
fsubmenu.add_separator()    #给菜单项添加分割线
#继续在子菜单实例下创建菜单项
for item in ['Close','Exit']:
    fsubmenu.add_command(label=item)
esubmenu = Menu(menubar)             #在主菜单下创建子菜单
for item in ['Undo','Redo','Cut','Copy']:
    esubmenu.add_command(label=item)  #为esubmenu菜单添加菜单项

rsubmenu = Menu(menubar)   #在主菜单实例下创建子菜单
for item in ['Python Shell','Check Module','Run Module']:
    rsubmenu.add_command(label=item)
#为主菜单添加下拉菜单
menubar.add_cascade(label='File',menu=fsubmenu)  # fsubmenu成为File的下拉菜单
menubar.add_cascade(label='Edit',menu=esubmenu)
menubar.add_cascade(label='Run',menu=rsubmenu)
window['menu']= menubar  #将主菜单实例menu添加到窗口中 
window.mainloop()
```

![9-13](图\9-13.png)

# 8 Message消息组件

Message（消息）组件是 Label 组件的变体，用于显示多行文本消息。Message 组件能够自动换行，并调整文本的尺寸使其适应给定的尺寸。

Message 组件用于显示简单的文本消息，通常你可以使用 Label 来代替。如果你希望使用多种字体来显示文本，那么应该使用 Text 组件。

创建一个 Message 组件，所有你要做的事就是指定要显示的文本内容。在必要的时候，该组件会自动换行，请随意感受下：

书上174页例子9-14

`9-14.py`

```python
from tkinter import *  
window = Tk()  
# 执行程序，text中的内容自动多行显示对齐，Label没有这个功能
Message(window, text="Genius only means hard-working.",fg='white',bg = 'grey',).pack()  
#如果不想让text中的内容自动多行显示，需要指定足够大的宽度  
Message(window, text="Genius only means hard-working.", width=300).pack()  
window.mainloop()  
```

![9-14](图\9-14.png)

# 9 消息窗口

tkmegbox.某种窗口（title，message[，options]）

所有的这些函数都有相同的参数：

- title 参数毋庸置疑是设置标题栏的文本
- message 参数是设置对话框的主要文本内容，你可以用 '\n' 来实现换行
- options 参数可以设置的选项和含义如下表所示

常见的提示窗口有这几种：

* askokcancel
  askquestion
  askretrycancel
  askyesno
  showinfo
  showerror
  showwarning

书上175页例子

`9-15.py`

```python
from tkinter import *
import tkinter.messagebox
def info_warn():
    a=tkinter.messagebox.showinfo("平凡的世界经典对白","这就是生命!没有什么力量能扼杀生命。下一句，点确定！")
    a=tkinter.messagebox.showinfo("平凡的世界经典对白","生命是这样顽强，它对抗的是整整一个严寒的冬天。下一句，点确定！")
    a=tkinter.messagebox.showinfo("平凡的世界经典对白", "冬天退却了，生命之花却蓬勃地怒放。下一句，点确定！")
    a=tkinter.messagebox.showinfo("平凡的世界经典对白", "你，为了这瞬间的辉煌，忍耐了多少暗淡无光的日月?下一句，点确定！")
    a=tkinter.messagebox.showwarning("平凡的世界经典对白", "只要春天不死，就会有迎春的花朵年年岁岁开放。这是最后一句对白，点击确定退出！")

def func2():
    a=tkinter.messagebox.askyesno("人","你都不理我了。点是返回答案")
    a=tkinter.messagebox.askokcancel("机器","我怎么不理你？点确定继续问话！")
    a=tkinter.messagebox.askquestion("人","荣耀6plus多少钱?想知道多少钱点是")
    a=tkinter.messagebox.askretrycancel("机器"," 京东大哥说过是2,899元哦。")
    a=tkinter.messagebox.askyesnocancel("人","你知道的真多呀。")
    a=tkinter.messagebox.showwarning("机器", "我应该的呀。")
    if tkinter.messagebox.askyesno("你没问题了吗？", "确认关闭窗口吗!"):
        window.destroy()

window=Tk()
window.title("消息框")
Button(window,text="平凡的世界经典对白消息框", command= info_warn ).pack()
Button(window,text="对话框",command=func2).pack()
window.mainloop()
```

结果自行演示



# 10 filedialog（文件对话框）

当你的应用程序需要使用打开文件或保存文件的功能时，文件对话框显得尤为重要。

实现起来就是这样：

```Python
import tkinter as tk
from tkinter import filedialog
root = tk.Tk()

def callback():
    #fileName = tk.filedialog.askopenfilename()   #报错，这个问题出现的原因是filedialog是tkinter的一个模块，而不是一个函数或性质。这样调用的办法是不对的。
    fileName = filedialog.askopenfilename()
    print(fileName)

tk.Button(root, text="打开文件", command=callback).pack()

root.mainloop()
```

![10-1](图\10-1.png)

![10-2](图\10-2.png)

# 11 colorchooser（颜色选择对话框）

颜色选择对话框提供一个友善的界面让用户选择需要的颜色，大家看下例子：

```Python
import tkinter as tk
from tkinter import colorchooser
root = tk.Tk()


def callback():
    fileName = tk.colorchooser.askcolor()
    print(fileName)


tk.Button(root, text="选择颜色", command=callback).pack()

root.mainloop()
```

![10-3](图\10-3.png)

![10-4](图\10-4.png)

# 12 Entry（输入框）组件

Entry（输入框）组件通常用于获取用户的输入文本。Entry 组件仅允许用于输入一行文本，如果用于输入的字符串长度比该组件可显示空间更长，那内容将被滚动。这意味着该字符串将不能被全部看到（你可以用鼠标或键盘的方向键调整文本的可见范围）。

Entry(master=None, options)

* master -- 父组件

* options -- 组件选项，下方表格详细列举了各个选项的具体含义和用法：

| **选项**          | **含义**                                                     |
| ----------------- | ------------------------------------------------------------ |
| show              | 1. 设置输入框如何显示文本的内容 2. 如果该值非空，则输入框会显示指定字符串代替真正的内容 3. 将该选项设置为 "*"，则是密码输入框 |
| selectbackground  | 1. 指定输入框的文本被选中时的背景颜色 2. 默认值由系统指定    |
| selectborderwidth | 1. 指定输入框的文本被选中时的边框宽度（选中边框） 2. 默认值由系统指定 |
| selectforeground  | 1. 指定输入框的文本被选中时的字体颜色 2. 默认值由系统指定    |
| textvariable      | 1. 指定一个与输入框的内容相关联的 Tkinter 变量（通常是 StringVar） 2. 当输入框的内容发生改变时，该变量的值也会相应发生改变 |

## 12.1 变量绑定

书上176例子

txet属性对单行文本不起作用，可以通过textvariable属性指定一个与输入框内容相关的变量。

`9-16.py`

```python
from tkinter import *  
window = Tk()
entry1=Entry(window,text = 'input your text here')
entry1.pack()
v = StringVar() 
# 绑定字符串变量v
entry2 = Entry(window,textvariable = v)
v.set('获取：')
entry2.pack()
window.mainloop()

```

![9-16](图\9-16.png)

## 12.2 如何显示文本的内容

核心是**show**的用法：

show=1，那么所有输入都显示为1，其他类似；show=None，那么输入什么就显示什么。

书上177页例子9-17

`9-17.py`

```python
from tkinter import *
window=Tk(className='输入账号密码') #创建'输入账号密码'窗口
Label(window, text='账号:').grid(row=0,column=0)
Label(window, text='密码:').grid(row=1,column=0)
entry1 = Entry(window,font=('楷体', 14))
entry2 = Entry(window,show='*',font=('楷体', 14))
entry1.grid(row=0,column=1, padx=10, pady=5)
entry2.grid(row=1,column=1, padx=10, pady=5) 
window.mainloop()
```

![9-17](图\9-17.png)

**get()**

-- 获得当前输入框的内容

# 13 Frame（框架）组件

Frame（框架）组件是在屏幕上的一个矩形区域。Frame 主要是作为其他组件的框架基础，或为其他组件提供间距填充。

书上177也例子9-18

`9-18.py`

```python
from tkinter import *
window = Tk()
'''创建Frame组件的方法与其他创建组件的方法不同，第一个参数不是window，也可以不加任何参数'''
frame1 = Frame(height = 20,width = 400,bg = "grey")
frame1.pack()
redbutton = Button(frame1, text="Redbutton", fg="white",bg='blue')
redbutton.pack( side = LEFT)
brownbutton = Button(frame1, text="Brownbutton", fg="brown",bg='yellow')
brownbutton.pack( side = RIGHT )
bluebutton = Button(frame1, text="Bluebutton", fg="blue",bg='white')
bluebutton.pack( side = LEFT )
frame2 = Frame()
frame2.pack()
# redbutton被添加到Frame2中了，而不是window默认的最上方。
redbutton = Button(frame2, text="Redbutton", fg="white",bg='blue')
redbutton.pack( side = LEFT)
brownbutton = Button(frame2, text="Brownbutton", fg="brown",bg='yellow')
brownbutton.pack( side = LEFT )
bluebutton = Button(frame2, text="Bluebutton", fg="blue",bg='white')
bluebutton.pack( side = LEFT )
window.mainloop()
```

![9-18](图\9-18.png)

