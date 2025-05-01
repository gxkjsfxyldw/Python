from tkinter import *
r = Tk()
'''创建Frame组件的方法与其他创建组件的方法不同，第一个参数不是window，也可以不加任何参数'''
def q():
    w.destroy()
def a():
    global w
    w = Tk()
    e = Entry(w)
    e.pack()
    b = Button(e,text ='退出',command = q)
    b.pack()

redbutton = Button(r, text="Redbutton", fg="white",bg='blue',command = a)
redbutton.pack( side = LEFT)
brownbutton = Button(r, text="Brownbutton", fg="brown",bg='yellow')
brownbutton.pack( side = RIGHT )
bluebutton = Button(r, text="Bluebutton", fg="blue",bg='white')
bluebutton.pack( side = LEFT )

r.mainloop()

