#雪球股票爬虫
import hashlib#将指定的 “字符串” 进行加密。使用hashlib的分步解析
import random #随机数
import time #时间戳
from tkinter import END, Button, Label, StringVar, Text, Tk, messagebox,PhotoImage
from tkinter.ttk import Combobox #下拉框
import requests #网页请求
from lxml import etree #网站解析器

class translate(object):#生成翻译的类

    def __init__(self):#构造函数
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'}#浏览器版本
        self.url1 = 'http://fanyi.youdao.com/' #爬取翻译语言代号网址
        self.url2 = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'#爬取翻译器网址

    def getlange(self):#爬取有道翻译网页中不同语言的代码代号
        lan_list = []#保存中翻英
        text_list = []#保存英翻中

        res = requests.get(url=self.url1, headers=self.headers)#访问网站
        html = etree.HTML(res.text)#网站解析
        li_list = html.xpath('/html/body/div[2]/div[1]/div[2]/div[1]/ul//li')#找到网页中存放语言代码的位置

        for i in li_list:#提取需要的信息
            dataval = i.xpath('./@data-value')[0].split('2')  # data-value标签 split截取字符串
            lan_list.append(dataval)

            text = i.xpath('./a/text()')[0].replace('\xa0', '') #截取语言的中文  用空字符代替文字中含有的\xa0
            text_list.append(text)

        lan_list[0].append('AUTO')
        # print(text_list)
        # print(lan_list)
        return lan_list, text_list


    def crawler(self, i, fromto):#翻译爬虫 i为译文  fromto为翻译语言  这里需要注意一下有道的反爬虫机制 不然做不到翻译其他语言
        # returnlist=list()
        header = {
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Connection': 'keep-alive',
            'Content-Length': '239',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Cookie': 'OUTFOX_SEARCH_USER_ID=48328342@10.108.160.100; OUTFOX_SEARCH_USER_ID_NCOO=276358647.14339805; JSESSIONID=aaaZHn7tLjpDiaro7Y2Hx; ___rl__test__cookies=%s'
                      % (str(int(time.time() * 1000))),
            'Host': 'fanyi.youdao.com',
            'Origin': 'http', 'Referer': 'http',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest'
        }  #需要header里面需要添加cookies才能爬取到译文

        # cookies中只有___rl__test__cookies发生变化，而ta的值就是当前时间戳
        salt = str(int(time.time() * 1000) + random.randint(1, 10))
        sign = hashlib.md5(('fanyideskweb' + i + salt + 'Tbh5E8=q6U3EXe+&L[4c@').encode('utf-8')).hexdigest()#转换陈加密模式hexdigest

        data = {
            'i': i,#翻译原文
            'from': fromto[0],#翻译原文的语言
            'to': fromto[1],#需要翻译成的语言
            'smartresult': 'dict',
            'client': 'fanyideskweb',
            'salt': salt,#这个值应该是下面的lts加一位数字，待验证
            'sign': sign,#服务器签名验证
            'its': str(int(time.time() * 1000)),#自动生成的时间戳字符串数字
            'bv': 'cda1e53e0c0eb8dd4002cefc117fa588',
            'doctype': 'json',
            'version': '2.1',
            'keyfrom': 'fanyi.web',
            'action': 'lan-select'
        }
        try:#异常机制
            res = requests.post(url=self.url2, data=data, headers=header)
            json_data = res.json()#解析网页响应的内容
            #print(json_data,'\n')
            result_list = json_data['translateResult'][0]
            print(result_list)
            '''for i in result_list:
                result=i[0]['tgt']
                returnlist.append(result)'''
            return result_list

        except KeyError as e:#发生异常时
            return e


