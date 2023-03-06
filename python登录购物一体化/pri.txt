#商场界面
import random#随机数产生
import xlrd
from xlutils.copy import copy
from tkinter import *
import re  # 注册需要的
import tkinter as tk
import tkinter.messagebox

# ----------------------------登录的全局变量------------------------------------------
data = xlrd.open_workbook("1.xls")
table = data.sheet_by_name("个人信息")

a = table.col_values(0)  #从电脑里边读入本来已经存储有的账号
b = table.col_values(1)  #密码
end=0 #记录最后一行的

for i in a:
    a[end] = int(a[end])  # 强制类型转换
    if b[end]!=str(b[end]): #跳过字符串的  否则全是数字时会有小数点
        b[end] = str(int(b[end]))  # 强制类型转换 去掉小数点
    end=end+1

date = dict(zip(a, b))  # 压缩成字典 # 建立字典date  键为账号 值为密码 压缩成字典后键值自动转换为str了

ZH = end
MM = end
#print(date)  #*********************
# --------------------------------------------------------------------------------

# -----------------------------购物系统的全局变量-----------------------------------------
#用来记录 有没有勾选商品的
ad = 0
ad1 = 0
ad2 = 0
ad3 = 0
ad4 = 0
ad5 = 0

sjs = 0#验证码
gold = random.randint(100, 1000)  # 初始化给用户一个金额*************
# ---------------------------------------------------------------------------

