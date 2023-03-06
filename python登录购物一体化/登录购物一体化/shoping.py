#商场界面
import xlrd
from tkinter import *
import random
import tkinter.messagebox

#用来记录 有没有勾选商品的
ad = 0
ad1 = 0
ad2 = 0
ad3 = 0
ad4 = 0
ad5 = 0

sjs = 0#验证码
gold = random.randint(100, 1000)  # 初始化给用户一个金额******************************

def mall():#商场********************************************************
    #窗口变量
    window = Tk()
    #窗口标题
    window.title('商品信息')
    #窗口大小
    window.geometry('800x500+600+250')
    #画布大小设置
    frm2 = Frame(window)
    frm2.config(bg='orange', width=800, height=500, )
    frm2.place(x=0, y=0)  # 规定框架的起始位置
    photo = PhotoImage(file=r'球\bj1.png')
    aaa = Label(frm2, text='', image=photo, ).place(x=0, y=0)  # 插入背景及规定起始位置

    data=xlrd.open_workbook("1.xls")
    table = data.sheet_by_name("商品信息")

    a=table.col_values(0)#提取商品信息
    b=table.col_values(1)

    end=0 #记录最后一行的

    for i in a:
        b[end] = str(int(b[end]))  # 强制类型转换
        end=end+1

    date=dict(zip(a,b))#压缩成字典 # 建立字典date
    print(date)

    # #加载图片
    # image_file = PhotoImage(file=r'球\1.png')
    # image_file1 = PhotoImage(file=r'球\2.png')
    # image_file2 = PhotoImage(file=r'球\3.png')
    # image_file3 = PhotoImage(file=r'球\4.png')
    # image_file4 = PhotoImage(file=r'球\5.png')
    # image_file5 = PhotoImage(file=r'球\6.png')

    #价格的位置
    tiaol1 = Text(frm2, width=7, height=1,bg="white" ,fg="black")  # 用来放选项内容 存放商品数量
    tiaol1.place(x=75, y=182)  # 存放商品数量位置 小窗口
    tiaol1.insert('insert', '$.'+b[0]+'元' )  # INSERT表示在光标位置插入msg所指代的文本

    tiaol2 = Text(frm2, width=7, height=1,bg="white" ,fg="black")  # 用来放选项内容 存放商品数量
    tiaol2.place(x=230, y=182)  # 存放商品数量位置 小窗口
    tiaol2.insert('insert', '$.'+b[1]+'元')    # INSERT表示在光标位置插入msg所指代的文本

    tiaol3 = Text(frm2, width=7, height=1,bg="white" ,fg="black")  # 用来放选项内容 存放商品数量
    tiaol3.place(x=385, y=182)  # 存放商品数量位置 小窗口
    tiaol3.insert('insert', '$.'+b[2]+'元')  # INSERT表示在光标位置插入msg所指代的文本

    tiaol4 = Text(frm2, width=7, height=1,bg="white" ,fg="black")  # 用来放选项内容 存放商品数量
    tiaol4.place(x=75, y=380)  # 存放商品数量位置 小窗口
    tiaol4.insert('insert', '$.'+b[3]+'元')  # INSERT表示在光标位置插入msg所指代的文本

    tiaol5 = Text(frm2, width=7, height=1,bg="white" ,fg="black")  # 用来放选项内容 存放商品数量
    tiaol5.place(x=230, y=380)  # 存放商品数量位置 小窗口
    tiaol5.insert('insert', '$.'+b[4]+'元')  # INSERT表示在光标位置插入msg所指代的文本

    tiaol6 = Text(frm2, width=7, height=1,bg="white" ,fg="black")  # 用来放选项内容 存放商品数量
    tiaol6.place(x=385, y=380)  # 存放商品数量位置 小窗口
    tiaol6.insert('insert', '$.'+b[5]+'元')  # INSERT表示在光标位置插入msg所指代的文本

    # 添加标签
    Label(frm2,text='请选择购买（可多选）',fg='blue').place(x=403,y=477)
    Label(frm2, text='选购商品如下所示：', fg='blue',font=('楷体', 14),).place(x=550, y=100)

    # 定义复选框的事件处理函数
    def callCheckbutton():
        msg = ''
        if var1.get() == 1:     #因为var1是IntVar型变量，选中为1，不选为0  如果它没有被选中  那么加再多也不给它
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
        text.delete(0.0,END)
        text.insert('insert',msg)  #INSERT表示在光标位置插入msg所指代的文本