class ui():#可视化界面制作
    def __init__(self):
        self.fanyi = translate()#创建翻译对象
        self.list1, self.list2 = self.fanyi.getlange()#创建两个对象存放翻译语言和代号
        self.index = 0  # 默认自动翻译
        self.count = 1

        self.window = Tk()  # 创建窗口
        self.window.title('《李达旺》翻译官')
        self.window.geometry('1000x550')  # width height
        self.window.iconbitmap("888.ico")#窗口小图标

        self.photo = PhotoImage(file=r'1.png')
        self.lableimg1=Label(self.window, text='', image=self.photo) # 插入背景及规定起始位置
        self.lableimg1.place(x=0, y=0)

        self.photo2=PhotoImage(file="2.png")
        self.lableimg2=Label(self.window,text="",image=self.photo2)
        self.lableimg2.place(x=0,y=430)

        self.photo3=PhotoImage(file="3.png")
        self.lableimg3=Label(self.window,text="",image=self.photo3)
        self.lableimg3.place(x=470,y=220)


        #两个显示内容的输入框
        self.text1 = Text(self.window, background='GREY85')
        self.text1.place(x=170, y=110, width=300, relheight=0.5)

        self.text2 = Text(self.window, background='GREY85')
        self.text2.place(x=530, y=110, width=300, relheight=0.5)

        self.var = StringVar()#实时更新字符串变量类型  var表示这个实例的变量

        # 按钮
        self.button1 = Button(self.window, text='翻译', command=self.submit, font=('宋体', 15),bg="red",fg='white')  #
        self.button2 = Button(self.window, text='清空', command=self.clean_all, font=('宋体', 15),bg="white",fg='red')

        self.button1.place(x=390, y=390, width=100, height=40)
        self.button2.place(x=510, y=390, width=100, height=40)

        self.button3 = Button(self.window, text='->>', bg="blue",fg="white", font=(None, 15))#下一组语言的转换
        self.button3.place(x=350, y=75, width=50, height=30)
        self.button3.bind('<Button-1>', self.click_left)#按钮绑定事件  1表示鼠标单击左键的调用此函数， 2表示鼠标中键  3表示右键

        self.button4 = Button(self.window, text='<<-', bg="red",fg="white",font=(None, 15))#上一组语言的转换
        self.button4.place(x=290, y=75, width=50, height=30)
        self.button4.bind('<Button-1>', self.click_right)#按钮绑定事件

        # 标签
        self.label1 = Label(self.window, text='输入原文:', font=('宋体', 15),fg="red")
        self.label1.place(x=65, y=100, width=100, height=30)

        self.label1 = Label(self.window, text='译文如下:', font=('宋体', 15),fg="red")
        self.label1.place(x=525, y=70, width=100, height=30)

        # 下拉列表
        self.comb = Combobox(self.window, textvariable=self.var, values=self.list2)#从下拉框获取值 textvariable 通过StringVar设置可改变的值 并执行参数
        # -self.comb=Combobox(self.window,textvariable=self.var,values=list1)
        self.comb.place(x=170, y=68, width=100, height=40)
        self.comb.set('自动检测语言')  # 默认自动检测语言
        self.comb.bind('<<ComboboxSelected>>', self.select)#选中下拉列表时所选择的执行的选项，并执行参数

    def click_left(self, event):#按左边的箭头
        self.index += 1
        self.comb.set('{}'.format(self.list2[self.index]))

    def click_right(self, event):#按右边的箭头
        if self.index > 0:#刚开始的时候
            self.index -= 1
            self.comb.set('{}'.format(self.list2[self.index]))

    def select(self, event):#下拉框选项
        #print(self.comb.current(1))有参数时它就指定下拉框的选项
        self.index = self.comb.current()#没有参数时它就返回当前下拉框的位置数值
        print(self.index)
        print(self.list1[self.index])
        # print(list1[self.index])

    def submit(self):#执行翻译
        self.text2.delete(0.0, END)#先把翻译那个框之前的数据清除了先
        content = self.text1.get(0.0, END).replace('\n', ' ')#提取原文输入框中的数据 从0到end replace表示用空格替换 换行 这样就算的有换行也能翻译出来了
        print(content)

        #print('###',self.list1)
        text = self.fanyi.crawler(content, self.list1[self.index])#调用网页翻译方法 并返回译文给text
        # text=self.fanyi.crawler(content,list2[self.index])
        #print('@@@',text)

        if text:#将译文输出到翻译框中
            for i in text:
                self.text2.insert(END, (i['tgt'] + '\n'))
        else:
            messagebox.showerror('error', '-1')

    def clean_all(self):#清除两个文本框中的全部内容
        self.text1.delete(0.0, END)
        self.text2.delete(0.0, END)

    def run(self):#执行程序
        self.window.mainloop()

if __name__ == '__main__':
    a = ui()#先显示可视化界面
    a.run()#再进入爬虫程序