def mall():#商场********************************************************
    # 窗口变量
    window = Tk()
    # 窗口标题
    window.title('商品信息')
    # 窗口大小
    window.geometry('800x500+600+250')
    # 画布大小设置
    frm2 = Frame(window)
    frm2.config(bg='orange', width=800, height=500, )
    frm2.place(x=0, y=0)  # 规定框架的起始位置
    photo = PhotoImage(file=r'球\bj1.png')
    aaa = Label(frm2, text='', image=photo, ).place(x=0, y=0)  # 插入背景及规定起始位置

    data = xlrd.open_workbook("1.xls")
    table = data.sheet_by_name("商品信息")

    a = table.col_values(0)  # 提取商品信息
    b = table.col_values(1)

    end = 0  # 记录最后一行的

    for i in a:
        b[end] = str(int(b[end]))  # 强制类型转换
        end = end + 1

    date = dict(zip(a, b))  # 压缩成字典 # 建立字典date
    print(date)

    # #加载图片
    # image_file = PhotoImage(file=r'球\1.png')
    # image_file1 = PhotoImage(file=r'球\2.png')
    # image_file2 = PhotoImage(file=r'球\3.png')
    # image_file3 = PhotoImage(file=r'球\4.png')
    # image_file4 = PhotoImage(file=r'球\5.png')
    # image_file5 = PhotoImage(file=r'球\6.png')

    # 价格的位置
    tiaol1 = Text(frm2, width=7, height=1, bg="white", fg="black")  # 用来放选项内容 存放商品数量
    tiaol1.place(x=75, y=182)  # 存放商品数量位置 小窗口
    tiaol1.insert('insert', '$.' + b[0] + '元')  # INSERT表示在光标位置插入msg所指代的文本

    tiaol2 = Text(frm2, width=7, height=1, bg="white", fg="black")  # 用来放选项内容 存放商品数量
    tiaol2.place(x=230, y=182)  # 存放商品数量位置 小窗口
    tiaol2.insert('insert', '$.' + b[1] + '元')  # INSERT表示在光标位置插入msg所指代的文本

    tiaol3 = Text(frm2, width=7, height=1, bg="white", fg="black")  # 用来放选项内容 存放商品数量
    tiaol3.place(x=385, y=182)  # 存放商品数量位置 小窗口
    tiaol3.insert('insert', '$.' + b[2] + '元')  # INSERT表示在光标位置插入msg所指代的文本

    tiaol4 = Text(frm2, width=7, height=1, bg="white", fg="black")  # 用来放选项内容 存放商品数量
    tiaol4.place(x=75, y=380)  # 存放商品数量位置 小窗口
    tiaol4.insert('insert', '$.' + b[3] + '元')  # INSERT表示在光标位置插入msg所指代的文本

    tiaol5 = Text(frm2, width=7, height=1, bg="white", fg="black")  # 用来放选项内容 存放商品数量
    tiaol5.place(x=230, y=380)  # 存放商品数量位置 小窗口
    tiaol5.insert('insert', '$.' + b[4] + '元')  # INSERT表示在光标位置插入msg所指代的文本

    tiaol6 = Text(frm2, width=7, height=1, bg="white", fg="black")  # 用来放选项内容 存放商品数量
    tiaol6.place(x=385, y=380)  # 存放商品数量位置 小窗口
    tiaol6.insert('insert', '$.' + b[5] + '元')  # INSERT表示在光标位置插入msg所指代的文本

    # 添加标签
    Label(frm2, text='请选择购买（可多选）', fg='blue').place(x=403, y=477)
    Label(frm2, text='选购商品如下所示：', fg='blue', font=('楷体', 14), ).place(x=550, y=100)

    # 定义复选框的事件处理函数
    def callCheckbutton():
        msg = ''
        if var1.get() == 1:  # 因为var1是IntVar型变量，选中为1，不选为0  如果它没有被选中  那么加再多也不给它
            msg += "【耐克篮球】\n"
        if var2.get() == 1:
            msg += "【李宁篮球】\n"
        if var3.get() == 1:
            msg += "【准者篮球】\n"
        if var4.get() == 1:
            msg += "【威尔胜篮球】\n"
        if var5.get() == 1:
            msg += "【斯伯丁篮球】\n"
        if var6.get() == 1:
            msg += "【安踏篮球】\n"

        '''清除text中的内容，0.0表示从第一行第一个字开始清除，END表示清除到最后结束'''
        text.delete(0.0, END)
        text.insert('insert', msg)  # INSERT表示在光标位置插入msg所指代的文本

    # 以下是用来放入已经勾选商品的文本框的  多选累计
    def add():
        global ad
        tiaol = Text(window, width=3, height=1)  # 用来放选项内容 存放商品数量
        tiaol.place(x=68, y=246)  # 存放商品数量位置 小窗口
        if var1.get() == 1:  # 因为var1是IntVar型变量，选中为1，不选为0  如果它没有被选中  那么加再多也不给它
            ad = ad + 1
            tiaol.insert('insert', ad)  # INSERT表示在光标位置插入msg所指代的文本
        elif var1.get() == 0:
            tiaol.delete(0.0, END)
            tiaol.insert('insert', 0)  # INSERT表示在光标位置插入msg所指代的文本  # 没有勾选时清空文本框
            ad = 0
        # print(ad)

    def add1():
        global ad1
        tiaol = Text(window, width=3, height=1)  # 用来放选项内容
        tiaol.place(x=225, y=246)
        if var2.get() == 1:
            ad1 = ad1 + 1
            tiaol.insert('insert', ad1)  # INSERT表示在光标位置插入msg所指代的文本
        elif var1.get() == 0:
            tiaol.delete(0.0, END)
            tiaol.insert('insert', 0)  # INSERT表示在光标位置插入msg所指代的文本  # 没有勾选时清空文本框
            ad1 = 0
        # print(ad1)

    def add2():
        global ad2
        tiaol = Text(window, width=3, height=1)  # 用来放选项内容
        tiaol.place(x=380, y=246)
        if var3.get() == 1:
            ad2 = ad2 + 1
            tiaol.insert('insert', ad2)
        elif var1.get() == 0:
            tiaol.delete(0.0, END)
            tiaol.insert('insert', 0)  # 没有勾选时清空文本框
            ad2 = 0
        # print(ad2)

    def add3():
        global ad3
        tiaol = Text(window, width=3, height=1)  # 用来放选项内容
        tiaol.place(x=68, y=447)
        if var4.get() == 1:
            ad3 = ad3 + 1
            tiaol.insert('insert', ad3)
        elif var1.get() == 0:
            tiaol.delete(0.0, END)
            tiaol.insert('insert', 0)  # 没有勾选时清空文本框
            ad3 = 0
        # print(ad3)

    def add4():
        global ad4
        tiaol = Text(window, width=3, height=1)  # 用来放选项内容
        tiaol.place(x=225, y=447)
        if var5.get() == 1:
            ad4 = ad4 + 1
            tiaol.insert('insert', ad4)
        elif var1.get() == 0:
            tiaol.delete(0.0, END)
            tiaol.insert('insert', 0)  # 没有勾选时清空文本框
            ad4 = 0
        # print(ad4)

    def add5():
        global ad5
        tiaol = Text(window, width=3, height=1)  # 用来放选项内容
        tiaol.place(x=380, y=447)
        if var6.get() == 1:
            ad5 = ad5 + 1
            tiaol.insert('insert', ad5)  # INSERT表示在光标位置插入msg所指代的文本
        elif var1.get() == 0:
            tiaol.delete(0.0, END)
            tiaol.insert('insert', 0)  # 没有勾选时清空文本框
            ad5 = 0
        # print(ad5)

    #   购物车********************************************************
    def cat():

        windows = Tk()
        windows.title("购物车")
        windows.geometry('560x400+660+300')
        frm3 = Frame(windows)

        frm3.config(width=560, height=400, )
        frm3.place(x=0, y=0)
        photo = PhotoImage(file=r'车\gwc_beijing.png')
        aaa = Label(frm3, text='', image=photo, ).place(x=0, y=0)  # 插入背景及规定起始位置

        text2 = Text(frm3, width=40, height=12, font=('楷体', 12), )  # 用来放选项内容的文本框
        text2.place(x=115, y=80)
        t1 = '*'
        t2 = '='

        def ccct():
            if ad > 0:
                a1 = str(ad)
                a2 = str(b[0])
                a3 = str(int(ad) * int(b[0]))
                text2.insert("end", '耐克篮球:' + a1 + t1 + a2 + t2 + a3 + '元\n')  # 必须统一数据类型
            if ad1 > 0:
                a1 = str(ad1)
                a2 = str(b[1])
                a3 = str(int(ad1) * int(b[1]))
                text2.insert("end", '李宁篮球:' + a1 + t1 + a2 + t2 + a3 + '元\n')  # 必须统一数据类型
            if ad2 > 0:
                a1 = str(ad2)
                a2 = str(b[2])
                a3 = str(int(ad2) * int(b[2]))
                text2.insert("end", '准者篮球:' + a1 + t1 + a2 + t2 + a3 + '元\n')  # 必须统一数据类型
            if ad3 > 0:
                a1 = str(ad3)
                a2 = str(b[3])
                a3 = str(int(ad3) * int(b[3]))
                text2.insert("end", '威尔胜篮球:' + a1 + t1 + a2 + t2 + a3 + '元\n')  # 必须统一数据类型
            if ad4 > 0:
                a1 = str(ad4)
                a2 = str(b[4])
                a3 = str(int(ad4) * int(b[4]))
                text2.insert("end", '斯伯丁篮球:' + a1 + t1 + a2 + t2 + a3 + '元\n')  # 必须统一数据类型
            if ad5 > 0:
                a1 = str(ad5)
                a2 = str(b[5])
                a3 = str(int(ad5) * int(b[5]))
                text2.insert("end", '安踏篮球:' + a1 + t1 + a2 + t2 + a3 + '元\n')  # 必须统一数据类型

        toto = str(ad + ad1 + ad2 + ad3 + ad4 + ad5)
        toto2 = str((ad * int(b[0])) + (ad1 * int(b[1])) + (ad2 * int(b[2])) + (ad3 * int(b[3])) + (ad4 * int(b[4])) + (
                    ad5 * int(b[5])))
        text2.insert("end", '总计:' + toto + '个商品,' + '总价：' + toto2 + '元' + '\n' + '\n')  # 必须统一数据类型

        ccct()
        lable = Label(text="购物商品如下：", fg='blue', font=('楷体', 16), )
        lable.place(x=0, y=0)

        def show():
            # 获取此账号的余额  然后减去总商品价格
            zyue = str(gold)
            toto3 = gold - int(toto2)
            syue = str(toto3)
            abc = tkinter.messagebox.showinfo("温馨提示", "您的当前余额为" + zyue + "\n您消费后的余额为：" + syue)

            print(gold)  # 给它弹出一下 余额
            toto3 = gold - int(toto2)  # 总价减去 随机余额
            print(toto3)  # 给他弹出一下 总结减去商品后剩余余额

            # 判断余额是否足够
            if toto3 >= 0:  # 余额够就跳转填写订单
                windows.destroy()
                order()
            # 余额不够就跳转充值页面
            else:
                abc = tkinter.messagebox.showwarning("温馨提示", "余额不足，跳转到充值界面！")
                windows.destroy()
                addmoney()

        def rt():
            windows.destroy()
            mall()

        pay = Button(frm3, text="确认付款", width=10, height=2, bg="#3ca3fb", fg="white", font=('楷体', 12), command=show)
        pay.place(x=160, y=300)
        pay = Button(frm3, text="返回商场", width=10, height=2, bg="#3ca3fb", fg="white", font=('楷体', 12), command=rt)
        pay.place(x=300, y=300)

        windows.mainloop()

    # 充值*********************************************************
    def addmoney():
        windowss = Tk()
        windowss.title("充值页面")
        windowss.geometry('560x400+660+300')
        frm4 = Frame(windowss)
        frm4.config(width=560, height=400, )
        frm4.place(x=0, y=0)
        photo = PhotoImage(file=r'银行\czhi_beijing.png')
        aaa = Label(frm4, text='', image=photo, ).place(x=0, y=0)  # 插入背景及规定起始位置
        lable = Label(text="请选择银行：", fg='red')
        lable.place(x=0, y=0)

        v = IntVar()
        v.set(1)

        Radiobutton(frm4, text="中国银行 ", variable=v, value=1).place(x=60, y=135)
        Radiobutton(frm4, text="农业银行 ", variable=v, value=2).place(x=190, y=135)
        Radiobutton(frm4, text="工商银行 ", variable=v, value=3).place(x=310, y=135)
        Radiobutton(frm4, text="中国建设银行 ", variable=v, value=4).place(x=420, y=135)

        a = Label(frm4, text='银行卡号：', font=('楷体', 14), ).place(x=150, y=190)
        p = Label(frm4, text='手机号：  ', font=('楷体', 14), ).place(x=150, y=225)
        m = Label(frm4, text='验证码：  ', font=('楷体', 14), ).place(x=150, y=260)

        ae = Entry(frm4, text='1', )
        ae.place(x=270, y=192)
        pe = Entry(frm4, text='2')
        pe.place(x=270, y=227)
        me = Entry(frm4, text='3')
        me.place(x=270, y=262)

        def mny():
            windowss.destroy()

            windows = Tk()
            windows.title("中国银行")
            windows.geometry('360x160+800+200')

            lable = Label(text="输入需要充值金额：", font=('黑体', 10), fg='red')
            lable.place(x=120, y=20)

            money = Entry(windows, text='1')
            money.place(x=120, y=50)

            print('余额：', gold)  # 这里弹窗提醒一下他余额有多少

            def show():
                global gold
                mn = money.get()
                gold = gold + int(mn)

                # 到这里 mn取得的输入的金额的数量 加上之前的随机给的
                ye = str(gold)
                abc = tkinter.messagebox.showinfo("温馨提示", "充值成功！您的当前余额为：" + ye)
                print("充值成功，您的余额为：", gold)  # 这里弹窗提醒
                windows.destroy()
                addmoney()
                # 回到购物车 继续支付

            pay = Button(windows, text="确定", width=10, height=1, font=('楷体', 14), command=show)
            pay.place(x=130, y=90)
            windows.mainloop()

        def y():
            global sjs
            sjs = random.randint(1000, 9999)
            ssjs = str(sjs)
            abc = tkinter.messagebox.showwarning("温馨提示", "验证码：" + ssjs)
            print('验证码：', ssjs)  # 弹出验证码

        yzm = Button(windowss, text="验证码", width=5, height=1, command=y)
        yzm.place(x=430, y=260)

        def show():
            py = int(me.get())  # 将验证码类型强制转换

            if sjs == py:  # 判断程序和输入验证码是否统一
                mny()
            else:
                abc = tkinter.messagebox.showwarning("温馨提示", "验证码输入错误 !")
                print("验证码输入错误")  # 这里弹窗提醒

        def CAT():
            windowss.destroy()
            cat()

        pay = Button(windowss, text="确定", width=8, height=1, font=('楷体', 14), command=show)
        pay.place(x=170, y=320)
        pay = Button(windowss, text="返回", width=8, height=1, font=('楷体', 14), command=CAT)
        pay.place(x=300, y=320)

        windowss.mainloop()

    # 订单页面**********************************************************
    def order():
        windows = Tk()
        windows.title("订单信息")
        windows.geometry('480x500+750+200')
        frm5 = Frame(windows, )
        frm5.config(bg='white', width=480, height=500, )
        frm5.place(x=0, y=0, )

        lable = Label(text="请输入您的收货订单：", fg='red', font=('楷体', 14), )
        lable.place(x=0, y=0)

        a = Label(frm5, text='收件人姓名：', font=('楷体', 14), ).place(x=90, y=50)
        p = Label(frm5, text='    手机号：', font=('楷体', 14), ).place(x=90, y=90)
        m = Label(frm5, text='      地址：', font=('楷体', 14), ).place(x=90, y=130)

        ae = Entry(frm5, text='1')
        ae.place(x=235, y=50)
        pe = Entry(frm5, text='2')
        pe.place(x=235, y=90)
        me = Entry(frm5, text='3')
        me.place(x=235, y=130)

        text2 = Text(frm5, width=30, height=10, font=('楷体', 14), )  # 用来放选项内容
        text2.place(x=90, y=180)
        t1 = '*'
        t2 = '='

        if ad > 0:
            a1 = str(ad)
            a2 = str(b[0])
            a3 = str(int(ad) * int(b[0]))
            text2.insert("end", '耐克篮球:' + a1 + t1 + a2 + t2 + a3 + '元\n')  # 必须统一数据类型
        if ad1 > 0:
            a1 = str(ad1)
            a2 = str(b[1])
            a3 = str(int(ad1) * int(b[1]))
            text2.insert("end", '李宁篮球:' + a1 + t1 + a2 + t2 + a3 + '元\n')  # 必须统一数据类型
        if ad2 > 0:
            a1 = str(ad2)
            a2 = str(b[2])
            a3 = str(int(ad2) * int(b[2]))
            text2.insert("end", '准者篮球:' + a1 + t1 + a2 + t2 + a3 + '元\n')  # 必须统一数据类型
        if ad3 > 0:
            a1 = str(ad3)
            a2 = str(b[3])
            a3 = str(int(ad3) * int(b[3]))
            text2.insert("end", '威尔胜篮球:' + a1 + t1 + a2 + t2 + a3 + '元\n')  # 必须统一数据类型
        if ad4 > 0:
            a1 = str(ad4)
            a2 = str(b[4])
            a3 = str(int(ad4) * int(b[4]))
            text2.insert("end", '斯伯丁篮球:' + a1 + t1 + a2 + t2 + a3 + '元\n')  # 必须统一数据类型
        if ad5 > 0:
            a1 = str(ad5)
            a2 = str(b[5])
            a3 = str(int(ad5) * int(b[5]))
            text2.insert("end", '安踏篮球:' + a1 + t1 + a2 + t2 + a3 + '元\n')  # 必须统一数据类型

        toto = str(ad + ad1 + ad2 + ad3 + ad4 + ad5)
        toto2 = str((ad * int(b[0])) + (ad1 * int(b[1])) + (ad2 * int(b[2])) + (ad3 * int(b[3])) + (ad4 * int(b[4])) + (
                    ad5 * int(b[5])))
        text2.insert("end", '\n' + '总计:' + toto + '个商品,' + '总价：' + toto2 + '元' + '\n')  # 必须统一数据类型

        def show():
            yue = str(gold)
            abc = tkinter.messagebox.showinfo("温馨提示", "交易完成，欢迎下次光临\n您的余额还有：" + yue + "   元")
            windows.destroy()
            print("交易完成，欢迎下次光临")  # 这里弹窗提醒

        def rt():
            windows.destroy()
            cat()

        pay = Button(frm5, text="确定", bg="#3ca3fb", fg="white", width=10, height=1, font=('楷体', 14), command=show)
        pay.place(x=120, y=405)

        fanhui = Button(frm5, text="返回", bg="#3ca3fb", fg="white", width=10, height=1, font=('楷体', 14), command=rt)
        fanhui.place(x=270, y=405)

        windows.mainloop()

    # -------------------------客服人员---------------------------------
    def all():
        window.destroy()
        windows1 = Tk()
        windows1.geometry('600x500')
        windows1.title('客服信息')

        lable = Label(text="Python首发阵容", font=(180), fg="red")
        lable.place(x=240, y=12)

        lable = Label(text="1号首发：192407101 陈炯杨", font=(20))
        lable.place(x=200, y=40)
        lable = Label(text="2号首发：192407153 杨军洪", font=(20))
        lable.place(x=200, y=65)
        lable = Label(text="3号首发：192407152 杨杰", font=(20))
        lable.place(x=200, y=90)
        lable = Label(text="4号首发：192407138 宋阳进", font=(20))
        lable.place(x=200, y=115)
        lable = Label(text="5号首发：192407117 李达旺", font=(20))
        lable.place(x=200, y=140)

        canvas1 = Canvas(windows1, bg='yellow', height=338, width=600)
        image_file1 = PhotoImage(file=r'666.png')

        canvas1.create_image(0, 0, anchor='nw', image=image_file1)
        canvas1.pack()
        canvas1.place(x=0, y=167)

        def close():
            windows1.destroy()
            mall()

        Button(text="关闭", width=8, height=2, command=close).place(x=250, y=470)
        windows1.mainloop()

    # 创建四个复选框  按钮
    plus = Button(frm2, text="加入购物车", width=10, font=('黑体', 8), bg="red", fg="white", height=1, command=add, ).place(
        x=115, y=245)
    plus1 = Button(frm2, text="加入购物车", width=10, font=('黑体', 8), bg="red", fg="white", height=1, command=add1).place(
        x=272, y=245)
    plus2 = Button(frm2, text="加入购物车", width=10, font=('黑体', 8), bg="red", fg="white", height=1, command=add2).place(
        x=425, y=245)
    plus3 = Button(frm2, text="加入购物车", width=10, font=('黑体', 8), bg="red", fg="white", height=1, command=add3).place(
        x=115, y=447)
    plus4 = Button(frm2, text="加入购物车", width=10, font=('黑体', 8), bg="red", fg="white", height=1, command=add4).place(
        x=272, y=447)
    plus5 = Button(frm2, text="加入购物车", width=10, font=('黑体', 8), bg="red", fg="white", height=1, command=add5).place(
        x=425, y=447)

    var1 = IntVar()  # 创建IntVar型数据对象  勾选框
    Checkbutton(frm2, text=a[0], variable=var1, bg="white", command=callCheckbutton).place(x=70, y=200)
    var2 = IntVar()
    Checkbutton(frm2, text=a[1], variable=var2, bg="white", command=callCheckbutton).place(x=225, y=200)
    var3 = IntVar()
    Checkbutton(frm2, text=a[2], variable=var3, bg="white", command=callCheckbutton).place(x=380, y=200)
    var4 = IntVar()
    Checkbutton(frm2, text=a[3], variable=var4, bg="white", command=callCheckbutton).place(x=70, y=400)
    var5 = IntVar()
    Checkbutton(frm2, text=a[4], variable=var5, bg="white", command=callCheckbutton).place(x=225, y=400)
    var6 = IntVar()
    Checkbutton(frm2, text=a[5], variable=var6, bg="white", command=callCheckbutton).place(x=380, y=400)

    def deCat():
        window.destroy()
        cat()

    def yue():
        money = str(gold)
        Act = str(1)
        tkinter.messagebox.showinfo("尊敬的" + Act + "用户", "您的余额为：" + money)

    Button(frm2, text="查看购物车", width=10, height=2, command=deCat).place(x=560, y=330)
    Button(frm2, text="查看余额", width=10, height=2, command=yue).place(x=670, y=330)
    Button(frm2, text="联系客服", width=10, height=2, command=all).place(x=560, y=400)
    Button(frm2, text="退出商场", width=10, height=2, command=window.destroy).place(x=670, y=400)
    # Button(window, text="取消选购", width=8,height=2).place(x=100,y=330)

    # 创建一个文本框
    text = Text(window, width=30, height=13)  # 用来放所选的商品内容
    text.place(x=550, y=125)

    window.mainloop()