#以下是用来放入已经勾选商品的文本框的  多选累计
    def add(cho):
        global ad
        tiaol = Text(window, width=3, height=1)  # 用来放选项内容 存放商品数量
        tiaol.place(x=68,y=246) #存放商品数量位置 小窗口
        if var1.get() == 1:  # 因为var1是IntVar型变量，选中为1，不选为0  如果它没有被选中  那么加再多也不给它

            if cho==1:#加购还减购
                ad=ad+1
                tiaol.insert('insert', ad)  # INSERT表示在光标位置插入msg所指代的文本
            elif cho==0:
                ad = ad - 1
                tiaol.insert('insert', ad)  # INSERT表示在光标位置插入msg所指代的文本

        elif var1.get() == 0:
            tiaol.delete(0.0, END)
            tiaol.insert('insert', 0)  # INSERT表示在光标位置插入msg所指代的文本  # 没有勾选时清空文本框
            ad=0
        #print(ad)
    def add1(cho):
        global ad1
        tiaol = Text(window, width=3, height=1)  # 用来放选项内容
        tiaol.place(x=225,y=246)
        if var2.get() == 1:

            if cho==1:#加购还减购
                ad1=ad1+1
                tiaol.insert('insert', ad1)  # INSERT表示在光标位置插入msg所指代的文本
            elif cho==0:
                ad1 = ad1 - 1
                tiaol.insert('insert', ad1)  # INSERT表示在光标位置插入msg所指代的文本
        elif var1.get() == 0:
            tiaol.delete(0.0, END)
            tiaol.insert('insert', 0)  # INSERT表示在光标位置插入msg所指代的文本  # 没有勾选时清空文本框
            ad1 = 0
        #print(ad1)
    def add2(cho):
        global ad2
        tiaol = Text(window, width=3, height=1)  # 用来放选项内容
        tiaol.place(x=380,y=246)
        if var3.get() == 1:
            if cho==1:#加购还减购

                ad2=ad2+1
                tiaol.insert('insert', ad2)  # INSERT表示在光标位置插入msg所指代的文本
            elif cho==0:
                ad2 = ad2 - 1
                tiaol.insert('insert', ad2)  # INSERT表示在光标位置插入msg所指代的文本

        elif var1.get() == 0:
            tiaol.delete(0.0, END)
            tiaol.insert('insert', 0)   # 没有勾选时清空文本框
            ad2 = 0
        #print(ad2)
    def add3(cho):
        global ad3
        tiaol = Text(window, width=3, height=1)  # 用来放选项内容
        tiaol.place(x=68,y=447)
        if var4.get() == 1:

            if cho==1:#加购还减购
                ad3=ad3+1
                tiaol.insert('insert', ad3)  # INSERT表示在光标位置插入msg所指代的文本
            elif cho==0:
                ad3 = ad3 - 1
                tiaol.insert('insert', ad3)  # INSERT表示在光标位置插入msg所指代的文本

        elif var1.get() == 0:
            tiaol.delete(0.0, END)
            tiaol.insert('insert', 0)   # 没有勾选时清空文本框
            ad3 = 0
        #print(ad3)
    def add4(cho):
        global ad4
        tiaol = Text(window, width=3, height=1)  # 用来放选项内容
        tiaol.place(x=225,y=447)
        if var5.get() == 1:

            if cho==1:#加购还减购
                ad4=ad4+1
                tiaol.insert('insert', ad4)  # INSERT表示在光标位置插入msg所指代的文本
            elif cho==0:
                ad4 = ad4 - 1
                tiaol.insert('insert', ad4)  # INSERT表示在光标位置插入msg所指代的文本

        elif var1.get() == 0:
            tiaol.delete(0.0, END)
            tiaol.insert('insert', 0)   # 没有勾选时清空文本框
            ad4 = 0
        #print(ad4)
    def add5(cho):
        global ad5
        tiaol = Text(window, width=3, height=1)  # 用来放选项内容
        tiaol.place(x=380,y=447)

        if var6.get() == 1:
            if cho==1:#加购还减购
                ad5=ad5+1
                tiaol.insert('insert', ad5)  # INSERT表示在光标位置插入msg所指代的文本
            elif cho==0:
                ad5 = ad5 - 1
                tiaol.insert('insert', ad5)  # INSERT表示在光标位置插入msg所指代的文本

        elif var1.get() == 0:
            tiaol.delete(0.0, END)
            tiaol.insert('insert', 0)   # 没有勾选时清空文本框
            ad5 = 0

        #print(ad5)

