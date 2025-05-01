# Python正则表达式中的re.S，re.M，re.I的作用

| 修饰符 | 描述                                                         |
| ------ | ------------------------------------------------------------ |
| re.l   | 使匹配对大小写不敏感                                         |
| re.L   | 做本地化识别(locale-aware)                                   |
| re.M   | 多匹配，影响^和$                                             |
| re.S   | 使.匹配包括换行在内的所有字符                                |
| re.U   | 根据Unicode字符集解析字符。这个标志影响\w，\W，\b，\B        |
| re.X   | 该标志通过给予你更灵活的格式以便你将正则表达式写得更易于理解。 |

### re.S

在Python的正则表达式中，有一个参数为re.S。它表示 “.” 的作用扩展到整个字符串，包括“\n”。看如下代码：

```python
import re
a = '''asdfhellopass:
    worldaf
    '''
b = re.findall('hello(.*?)world',a)
c = re.findall('hello(.*?)world',a,re.S)
print('b is ', b)
print('c is ', c)
#b is  []
#c is  ['pass:\n    ']
```

### re.I

不区分大小写

```python
import re

res = re.findall(r"AbC", "abc", re.I)
print(res)
#['abc']
```

### re.M

将所有行的头尾字符输出

```python
import re
s= '12 34\n56 78\n90'
print(re.findall(r'^\d+', s, re.M))   ## 匹配位于字符串开头的数字
print(re.findall(r'\A\d+', s, re.M))  #匹配字符串开始
print(re.findall(r'\d+$', s, re.M))  # 匹配位于行尾的数字
print(re.findall(r'\d+\Z', s, re.M)) # 匹配位于行尾的数字
#['12', '56', '90']
#['12']
#['34', '78', '90']
#['90']
```

### re.X



```python
import re
s= '  123'
print(re.findall('''

\ +
 
 ''', s, re.X))
#['  ']
```