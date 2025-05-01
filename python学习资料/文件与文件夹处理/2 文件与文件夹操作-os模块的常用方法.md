# 1 文件与文件夹操作

python的os和shutill模块提供了大量的操作文件和文件夹的方法。

os模块的常用方法

| 方法                       | 功能说明                                       |
| -------------------------- | ---------------------------------------------- |
| os.getcwd()                | 返回程序的当前工作目录路径                     |
| os.chdir(path)             | 修改当前工作目录的路径                         |
| os.listdir()               | 列出指定目录下的所有文件和子目录，包括隐藏文件 |
| os.mkdir()                 | 创建单级目录（文件夹）                         |
| os.makedirs('dir1/dir2')   | 可生成多层递归目录                             |
| os.rmdir()                 | 删除单级空目录，若目录不为空则无法删除并报错   |
| os.removedirs()            | 递归删除空目录（要小心）                       |
| os.rename("oldname","new") | 重命名文件/目录                                |

```python
os.getcwd() #获取当前工作目录，即当前python脚本工作的目录路径
os.chdir("dirname") #改变当前脚本工作目录；相当于shell下cd
os.curdir   #返回当前目录: ('.')
os.pardir   #获取当前目录的父目录字符串名：('..')
os.makedirs('dir1/dir2')    #可生成多层递归目录
os.removedirs('dirname1')   #递归删除空目录（要小心）
os.mkdir('dirname') #生成单级目录
os.rmdir('dirname') #删除单级空目录，若目录不为空则无法删除并报错
os.listdir('dirname')   #列出指定目录下的所有文件和子目录，包括隐藏文件
os.remove('filename')   #删除一个文件
os.rename("oldname","new")  #重命名文件/目录
os.stat('path/filename')    #获取文件/目录信息
os.path.abspath(path)   #返回path规范化的绝对路径
os.path.split(path) #将path分割成目录和文件名二元组返回
os.path.dirname(path)   #返回path的目录。其实就是os.path.split(path)的第一个元素
os.path.basename(path)  #返回path最后的文件名。如果path以／或\结尾，那么就会返回空值。
os.path.exists(path或者file)  #如果path存在，返回True；如果path不存在，返回False
os.path.isabs(path) #如果path是绝对路径，返回True
os.path.isfile(path)    #如果path是一个存在的文件，返回True。否则返回False
os.path.isdir(path) #如果path是一个存在的目录，则返回True。否则返回False
os.path.join(path1[, path2[, ...]]) #将多个路径组合后返回，第一个绝对路径之前的参数将被忽略
os.path.getatime(path)  #返回path所指向的文件或者目录的最后存取时间
os.path.getmtime(path)  #返回path所指向的文件或者目录的最后修改时间
os.path.getsize(filename)   #返回文件包含的字符数量
```

在Python中，使用windows的文件路径时一定要小心，比如你要引用d盘下的1.txt文件，那么路径要以字符串的形式写成'd:\1.txt'或者r'd:\1.txt。前面的方式是使用windwos的双斜杠作为路径分隔符，后者是使用原生字符串的形式，以r开始的字符串都被认为是原始字符串，表示字符串里所有的特殊符号都以本色出演，不进行转义，此时可以使用普通windows下的路径表示方式。这两种方法使用哪种都可以，但不可混用。

```python
import os
print(os.getcwd())
os.chdir("d:")
print(os.getcwd())
os.makedirs("1\\2")   #在D可生成1\2目录，点击D盘查看
```

然后删除递归文件夹

```python
import os
os.chdir("d:")        #定位到d:盘目录下
print(os.getcwd())
os.removedirs("1\\2")  #删除在D生成的1\2目录，点击D盘查看
```

查看根目录的文件夹

```python
import os
os.chdir("d:")        #定位到d:盘目录下
print(os.getcwd())
print(os.listdir())   #打印 返回的根目录文件夹，放在列表中
os.mkdir("1")         #生成单个文件夹1
print('创建1文件后的目录',os.listdir())         #打印 返回的根目录文件夹，放在列表中
with open('1.txt','w+') as f:       #因为1.txt不存在，因此创建一个1.txt文本文件
    f.read()

os.rmdir("1")         #删除单级空目录，若目录不为空则无法删除并报错
print('删除1文件后的目录',os.listdir())
os.rename('1.txt','2.txt')  #重命名文件/目录
print('重复名1.txt后的目录',os.listdir())
```

```python
os.remove('2.txt')     #删除一个文件
```

* os.curdir   #返回当前目录: ('.')
  os.pardir   #获取当前目录的父目录字符串名：('..')

```python
import os
print(os.curdir)
print(os.pardir)
#.
#..

```