#   购物车********************************************************
    def cat():

        windows=Tk()
        windows.title("购物车")
        windows.geometry('560x400+660+300')
        frm3 = Frame(windows)

        frm3.config( width=560, height=400, )
        frm3.place(x=0, y=0)
        photo = PhotoImage(file=r'车\gwc_beijing.png')
        aaa = Label(frm3, text='', image=photo, ).place(x=0, y=0)  # 插入背景及规定起始位置

        text2 = Text(frm3, width=40, height=12,font=('楷体', 12),)  # 用来放选项内容的文本框
        text2.place(x=115, y=80)
        t1='*'
        t2='='

        def ccct():
            if ad > 0:
                a1=str(ad)
                a2=str(b[0])
                a3=str(int(ad)*int(b[0]))
                text2.insert("end",'耐克篮球:'+a1+t1+a2+t2+a3+'元\n')#必须统一数据类型
            if ad1 > 0:
                a1=str(ad1)
                a2=str(b[1])
                a3=str(int(ad1)*int(b[1]))
                text2.insert("end",'李宁篮球:'+a1+t1+a2+t2+a3+'元\n')#必须统一数据类型
            if ad2 > 0:
                a1=str(ad2)
                a2=str(b[2])
                a3=str(int(ad2)*int(b[2]))
                text2.insert("end",'准者篮球:'+a1+t1+a2+t2+a3+'元\n')#必须统一数据类型
            if ad3 > 0:
                a1=str(ad3)
                a2=str(b[3])
                a3=str(int(ad3)*int(b[3]))
                text2.insert("end",'威尔胜篮球:'+a1+t1+a2+t2+a3+'元\n')#必须统一数据类型
            if ad4 > 0:
                a1=str(ad4)
                a2=str(b[4])
                a3=str(int(ad4)*int(b[4]))
                text2.insert("end",'斯伯丁篮球:'+a1+t1+a2+t2+a3+'元\n')#必须统一数据类型
            if ad5 > 0:
                a1=str(ad5)
                a2=str(b[5])
                a3=str(int(ad5)*int(b[5]))
                text2.insert("end",'安踏篮球:'+a1+t1+a2+t2+a3+'元\n')#必须统一数据类型

        toto=str(ad+ad1+ad2+ad3+ad4+ad5)
        toto2=str((ad*int(b[0]))+(ad1*int(b[1]))+(ad2*int(b[2]))+(ad3*int(b[3]))+(ad4*int(b[4]))+(ad5*int(b[5])))
        text2.insert("end", '总计:'+toto+'个商品,'+'总价：'+toto2+'元'+'\n'+'\n')  # 必须统一数据类型

        ccct()
        lable = Label(text="购物商品如下：", fg='blue',font=('楷体', 16),)
        lable.place(x=0, y=0)


        def show():
            #获取此账号的余额  然后减去总商品价格
            zyue = str(gold)
            toto3 = gold - int(toto2)
            syue = str(toto3)
            abc = tkinter.messagebox.showinfo("温馨提示", "您的当前余额为" + zyue + "\n您消费后的余额为：" + syue)

            print(gold) #给它弹出一下 余额
            toto3=gold-int(toto2) #总价减去 随机余额
            print(toto3)#给他弹出一下 总结减去商品后剩余余额

            #判断余额是否足够
            if toto3>=0: #余额够就跳转填写订单
                windows.destroy()
                order()
            #余额不够就跳转充值页面
            else:
                abc = tkinter.messagebox.showwarning("温馨提示", "余额不足，跳转到充值界面！")
                windows.destroy()
                addmoney()

        def rt():
            windows.destroy()
            mall()

        pay=Button(frm3,text="确认付款",width=10,height=2,bg="#3ca3fb",fg="white",font=('楷体', 12),command=show)
        pay.place(x=160,y=300)
        pay=Button(frm3,text="返回商场",width=10,height=2,bg="#3ca3fb",fg="white",font=('楷体', 12),command=rt)
        pay.place(x=300,y=300)

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

        a = Label(frm4, text='银行卡号：',font=('楷体', 14), ).place(x=150, y=190)
        p = Label(frm4, text='手机号：  ',font=('楷体', 14),).place(x=150, y=225)
        m = Label(frm4, text='验证码：  ',font=('楷体', 14),).place(x=150, y=260)

        ae = Entry(frm4, text='1',)
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
                print("充值成功，您的余额为：", gold) # 这里弹窗提醒
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
                print("验证码输入错误") # 这里弹窗提醒

        def CAT():
            windowss.destroy()
            cat()
        pay = Button(windowss, text="确定", width=8, height=1,font=('楷体', 14),  command=show)
        pay.place(x=170, y=320)
        pay = Button(windowss, text="返回", width=8, height=1,font=('楷体', 14), command=CAT)
        pay.place(x=300, y=320)

        windowss.mainloop()


    # 订单页面**********************************************************
    def order():
        sf=random.randint(100000000000000,999999999999999)
        windows = Tk()
        windows.title("订单信息")
        windows.geometry('480x500+750+200')
        frm5 = Frame(windows, )
        frm5.config(bg='white', width=480, height=500, )
        frm5.place(x=0, y=0, )

        lables=Label(text="国内承运快递：")
        lables.place(x=0, y=0)

        lable = Label(text="请输入您的收货订单：", fg='red',font=('楷体', 14),)
        lable.place(x=0, y=40)

        a = Label(frm5, text='收件人姓名：', font=('楷体', 14),).place(x=90, y=50)
        p = Label(frm5, text='    手机号：',font=('楷体', 14),).place(x=90, y=90)
        m = Label(frm5, text='      地址：',font=('楷体', 14),).place(x=90, y=130)

        ae = Entry(frm5, text='1')
        ae.place(x=235, y=50)
        pe = Entry(frm5, text='2')
        pe.place(x=235, y=90)
        me = Entry(frm5, text='3')
        me.place(x=235, y=130)

        text2 = Text(frm5, width=30, height=10,font=('楷体', 14),)  # 用来放选项内容
        text2.place(x=90, y=180)
        t1='*'
        t2='='

        if ad > 0:
            a1=str(ad)
            a2=str(b[0])
            a3=str(int(ad)*int(b[0]))
            text2.insert("end",'耐克篮球:'+a1+t1+a2+t2+a3+'元\n')#必须统一数据类型
        if ad1 > 0:
            a1=str(ad1)
            a2=str(b[1])
            a3=str(int(ad1)*int(b[1]))
            text2.insert("end",'李宁篮球:'+a1+t1+a2+t2+a3+'元\n')#必须统一数据类型
        if ad2 > 0:
            a1=str(ad2)
            a2=str(b[2])
            a3=str(int(ad2)*int(b[2]))
            text2.insert("end",'准者篮球:'+a1+t1+a2+t2+a3+'元\n')#必须统一数据类型
        if ad3 > 0:
            a1=str(ad3)
            a2=str(b[3])
            a3=str(int(ad3)*int(b[3]))
            text2.insert("end",'威尔胜篮球:'+a1+t1+a2+t2+a3+'元\n')#必须统一数据类型
        if ad4 > 0:
            a1=str(ad4)
            a2=str(b[4])
            a3=str(int(ad4)*int(b[4]))
            text2.insert("end",'斯伯丁篮球:'+a1+t1+a2+t2+a3+'元\n')#必须统一数据类型
        if ad5 > 0:
            a1=str(ad5)
            a2=str(b[5])
            a3=str(int(ad5)*int(b[5]))
            text2.insert("end",'安踏篮球:'+a1+t1+a2+t2+a3+'元\n')#必须统一数据类型

        toto=str(ad+ad1+ad2+ad3+ad4+ad5)
        toto2=str((ad*int(b[0]))+(ad1*int(b[1]))+(ad2*int(b[2]))+(ad3*int(b[3]))+(ad4*int(b[4]))+(ad5*int(b[5])))
        text2.insert("end", '\n'+'总计:'+toto+'个商品,'+'总价：'+toto2+'元'+'\n')  # 必须统一数据类型

        def show():
            yue = str(gold)
            abc = tkinter.messagebox.showinfo("温馨提示", "交易完成，欢迎下次光临\n您的余额还有：" + yue + "   元")
            windows.destroy()
            print("交易完成，欢迎下次光临") # 这里弹窗提醒

        def rt():
            windows.destroy()
            cat()

        pay = Button(frm5, text="确定",bg="#3ca3fb",fg="white", width=10, height=1, font=('楷体', 14),command=show)
        pay.place(x=120, y=405)

        fanhui = Button(frm5, text="返回", bg="#3ca3fb",fg="white",width=10, height=1, font=('楷体', 14),command=rt)
        fanhui.place(x=270, y=405)

        windows.mainloop()

