import xlrd
import xlwt
from xlutils.copy import copy
import re  # 正则表达式
from tkinter import *
import tkinter as tk
import tkinter.messagebox
# --------------------------------------------------------------------------------------------------------
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

#----------------------------------------------------------------------------------------------------
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

#------------------------------------------------------------------------------------------------
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
        a = at
        end = dele
        b = bt

        main_windows.destroy()
        chose()
    ini = Button(main_windows, text="删除", width=10, command=show).place(x=120,y=170)
    qut = Button(main_windows, text="返回", width=10, command=fanhui).place(x=240,y=170)

    main_windows.mainloop()
    # 在代码中并未调用删除函数

#-------------------------------------------------------------------------------------------
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

# ---------------------------------------------------------------------------------------------
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

#------------------------------------------------------------------------------------------------------
#登录后选择窗口
def chose():

    def one(): #先销毁本窗口 再显示窗口
        main_windows.destroy()
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
    main_windows.title('欢迎来到《胖虎的幻想世界》')
    v = tk.IntVar()
    v.set(2)

    tk.Button(main_windows,bg="red", fg="white",text='进入购物商场',compound=CENTER,font=('楷体', 12), anchor='c',width=21,height=2,command=one).pack()  # command=函数
    tk.Button(main_windows, bg="orange", fg="white", text='修改密码', font=('楷体', 12), anchor='c', width=21,height=2,command=two).pack()
    tk.Button(main_windows,bg="blue", fg="white", text='注销账号', font=('楷体', 12), anchor='c', width=21,height=2,command=three).pack()
    tk.Button(main_windows,bg="indigo", fg="white", text='查看账号', font=('楷体', 12), anchor='c', width=21,height=2,command=four).pack()
    tk.Button(main_windows,bg="purple", fg="white", text='退出登录', font=('楷体', 12), anchor='c', width=21,height=2, command=five).pack()

    main_windows.mainloop()

#------------------------------------------------------------------------------------------------------------
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