#mall()#购物商场**********************************************************

#登录系统*******************************************************
# ----------------------------------------------------------------------
data = xlrd.open_workbook("1.xls")
table = data.sheet_by_name("个人信息")

a = table.col_values(0)  #从电脑里边读入本来已经存储有的账号
b = table.col_values(1)  #密码
end=0 #记录最后一行的

for i in a:
    a[end] = int(a[end])  # 强制类型转换
    if b[end]!=str(b[end]): #跳过字符串的  否则全是数字时会有小数点
        b[end] = str(int(b[end]))  # 强制类型转换 去掉小数点
    end=end+1

date = dict(zip(a, b))  # 压缩成字典 # 建立字典date  键为账号 值为密码 压缩成字典后键值自动转换为str了

ZH = end
MM = end
#print(date)  #*********************


dele=0 #用来动态保存表单最后账号处于的位置
bt=[]#用来动态保存表单的账号情况
at=[]#用来动态保存表单的密码情况

def open():

    global dele
    global bt
    global at
    global ZH
    global MM

    data = xlrd.open_workbook("1.xls")
    table = data.sheet_by_name("个人信息")

    a = table.col_values(0)  # 从电脑里边读入本来已经存储有的账号
    b = table.col_values(1)  # 密码
    end = 0  # 记录最后一行的
    for i in a:
        a[end] = int(a[end])  # 强制类型转换
        if b[end] != str(b[end]):
            b[end] = str(int(b[end]))  # 强制类型转换
        end = end + 1

    date = dict(zip(a, b))  # 压缩成字典 # 建立字典date  键为账号 值为密码 压缩成字典后键值自动转换为str了
    ZH = end
    MM = end

    dele=end#更新表单最后的处于的位置
    bt=b#更新表单的账号数据
    at=a#更新表单的密码数据

