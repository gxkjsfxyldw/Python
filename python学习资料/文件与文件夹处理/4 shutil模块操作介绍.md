# shutil模块操作介绍

Python的os和shutil模块封装了常见的文件和目录操作如copy，cd，mv，rm以及解压等等操作。

| 方法                                                    | 功能                                   | 格式                                                         | 返回值             |
| ------------------------------------------------------- | -------------------------------------- | ------------------------------------------------------------ | ------------------ |
| copy(src, dst)                                          | 复制文件                               | shutil.copy('来源文件','目标地址')                           | 复制之后的路径     |
| copyfileobj(fsrc, fdst)                                 | 将一个文件的内容拷贝的另外一个文件当中 | shutil.copyfileobj(open(来源文件,'r'),open（'目标文件','w'）) | 无                 |
| copytree(src, dst)                                      | 复制整个文件目录                       | shutil.copytree(来源目录,目标目录)                           | 目标目录的路径     |
| move(src, dst)                                          | 移动文件或者文件夹                     | shutil.move(来源地址,目标地址)                               | 目标地址           |
| rmtree(path)                                            | 移除整个目录，无论是否空               | shutil.rmtree(目录路径)                                      | 无                 |
| make_archive(base_name, format, root_dir, …)            | 归档函数，归档操作                     | shutil.make_archive('目标文件路径','归档文件后缀','需要归档的目录') | 归档文件的最终路径 |
| unpack_archive(filename, extract_dir=None, format=None) | 解包操作                               | shutil.unpack_archive('归档文件路径','解包目标文件夹')       | None               |

注意：

**归档：**将多个文件合并到一个文件当中，这种操作方式就是归档。

**解包：**将归档的文件进行释放。

**压缩：**压缩时将多个文件进行有损或者无损的合并到一个文件当中。

**解压缩：**就是压缩的反向操作，将压缩文件中的多个文件，释放出来。

注意：压缩属于归档！

## 1 copyfileobj(fsrc, fdst) 

将fsrc文件内容复制至fdst文件

- fsrc： 源文件
- fdst： 复制至fdst文件

```python
# import shutil
# f1 = open("file1.txt","r")
# f2 = open("file_copy.txt","w")
# shutil.copyfileobj(f1,f2)
#以上报错，必须改成b二进制操作
import shutil
f1 = open("file1.txt","rb")
f2 = open("file_copy.txt","wb")
shutil.copyfileobj(f1,f2)
```

## 2 copy(src, dst) 

将文件src复制至dst。dst可以是个目录，会在该目录下创建与src同名的文件，若该目录下存在同名文件，将会报错提示已经存在同名文件。权限会被一并复制。本质是先后调用了copyfile与copymode而已