# print 函数用法

## 1.输出字符串和数字

```python
>>>print("runoob")  # 输出字符串
runoob 
>>> print(100)            # 输出数字
100
>>> str = 'runoob'
>>> print(str)            # 输出变量
runoob
>>> L = [1,2,'a']         # 列表 
>>> print(L)  
[1, 2, 'a']  
>>> t = (1,2,'a')         # 元组
>>> print(t)  
(1, 2, 'a')  
>>> d = {'a':1, 'b':2}    # 字典
>>> print(d)  
{'a': 1, 'b': 2}
```

## 2. 格式化输出整数

支持参数格式化，与 C 语言的 printf 类似

```python
>>>str = "the length of (%s) is %d" %('runoob',len('runoob'))
>>> print(str)
the length of (runoob) is 6
```



**python字符串格式化符号:**



![](E:\科师\2021春资料\课程\python\笔记+代码+课件+资料\Day02-Python介绍、变量、输入输出语句\03-笔记\imgs\符号.png)



**格式化操作符辅助指令:**



![](E:\科师\2021春资料\课程\python\笔记+代码+课件+资料\Day02-Python介绍、变量、输入输出语句\03-笔记\imgs\辅助命令.png)



## 3. 格式化输出16进制，十进制，八进制整数

```python
#%x --- hex 十六进制

#%d --- dec 十进制

#%o --- oct 八进制

>>>nHex = 0xFF
>>> print("nHex = %x,nDec = %d,nOct = %o" %(nHex,nHex,nHex))
nHex = ff,nDec = 255,nOct = 377
```



## 4.格式化输出浮点数(float)

```python
>>>pi = 3.141592653  
>>> print('%10.3f' % pi) #字段宽10，精度3  
     3.142  
>>> print("pi = %.*f" % (3,pi)) #用*从后面的元组中读取字段宽度或精度  
pi = 3.142  
>>> print('%010.3f' % pi) #用0填充空白  
000003.142  
>>> print('%-10.3f' % pi) #左对齐  
3.142       
>>> print('%+f' % pi) #显示正负号  
+3.141593
```

## 5. 自动换行

print 会自动在行末加上回车, 如果不需回车，只需在 print 语句的结尾添加一个逗号 **,** 并设置分隔符参数 end，就可以改变它的行为。

```python
print(1)
print(2)
print(3)
print(4)
1
2
3
4
#如果不想自动换行，结尾加入end参数，就可以改变他结尾方式。
>>>print(1, end=" ")  #结尾加空格



```