#--------------------------------------------------------
#查看账号
def pt():

   open()
   a = at

   main_windows = Tk()
   main_windows.geometry("450x320+740+350")
   main_windows.title("账号情况")
   theLB = Listbox(main_windows)# 创建一个空列表
   theLB.pack()
   # 往列表里添加数据
   result=0
   for i in a:
      t=str(a[result])
      y=str(result+1)
      theLB.insert("end","账号"+y+":   "+t) #`listbox.delete(0, "end")删除的方法
      result=result+1

   def show():
       main_windows.destroy()
       chose()

   qut = Button(main_windows, text="返回",bg="#1bb7ea",fg="white", width=10, command=show).pack()
   main_windows.mainloop()

#-------------------------------------------------------------------------------
#删除
def dlt():

    open()
    a=at
    end=dele
    b=bt

    j = 0  # 记录最后一行的
    for i in a:
        b[j] = int(b[j])  # 强制类型转换
        j = j + 1

    main_windows = Tk()
    main_windows.geometry("450x320+740+350")
    frm1 = Frame(main_windows, )
    frm1.config(bg='yellow', width=450, height=320, )
    frm1.place(x=0, y=0, )
    main_windows.title('注销账号')
    photo = PhotoImage(file=r'3.gif')
    aaa = Label(frm1, text='', image=photo, ).place(x=0, y=0)  # 插入背景及规定起始位置
    #先输入需要删除的账号 然后点击删除就删除了

    account = Label(frm1, text='账号：',
                    justify=LEFT,  # 左对齐
                    compound=CENTER,  # 设置文本和图像的混合模式a
                    font=('楷体', 14),
                    fg='black'  # 前景颜色
                    )
    account.place(x=110,y=100) # 1: 上下位置   2:左右位置  3：上下大小  4 左右大小
    account_Entry = Entry(frm1, text='1', )
    account_Entry.place(x=200,y=103)

    def show():
        global ZH
        global MM

        act = account_Entry.get()  # 从输入框获取数据到act中
        Acount = int(act)  # 获取到输入框的账号的值  转换为int类型

        if Acount in date.keys():

            rb = xlrd.open_workbook("1.xls", formatting_info=True)
            rs = rb.sheet_by_index(0)  # 匹配第一个表单
            wb = copy(rb)  # 拷贝原表单的东西
            ws = wb.get_sheet("个人信息")  # 获取要追加信息的表单
            #遍历账号的一整列 找到相应账号那一列 a是之前就已经提取在列表里边的
            rsult=0

            for i in a: #表单从零开始
                if a[rsult]==Acount:#已经遍历到要删除的账号 这两个都是int类型的
                    j=rsult
                    #end账号的最大长度
                    while j<end:#从当前需要删除的账号行开始循环
                            if j!=rsult: #第一个不要覆盖
                                head = a[j] #获取到表格里边的账号
                                tail = b[j] #获取到表格里边的密码

                                ws.write(j-1, 0, head)  # 写入数据 账号
                                ws.write(j-1, 1, tail)  # 写入数据 密码
                            j=j+1
                    break
                rsult=rsult+1
            ws.write(end-1, 0, None)  # 把最后一个赋值为空
            ws.write(end-1, 1, None)
            wb.save("1.xls")  # 保存
            dt=str(Acount)
            del date[Acount]  # 删除键是'Acount'的条目 把字典里边的键和值也删除了
            abc = tkinter.messagebox.showinfo("删除成功","删除的账号为： "+dt)
            ZH=ZH-1
            MM=MM-1
            main_windows.destroy()
            w()
        else:
            abc = tkinter.messagebox.showwarning("温馨提示", "此账号未被注册！")
            main_windows.destroy()
            dlt()
    def fanhui():
        open()
        main_windows.destroy()
        chose()
    ini = Button(main_windows, text="删除", width=10, command=show).place(x=120,y=170)
    qut = Button(main_windows, text="返回", width=10, command=fanhui).place(x=240,y=170)

    main_windows.mainloop()