#-------------------------客服人员---------------------------------
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
        Button(text="关闭", width=8, height=2, command=close).place(x=540, y=120)
        windows1.mainloop()


    def incres():
        add(1)
    def incres1():
        add1(1)
    def incres2():
        add2(1)
    def incres3():
        add3(1)
    def incres4():
        add4(1)
    def incres5():
        add5(1)

    def decres():
        add(0)
    def decres1():
        add1(0)
    def decres2():
        add2(0)
    def decres3():
        add3(0)
    def decres4():
        add4(0)
    def decres5():
        add5(0)

    #创建四个复选框  按钮 加购
    plus = Button(frm2, text="加入购物车", width=10,font=('黑体', 8),bg="red",fg="white",height=1,command=incres).place(x=115,y=245)
    plus1 = Button(frm2, text="加入购物车", width=10,font=('黑体', 8),bg="red",fg="white",height=1,command=incres1).place(x=272,y=245)
    plus2 = Button(frm2, text="加入购物车", width=10,font=('黑体', 8),bg="red",fg="white",height=1,command=incres2).place(x=425,y=245)
    plus3 = Button(frm2, text="加入购物车", width=10,font=('黑体', 8),bg="red",fg="white",height=1,command=incres3).place(x=115,y=447)
    plus4 = Button(frm2, text="加入购物车", width=10,font=('黑体', 8),bg="red",fg="white",height=1,command=incres4).place(x=272,y=447)
    plus5 = Button(frm2, text="加入购物车", width=10,font=('黑体', 8),bg="red",fg="white",height=1,command=incres5).place(x=425,y=447)

    # 创建四个复选框  按钮 加购
    pluss = Button(frm2, text="-", width=1, font=('黑体', 8), bg="blue", fg="white", height=1, command=decres).place(x=50, y=245)
    pluss1 = Button(frm2, text="-", width=1, font=('黑体', 8), bg="blue", fg="white", height=1, command=decres1).place(x=207,y=245)
    pluss2 = Button(frm2, text="-", width=1, font=('黑体', 8), bg="blue", fg="white", height=1, command=decres2).place(x=360,y=245)
    pluss3 = Button(frm2, text="-", width=1, font=('黑体', 8), bg="blue", fg="white", height=1, command=decres3).place(x=50,y=447)
    pluss4 = Button(frm2, text="-", width=1, font=('黑体', 8), bg="blue", fg="white", height=1, command=decres4).place(x=207,y=447)
    pluss5 = Button(frm2, text="-", width=1, font=('黑体', 8), bg="blue", fg="white", height=1, command=decres5).place(x=360,y=447)


    var1 = IntVar()       #创建IntVar型数据对象  勾选框
    Checkbutton(frm2,text=a[0],variable=var1,bg="white", command=callCheckbutton).place(x=70,y=200)
    var2 = IntVar()
    Checkbutton(frm2,text=a[1],variable=var2,bg="white",command=callCheckbutton).place(x=225,y=200)
    var3 = IntVar()
    Checkbutton(frm2,text=a[2],variable=var3,bg="white",command=callCheckbutton).place(x=380,y=200)
    var4 = IntVar()
    Checkbutton(frm2,text=a[3],variable=var4,bg="white",command=callCheckbutton).place(x=70,y=400)
    var5 = IntVar()
    Checkbutton(frm2,text=a[4],variable=var5,bg="white",command=callCheckbutton).place(x=225,y=400)
    var6 = IntVar()
    Checkbutton(frm2,text=a[5],variable=var6,bg="white",command=callCheckbutton).place(x=380,y=400)

    def deCat():
        window.destroy()
        cat()

    def yue():
       money=str(gold)
       Act=str(1)
       tkinter.messagebox.showinfo("尊敬的"+Act+"用户", "您的余额为："+money)


    Button(frm2, text="查看购物车", width=10,height=2,command=deCat).place(x=560,y=330)
    Button(frm2, text="查看余额", width=10,height=2,command=yue).place(x=670,y=330)
    Button(frm2, text="联系客服", width=10, height=2,command=all).place(x=560, y=400)
    Button(frm2, text="退出商场", width=10, height=2,command=window.destroy).place(x=670, y=400)
    #Button(window, text="取消选购", width=8,height=2).place(x=100,y=330)

    # 创建一个文本框
    text = Text(window,width=30,height=13) #用来放所选的商品内容
    text.place(x=550,y=125)

    window.mainloop()

mall()