#---------------------------------------------------------------------------
#修改密码
def c(): #建立函数块  这样在别的文件引用时就不会马上就弹出了，就可以等点击的时候再弹出

    open()
    a=at

    main_windows = Tk()
    main_windows.title("修改密码")
    main_windows.geometry("450x320+740+350")
    frm1 = Frame(main_windows,)
    frm1.config(bg='yellow', width=450, height=320, )
    frm1.place(x=0, y=0, )
    photo = PhotoImage(file=r'3.gif')
    aaa = Label(frm1, text='', image=photo, ).place(x=0, y=0)  # 插入背景及规定起始位置
    top = Label(frm1, text='账号为数字0-9，密码为字母或数字',bg="white",).place(x=250,y=5)
    account = Label(frm1, text='账号：',
                    justify=LEFT,  # 左对齐
                    compound=CENTER,  # 设置文本和图像的混合模式a
                    font=('楷体', 12),
                    fg='black'  # 前景颜色
                    )
    lack = Label(frm1, text='新密码：',
                 justify=LEFT,  # 左对齐
                 compound=CENTER,  # 设置文本和图像的混合模式
                 font=('楷体', 12),  # 注意字体和字号用元组的形式
                 fg='black'  # 前景颜色
                 )
    double_lack = Label(frm1, text='确认新密码：',
                        justify=LEFT,  # 左对齐
                        compound=CENTER,  # 设置文本和图像的混合模式
                        font=('楷体', 12), # 注意字体和字号用元组的形式
                        fg='black'  # 前景颜色
                        )
    account.place(x=90, y=80)  # x：水平距离 ； y：垂直距离
    lack.place(x=90, y=135)
    double_lack.place(x=90, y=185)

    account_Entry = Entry(frm1, text='1', )
    lack_Entry = Entry(frm1, show='*')
    double_lack = Entry(frm1, show="*")
    #以下是规定输入框所在的位置
    account_Entry.place(x=210, y=80)
    lack_Entry.place(x=210, y=135)
    double_lack.place(x=210, y=185)

    List=a#保存a账号数组
    def show():
        act = account_Entry.get()  # 从输入框获取数据到act中
        lak = lack_Entry.get()
        dlc = double_lack.get() #以这个密码为准

        value = re.compile(r'^[0-9]+$')  # 必须是数字 ^表示以这个字符开头0到9数字开头 同理[0-9]表示0到9的一个数字，+表示1个或多个，也就是整数部分 $ 表示结尾
        result = value.match(act)
        value2 = re.compile('^[a-zA-Z0-9]+$')# 必须是字母加数字
        result2=value2.match(lak)

        if bool(result) == False or bool(result2) == False: #检查账号格式不能错误
            a = tkinter.messagebox.showinfo("警告","账号必须为数字，\n 密码不能是特殊字母")
            main_windows.destroy()
            c()  # 登录
        else:
            Acount = int(act)  # 获取到输入框的账号的值  转换为int类型
            if dlc!=lak:#判断两次输入的密码是否一致
                abc = tkinter.messagebox.showwarning("温馨提示", "您所输入的两次密码不一致！")
                main_windows.destroy()
                c()
            elif Acount not in date.keys():
                abc = tkinter.messagebox.showwarning("温馨提示","此账号未被注册！")
                main_windows.destroy()
                c()
            else:#正确时
                date[Acount] = lak  # 账号和密码保存在字典中
                rb = xlrd.open_workbook("1.xls", formatting_info=True)
                rs = rb.sheet_by_index(0)  # 匹配第一个表单
                wb = copy(rb)  # 拷贝原表单的东西
                ws = wb.get_sheet("个人信息")  # 获取要追加信息的表单

                #遍历账号的一整列 找到相应账号那一列 a是之前就已经提取在列表里边的
                rsult=0
                for i in List: #表单从零开始
                    if List[rsult]==Acount:
                        break
                    rsult=rsult+1

                ws.write(rsult, 1, dlc)  # 写入数据 密码
                wb.save("1.xls")  # 保存
                abc = tkinter.messagebox.showwarning("温馨提示", "修改成功！\n" + "您的新密码：" + dlc)

                main_windows.destroy()
                w()

    def fanhui():
        main_windows.destroy()
        chose()
    ini = Button(frm1, text="确定", width=10, bg="#6bba25",fg="white",  command=show).place(x=120, y= 245)
    qut = Button(frm1, text="返回", width=10, bg="#6bba25",fg="white",  command=fanhui).place(x=240, y= 245)

    main_windows.mainloop()

# ----------------------------------------------------------------------
# 注册界面
def e():  # 建立函数块  这样在别的文件引用时就不会马上就弹出了，就可以等点击的时候再弹出
    main_windows = Tk()
    main_windows.title("注册")
    main_windows.geometry("450x320+740+350")
    frm1 = Frame(main_windows)
    frm1.config(bg='orange', width=450, height=320, )
    frm1.place(x=0, y=0)  #规定框架的起始位置

    photo = PhotoImage(file=r'3.gif')
    aaa = Label(frm1, text='', image=photo, ).place(x=0, y=0)  #插入背景及规定起始位置

    top = Label(frm1, text='账号为数字0-9，密码字母或者数字', bg="white").place(x=250,y=5)

    account = Label(frm1, text='账号：',
                    justify=LEFT,  # 左对齐
                    compound=CENTER,  # 设置文本和图像的混合模式
                    font=('楷体', 12),
                    fg='black'  # 前景颜色
                    )
    lack = Label(frm1, text='密码：',
                 justify=LEFT,  # 左对齐
                 compound=CENTER,  # 设置文本和图像的混合模式
                 font=('楷体', 12),  # 注意字体和字号用元组的形式
                 fg='black'  # 前景颜色
                 )

    double_lack = Label(frm1, text='确认密码：',
                        justify=LEFT,  # 左对齐
                        compound=CENTER,  # 设置文本和图像的混合模式
                        font=('楷体', 12),  # 注意字体和字号用元组的形式
                        fg='black'  # 前景颜色
                        )

    account.place(x=90,y=80)  # x：水平距离 ； y：垂直距离
    lack.place(x=90,y=135)
    double_lack.place(x=90,y=185)

    account_Entry = Entry(frm1, text='1', )
    lack_Entry = Entry(frm1, show='*')
    double_lack = Entry(frm1, show="*")

    account_Entry.place(x=210, y=80 )
    lack_Entry.place(x=210, y=135 )
    double_lack.place(x=210, y= 185)

    def show():

        global ZH  # 将外边的变量声明为全局变量
        global MM
        act = account_Entry.get()  # 从输入框获取数据到act中
        lak = lack_Entry.get()
        dlc = double_lack.get()

        value = re.compile(r'^[0-9]+$')  # 必须是数字 ^表示以这个字符开头0到9数字开头 同理[0-9]表示0到9的一个数字，+表示1个或多个，也就是整数部分 $ 表示结尾
        result = value.match(act)

        value2 = re.compile('^[a-zA-Z0-9]+$')  # 必须是字母加数字
        result2 = value2.match(lak)

        if bool(result) == False or bool(result2) == False: #检查账号格式不能错误
            a = tkinter.messagebox.showwarning("警告","账号必须为数字，\n 密码不能是特殊字母")
            main_windows.destroy()
            e()  # 登录

        else :
            Acount = int(act)  # 获取到输入框的账号的值  转换为int类型
            if  Acount in date.keys():  # 判断账号格式是否正确 #判断账号未被注册
                a = tkinter.messagebox.showwarning("温馨提示", "此账号已注册！")
                main_windows.destroy()
                e()
            elif dlc != lak:  # 判断两次输入的密码是否一致
                a = tkinter.messagebox.showwarning("温馨提示", "您所输入的密码不相同！\n请重新注册！")
                main_windows.destroy()
                e()
            else:  # 正确开始信息存储
                date[Acount] = lak  # 账号和密码保存在字典中
                # 追加
                rb = xlrd.open_workbook("1.xls", formatting_info=True)
                rs = rb.sheet_by_index(0)  # 匹配第一个表单
                wb = copy(rb)  # 拷贝原表单的东西
                ws = wb.get_sheet("个人信息")  # 获取要追加信息的表单

                ws.write(ZH, 0, Acount)  # 写入数据 账号
                ws.write(MM, 1, lak)  # 写入数据 密码
                wb.save("1.xls")  # 保存

                ZH = ZH + 1
                MM = MM + 1

                a = tkinter.messagebox.showwarning("温馨提示", "注册成功！！！\n" + "账号：" + act + "    " +"密码：" + lak)
                main_windows.destroy()  # 销毁此窗口
                w()  #登录

    ini = Button(main_windows, text="注册", width=10, bg="#6bba25",fg="white", command=show).place(x=120, y= 245)
    qut = Button(main_windows, text="退出", width=10, bg="#6bba25",fg="white", command=main_windows.destroy).place(x=240, y= 245)

    main_windows.mainloop()

#---------------------------------------------------------------------
#登录后选择窗口
def chose():

    def one(): #先销毁本窗口 再显示窗口
        main_windows.destroy()
        mall()
    def two(): #先销毁本窗口 再显示窗口
        main_windows.destroy()
        c()
    def three(): #先销毁本窗口 再显示窗口
        main_windows.destroy()
        dlt()
    def four(): #先销毁本窗口 再显示窗口
        main_windows.destroy()
        pt()
    def five(): #先销毁本窗口 再显示窗口
        main_windows.destroy()
        w()
    main_windows = Tk()
    main_windows.geometry("450x320+740+350")
    main_windows.title('欢迎来到 MiniQQ 登陆界面')
    v = tk.IntVar()
    v.set(2)

    tk.Button(main_windows,bg="red", fg="white",text='进入购物商场',compound=CENTER,font=('楷体', 12), anchor='c',width=21,height=2,command=one).pack()
    tk.Button(main_windows, bg="orange", fg="white", text='修改密码', font=('楷体', 12), anchor='c', width=21,height=2,command=two).pack()
    tk.Button(main_windows,bg="blue", fg="white", text='注销账号', font=('楷体', 12), anchor='c', width=21,height=2,command=three).pack()
    tk.Button(main_windows,bg="indigo", fg="white", text='查看账号', font=('楷体', 12), anchor='c', width=21,height=2,command=four).pack()
    tk.Button(main_windows,bg="purple", fg="white", text='退出登录', font=('楷体', 12), anchor='c', width=21,height=2, command=five).pack()

    main_windows.mainloop()

#----------------------------------------------------------------------------
# 登录界面
def w():
    main_windows = Tk()
    main_windows.title("登录")
    main_windows.geometry("450x320+740+350")
    frm1 = Frame(main_windows,)  #创建一个框架
    frm1.config(bg='yellow', width=450, height=320, )  #规定框架大小
    frm1.place(x=0,y=0,)  #规定框架的起始位置

    photo = PhotoImage(file=r'2.gif')
    aaa = Label(frm1, text='',image=photo,).place(x=0,y=0)

    account = Label(frm1, text='账号：',
                    justify=LEFT,  # 左对齐
                    compound=CENTER,  # 设置文本和图像的混合模式
                    font=('楷体', 14),
                    bg="white",
                    fg='black'  # 前景颜色
                    ).place(x=100,y=130)
    lack = Label(frm1, text='密码：',
                 justify=LEFT,  # 左对齐
                 compound=CENTER,  # 设置文本和图像的混合模式
                 font=('楷体', 14),  # 注意字体和字号用元组的形式
                 fg='black'  # 前景颜色
                 ).place(x=100,y=185)

    account_Entry = Entry(frm1, text='1')
    account_Entry.place(x=200, y=130)
    lack_Entry = Entry(frm1, show='*')
    lack_Entry.place(x=200, y=185)

    def show():
        Acount=0
        act = account_Entry.get()  # 从输入框获取数据到act中  账号
        lak = lack_Entry.get()  # 密码

        value = re.compile(r'^[0-9]+$')  # 必须是数字 ^表示以这个字符开头0到9数字开头 同理[0-9]表示0到9的一个数字，+表示1个或多个，也就是整数部分 $ 表示结尾
        result = value.match(act)

        value2 = re.compile('^[a-zA-Z0-9]+$')  # 必须是字母加数字
        result2 = value2.match(lak)

        if bool(result) == False or bool(result2) == False: #检查账号格式不能错误
            a = tkinter.messagebox.showwarning("警告","账号必须为数字，\n 密码不能是特殊字母")
            main_windows.destroy()
            w()  # 登录
        else:
            Acount = int(act)  # 获取到输入框的账号的值  转换为int类型
            # 这里要判断输入的与字典里面的是否一致
            if Acount in date.keys() and lak == date.get(Acount):
                a = tkinter.messagebox.showinfo("温馨提示", "登录成功！！！\n" +"账号：" + act + "   " +"密码：" + lak )
                main_windows.destroy()  # 销毁此窗口
                chose()  #菜单页面
            elif Acount not in date.keys():
                a = tkinter.messagebox.showwarning("温馨提示", "此账号不存在！\n" + "即将为您跳转到 <注册界面>")
                main_windows.destroy()  # 销毁此窗口
                e()  # 注册
            elif lak != date.get(Acount):
                a = tkinter.messagebox.showwarning("温馨提示", "您的密码错误！\n" )
                main_windows.destroy()  # 销毁此窗口
                w()  # 登录

    ini = Button(frm1, text="登录", bg="#1bb7ea",fg="white", width=10, command=show).place(x=120,y=250)
    qut = Button(frm1, text="退出", bg="#1bb7ea",fg="white", width=10, command=main_windows.destroy).place(x=240,y=250)
    main_windows.mainloop()
w()  #登录

