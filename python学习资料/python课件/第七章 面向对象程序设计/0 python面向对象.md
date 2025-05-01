# 1 什么是面向对象

* Python面向对象（一切皆对象）

Python 语言在设计之初，就定位为一门面向对象的编程语言，“Python 中一切皆对象”就是对 Python 这门编程语言的完美诠释。

类和对象是 Python 的重要特征，相比其它面向对象语言，Python 很容易就可以创建出一个类和对象。同时，Python 也支持面向对象的三大特征：封装、继承和多态。

代码封装，其实就是隐藏实现功能的具体代码，仅留给用户使用的接口，就好像使用计算机，用户只需要使用键盘、鼠标就可以实现一些功能，而根本不需要知道其内部是如何工作的。

打个比方，若在某游戏中设计一个乌龟的角色，应该如何来实现呢？使用面向对象的思想会更简单，可以分为如下两个方面进行描述：

1. 从表面特征来描述，例如，绿色的、有 4 条腿、重 10 kg、有外壳等等。
2. 从所具有的的行为来描述，例如，它会爬、会吃东西、会睡觉、会将头和四肢缩到壳里，等等。

```python
class Tortoise:
    bodyColor = "绿色"
    footNum = 4
    weight = 10
    hasShell = True

    #会爬
    def pa(self):
        print("乌龟会爬")
    #会吃东西
    def eat(self):
        print("乌龟吃东西")
    #会睡觉
    def sleep(self):
        print("乌龟在睡觉")
    #会缩到壳里
    def fangyu(self):
        print("乌龟缩进了壳里")
```

面向对象中，常用术语包括：

- 类：可以理解是一个模板，通过它可以创建出无数个具体实例。比如，前面编写的 WuGui表示的只是乌龟这个物种，通过它可以创建出无数个实例来代表各种不同特征的乌龟（这一过程又称为类的实例化）。
- 对象：类并不能直接使用，通过类创建出的实例（又称对象）才能使用。这有点像汽车图纸和汽车的关系，图纸本身（类）并不能为人们使用，通过图纸创建出的一辆辆车（对象）才能使用。
- 属性：类中的所有变量称为属性。例如，WuGui这个类中，bodyColor、footNum、weight、hasShell 都是这个类拥有的属性。
- 方法：类中的所有函数通常称为方法。不过，和函数所有不同的是，类方法至少要包含一个 self 参数（后续会做详细介绍）。例如，tortoise 类中，pa()、eat()、sleep()、fangyu() 都是这个类所拥有的方法，类方法无法单独使用，只能和类的对象一起使用。



# 2 Python类的定义

Python 中定义一个类使用 class 关键字实现，其基本语法格式如下：

```
class 类名：
  多个（≥0）类属性...
  多个（≥0）类方法...
```

* 注意，无论是类属性还是类方法，对于类来说，它们都不是必需的，可以有也可以没有。另外，Python 类中属性和方法所在的位置是任意的，即它们之间并没有固定的前后次序。
* 注意，如果由单词构成类名，建议每个单词的首字母大写，其它字母小写。

给类起好名字之后，其后要跟有冒号（：），表示告诉 Python 解释器，下面要开始设计类的内部功能了，也就是编写类属性和类方法。

其实，类属性指的就是包含在类中的变量；而类方法指的是包含类中的函数。换句话说，类属性和类方法其实分别是包含类中的变量和函数的别称。

通过上面的分析，可以得出这样一个结论，即 Python 类是由类头（class 类名）和类体（统一缩进的变量和函数）构成。例如，下面程序定义一个 TheFirstDemo 类：

```python
class TheFirstDemo:
    # 下面定义了一个类属性
    add = '我是类属性'
    # 下面定义了一个say方法
    def say(self, content):
        print(content)
```

另外分析上面的代码可以看到，我们创建了一个名为 TheFirstDemo 的类，其包含了一个名为 add 的类属性。注意，根据定义属性位置的不同，在各个类方法之外定义的变量称为类属性或类变量（如 add 属性），而在类方法中定义的属性称为实例属性（或实例变量）。

同时，TheFirstDemo 类中还包含一个 say() 类方法，细心的读者可能已经看到，该方法包含两个参数，分别是 self 和 content。可以肯定的是，content 参数就只是一个普通参数，没有特殊含义，但 self 比较特殊，并不是普通的参数，它的作用会在后续章节中详细介绍。



# 3 Python `__init__()`类构造方法

在创建类时，我们可以手动添加一个 __init__() 方法，该方法是一个特殊的类实例方法，称为构造方法（或构造函数）。

构造方法用于创建对象时使用，每当创建一个类的实例对象时，[Python](http://c.biancheng.net/python/) 解释器都会自动调用它。[Python](http://c.biancheng.net/python/) 类中，手动添加构造方法的语法格式如下：

```python
def __init__(self,...):
    代码块
```

* 注意，此方法的方法名中，开头和结尾各有 **2 个下划线**，且中间不能有空格。Python 中很多这种以双下划线开头、双下划线结尾的方法，**都**具有特殊的意义，后续会一一为大家讲解。

另外，__init__() 方法可以包含多个参数，但必须包含一个名为 self 的参数，且必须作为第一个参数。也就是说，类的构造方法最少也要有一个 self 参数。例如，仍以 TheFirstDemo 类为例，添加构造方法的代码如下所示：

```python
class TheFirstDemo:
    #构造方法
    def __init__(self):
        print("调用构造方法")
    # 下面定义了一个类属性
    add = '我是一个类属性'
    # 下面定义了一个say方法
    def say(self, content):
        print(content)
```

仅包含 self 参数的 __init__() 构造方法，又称为类的默认构造方法。

```python
a = TheFirstDemo()
#调用构造方法
```

这行代码的含义是创建一个名为 a的 TheFirstDemo 类对象。运行代码可看到如下结果：#调用构造方法

显然，在创建 a这个对象时，隐式调用了我们手动创建的 __init__() 构造方法。

不仅如此，在 __init__() 构造方法中，除了 self 参数外，还可以自定义一些参数，参数之间使用逗号“,”进行分割。例如，下面的代码在创建 __init__() 方法时，额外指定了 2 个参数：

```python
class TheFirstDemo:
    #构造方法
    def __init__(self,name,age):
        print(name+'今年%d'%age+'岁')
    # 下面定义了一个类属性
    add = '我是一个类属性'
    # 下面定义了一个say方法
    def say(self, content):
        print(content)

a = TheFirstDemo('小明',17)
#小明今年17岁
```

可以看到，虽然构造方法中有 self、name、add 3 个参数，但实际需要传参的仅有 name 和 add，也就是说，self 不需要手动传递参数。关于 self 参数，后续章节会做详细介绍，这里只需要知道，在创建类对象时，无需给 self 传参即可。



# 4 Python类对象的创建和使用

## 4.1 类的实例化

定义类时，如果没有手动添加 __init__() 构造方法，又或者添加的 __init__() 中仅有一个 self 参数，则创建类对象时的参数可以省略不写。

例如，如下代码创建了名为 CLanguage 的类，并对其进行了实例化：

```python
class TheFirstDemo:
    #构造方法
    def __init__(self,name,age):
        print(name+'今年%d'%age+'岁')
    #下面定义 2 个实例变量或者实例属性
    	self.name = name
    	self.age = age
    add = '我是一个类属性'
    # 下面定义了一个say方法
    def say(self, content):
        print(content)

a = TheFirstDemo('小明',17)
#小明今年17岁
```

在上面的程序中，由于构造方法除 self 参数外，还包含 2 个参数，且这 2 个参数没有设置默认参数，因此在实例化类对象时，需要传入相应的 name 值和 add 值（self 参数是特殊参数，不需要手动传值，Python 会自动传给它值）。

类变量和实例变量，简单地理解，定义在各个类方法之外（包含在类中）的变量为类变量（或者类属性），定义在类方法中的变量为实例变量（或者实例属性）。

## 4.2 Python类对象的使用

定义的类只有进行实例化，也就是使用该类创建对象之后，才能得到利用。总的来说，实例化后的类对象可以执行以下操作：

- 访问或修改类对象具有的实例变量，甚至可以添加新的实例变量或者删除已有的实例变量；
- 调用类对象的方法，包括调用现有的方法，以及给类对象动态添加方法。

### 4.2.1 类对象访问变量或方法

使用已创建好的类对象访问类中实例变量的语法格式如下：

```Python
class TheFirstDemo:
    #构造方法
    def __init__(self,name,age):
        print(name+'今年%d'%age+'岁')
    #下面定义 2 个实例变量或者实例属性
        self.name = name
        self.age = age
    add = '我是一个类属性'
    # 下面定义了一个say方法
    def say(self, content):
        print(content)
a = TheFirstDemo('小明',17)
print(a.name, a.age)
a.name = '小东'    #修改实例变量的值
a.age = 18
print('修改后的实例a的name:{}，age:{}'.format(a.name, a.age))
a.say('人生苦短，我用Python')   #调用实例a的say方法

#小明今年17岁
#小明 17
#修改后的实例a的name:小东，age:18
#人生苦短，我用Python
```

### 4.2.2 给类对象动态添加/删除变量

Python 支持为已创建好的对象动态增加实例变量，方法也很简单，举个例子：

```Python
a.money = 100
print(a.money)
#100
```

既然能动态添加，那么是否能动态删除呢？答案是肯定的，使用 del 语句即可实现，例如：

```Python
#删除新添加的 money 实例变量
del a.money
#再次尝试输出 money，此时会报错
print(a.money)
#AttributeError: 'TheFirstDemo' object has no attribute 'money'
```

Python 也允许为对象动态增加方法。以本节开头的 a类为例，由于其内部只包含一个 say() 方法，因此该类实例化出的 a对象也只包含一个 say() 方法。但其实，我们还可以为 a对象动态添加其它方法。

需要注意的一点是，为 a对象动态增加的方法，Python 不会自动将调用者自动绑定到第一个参数（即使将第一个参数命名为 self 也没用）。例如如下代码：

```python
def b(self):
    print(self.name)

a.c = b
a.c(a)
#小东
```

通过借助 types 模块下的 a可以实现，仍以上面的 b() 函数为例：

```python
from types import MethodType
def b(self):
    print(self.name)

a.c = MethodType(b,a)
a.c()
#小东
```

可以看到，由于使用 a包装 b() 函数时，已经将该函数的 self 参数绑定为 a，因此后续再使用 b() 函数时，就不用再给 self 参数绑定值了。



# 5 Python self用法详解

在定义类的过程中，无论是显式创建类的构造方法，还是向类中添加实例方法，都要求将 self 参数作为方法的第一个参数。例如，定义一个 Person 类：

```python
class Person:
    def __init__(self):
        print("正在执行构造方法")
    # 定义一个study()实例方法
    def study(self,name):
        print(name,"正在学Python")
```

那么，self 到底扮演着什么样的角色呢？本节就对 self 参数做详细的介绍。

事实上，Python 只是规定，无论是构造方法还是实例方法，最少要包含一个参数，并没有规定该参数的具体名称。之所以将其命名为 self，只是程序员之间约定俗成的一种习惯，遵守这个约定，可以使我们编写的代码具有更好的可读性（大家一看到 self，就知道它的作用）。

那么，self 参数的具体作用是什么呢？打个比方，如果把类比作造房子的图纸，那么类实例化后的对象是真正可以住的房子。根据一张图纸（类），我们可以设计出成千上万的房子（类对象），每个房子长相都是类似的（都有相同的类变量和类方法），但它们都有各自的主人，那么如何对它们进行区分呢？

当然是通过 self 参数，它就相当于每个房子的门钥匙，可以保证每个房子的主人仅能进入自己的房子（每个类对象只能调用自己的类变量和类方法）。

也就是说，同一个类可以产生多个对象，当某个对象调用类方法时，该对象会把自身的引用作为第一个参数自动传给该方法，换句话说，Python 会自动绑定类方法的第一个参数指向调用该方法的对象。如此，Python解释器就能知道到底要操作哪个对象的方法了。

因此，程序在调用实例方法和构造方法时，不需要手动为第一个参数传值。例如，更改前面的 Person 类，如下所示：

```python
class Person:
    def __init__(self):
        print("正在执行构造方法")
    # 定义一个study()实例方法
    def study(self):
        print(self,"正在学Python")
zhangsan = Person()
zhangsan.study()
lisi = Person()
lisi.study()
#正在执行构造方法
#<__main__.Person object at 0x000001DA88371FD0> 正在学Python
#正在执行构造方法
#<__main__.Person object at 0x000001DA88371DF0> 正在学Python
```

上面代码中，study() 中的 self 代表该方法的调用者，即谁调用该方法，那么 self 就代表谁。

另外，对于构造函数中的 self 参数，其代表的是当前正在初始化的类对象。举个例子：

```python
class Person:
    name = "xxx"
    def __init__(self,name):
        self.name=name
zhangsan = Person("张三")
print(zhangsan.name)
lisi = Person("李四")
print(lisi.name)
#张三
#李四
```

可以看到，zhangsan 在进行初始化时，调用的构造函数中 self 代表的是 zhangsan；而 lisi 在进行初始化时，调用的构造函数中 self 代表的是 lisi。

总之，无论是类中的构造函数还是普通的类方法，实际调用它们的谁，则第一个参数 self 就代表谁。



# 6 Python类变量和实例变量（类属性和实例属性）

无论是类属性还是类方法，都无法像普通变量或者函数那样，在类的外部直接使用它们。我们可以将类看做一个独立的空间，则类属性其实就是在类体中定义的变量，类方法是在类体中定义的函数。

前面章节提到过，在类体中，根据变量定义的位置不同，以及定义的方式不同，类属性又可细分为以下 3 种类型：

1. 类体中、所有函数之外：此范围定义的变量，称为类属性或类变量；
2. 类体中，所有函数内部：以“self.变量名”的方式定义的变量，称为实例属性或实例变量；
3. 类体中，所有函数内部：以“变量名=变量值”的方式定义的变量，称为局部变量。

* 不仅如此，类方法也可细分为实例方法、静态方法和类方法，后续章节会做详细介绍。



## 6.1 类变量（类属性）

类变量指的是在类中，但在各个类方法外定义的变量。举个例子：

```Python
class Dog :
    # 下面定义了2个类变量
    name = "小狗狗"
    add = "豪华狗窝"
    # 下面定义了一个say实例方法
    def say(self, content):
        print(content)
```

上面程序中，name 和 add 就属于类变量。

类变量的特点是，所有类的实例化对象都同时共享类变量，也就是说，类变量在所有实例化对象中是作为公用资源存在的。类方法的调用方式有 2 种，既可以使用类名直接调用，也可以使用类的实例化对象调用。

比如，在 Dog类的外部，添加如下代码：

```python
#使用类名直接调用
print(Dog.name)
print(Dog.add)
#修改类变量的值
Dog.name = "大狗狗"
Dog.add = "六星级狗窝"
print(Dog.name)
print(Dog.add)
#小狗狗
#豪华狗窝
#大狗狗
#六星级狗窝
```

可以看到，通过类名不仅可以调用类变量，也可以修改它的值。

当然，也可以使用类对象来调用所属类中的类变量（此方式不推荐使用，原因后续会讲）。例如，在 Dog类的外部，添加如下代码：

```python
g = Dog()
print(g.name)
print(g.add)
#小狗狗
#豪华狗窝
```

* 注意，因为类变量为所有实例化对象共有，通过类名修改类变量的值，会影响所有的实例化对象。例如，在 CLanguage 类体外部，添加如下代码：

```python
print("修改前，各类对象中类变量的值：")
g1 = Dog()
print(g1.name)
print(g1.add)
g2 = Dog()
print(g2.name)
print(g2.add)
print("修改后，各类对象中类变量的值：")
Dog.name = "大狗狗"
Dog.add = "六星级狗窝"
print(g1.name)
print(g1.add)
print(g2.name)
print(g2.add)
#修改前，各类对象中类变量的值：
#小狗狗
#豪华狗窝
#小狗狗
#豪华狗窝
#修改后，各类对象中类变量的值：
#大狗狗
#六星级狗窝
#大狗狗
#六星级狗窝
```

显然，通过类名修改类变量，会作用到所有的实例化对象（例如这里的g1 和g2）。

* 注意，通过类对象是无法修改类变量的。通过类对象对类变量赋值，其本质将不再是修改类变量的值，而是在给该对象定义新的实例变量（在讲实例变量时会进行详细介绍）。

值得一提的是，除了可以通过类名访问类变量之外，还可以动态地为类和对象添加类变量。例如，在 Dog类的基础上，添加以下代码：

```python
g1 = Dog()
Dog.age = 3
print(g1.age)
#3
```



## 6.2 实例变量（实例属性）

实例变量指的是在任意类方法内部，以“self.变量名”的方式定义的变量，其特点是只作用于调用方法的对象。另外，实例变量只能通过对象名访问，无法通过类名访问。

```python
class Dog :
    def __init__(self):
        self.name = "小狗狗"
        self.add = "豪华狗窝"
    # 下面定义了一个say实例方法
    def say(self):
        self.bark = '汪汪'
        
```

此 Dog类中，name、add 以及 bark都是实例变量。其中，由于 __init__() 函数在创建类对象时会自动调用，而 say() 方法需要类对象手动调用。因此，Dog类的类对象都会包含 name 和 add 实例变量，而只有调用了 say() 方法的类对象，才包含 bark实例变量。

例如，在上面代码的基础上，添加如下语句：

```python
g1 = Dog()
print(g1.name)
print(g1.add)
#由于 g1 对象未调用 say() 方法，因此其没有 bark 变量，下面这行代码会报错
#print(g1.bark)
g2 = Dog()
print(g2.name)
print(g2.add)
#只有调用 say()，才会拥有 bark 实例变量
g2.say()
print(g2.bark)
#小狗狗
#豪华狗窝
#小狗狗
#豪华狗窝
#汪汪
```

前面讲过，通过类对象可以访问类变量，但无法修改类变量的值。这是因为，通过类对象修改类变量的值，不是在给“类变量赋值”，而是定义新的实例变量。

另外，和类变量不同，通过某个对象修改实例变量的值，不会影响类的其它实例化对象，更不会影响同名的类变量。

## 6.3 局部变量

除了实例变量，类方法中还可以定义局部变量。和前者不同，局部变量直接以“变量名=值”的方式进行定义，例如：

```python
class Buy :
    # 下面定义了一个say实例方法
    def count(self,money):
        sale = 0.8*money
        print("优惠后的价格为：",sale)
clang = Buy()
clang.count(100)
#优惠后的价格为： 80.0
```

通常情况下，定义局部变量是为了所在类方法功能的实现。需要注意的一点是，局部变量只能用于所在函数中，函数执行完成后，局部变量也会被销毁。

# 7 私有属性、公有属性

- 私有属性

  函数、方法或者属性的名称以两个下划线开始，则为私有类型；

- 公有属性

  如果函数、方法或者属性的名称没有以两个下划线开始，则为公有属性；

- `_xxx`，单下划线开头的变量，标明是一个受保护(protected)的变量，原则上不允许直接访问，但外部类还是可以访问到这个变量。这只是程序员之间的一个约定，用于警告说明这是一个私有变量，外部类不要去访问它。
- `__xxx`，双下划线开头的，表示的是私有类型(private)的变量。只能是允许这个类本身进行访问了, 连子类也不可以，用于命名一个类属性（类变量），调用时名字被改变（在类Student内部，`__name`变成`_Person__name`,如 `self._Person__name`)

```python
class person:
    def __init__(self,name,age,sex):
        self.__name = name
        self._age = age
        self.sex = sex

a = person('小花',20,'女')
print(a.sex)
print(a._age)
print(a.__name)
#AttributeError: 'person' object has no attribute '__name'
```

双下划线开头的实例变量是不是一定不能从外部访问呢？其实也不是。仍然可以通过`self._Person__age`来访问`__name`变量：

```python
print(a._Person__name)
#小花
```

* `__xxx__`，以双下划线开头，并且以双下划线结尾的，是内置变量，内置变量是可以直接访问的，不是 private 变量，如`__init__`，`__import__`或是`__file__`。所以，不要自己定义这类变量。

```python
class Person:
    def __init__(self,name,age,sex):
        self.__name = name
        self._age = age
        self.sex = sex
    def _money(self):
        print(self.__name,'有',10,'亿')

a = Person('小花',20,'女')
print(a._Person__name)
a._money()
#小花
#小花 有 10 亿
```

一个下划线其实可以说是正常的命名规则。两个下划线才是私有方法

```python
class Person:
    def __init__(self,name,age,sex):
        self.__name = name
        self._age = age
        self.sex = sex
    def __money(self):
        print(self.__name,'有',10,'亿')

a = Person('小花',20,'女')
a.__money()
#AttributeError: 'Person' object has no attribute '__money'
```

调用私有方法也是和上面一样

```Python
a._Person__money()
#小花 有 10 亿
```

* Python运行这种方式访问变量，主要是为保护类中的资源，避免“不小心”被修改。虽然可以通过这种方式修改，但不建议使用。

# 8 @property的介绍与使用

python的@property是python的一种装饰器，是用来修饰方法的。
作用：
我们可以使用@property装饰器来创建只读属性，@property装饰器会将方法转换为相同名称的只读属性,可以与所定义的属性配合使用，这样可以防止属性被修改。

使用场景：

## 8.1 修饰方法，是方法可以像属性一样访问。

```Python
class Person:
    def __init__(self,name,age,money):
        self.__name = name
        self.age = age
        self.__money = money
    @property
    def money(self):
        return self.__money

    def money1(self):
        return self.__money
a = Person('小花',20,1000000)
print(a.money) # 加了@property后，可以用调用属性的形式来调用方法,后面不需要加（）。

print(a.money1())  #没有加@property , 必须使用正常的调用方法的形式，即在后面加()
#1000000
#1000000
```

如果使用property进行修饰后，又在调用的时候，方法后面添加了()， 那么就会显示错误信息：TypeError: ‘int’ object is not callable，也就是说添加@property 后，这个方法就变成了一个属性，如果后面加入了()，那么就是当作函数来调用，而它却不是callable（可调用）的。

## 8.2 与所定义的属性配合使用，这样可以防止属性被修改。

由于python进行属性的定义时，没办法设置私有属性，因此要通过@property的方法来进行设置。这样可以隐藏属性名，让用户进行使用的时候无法随意修改。也可以使用@（@property的方法名）.setter。例如以下的 @property的方法为money，那么就是修改方法的名称都要死money。@money.setter是@money.setter装饰后的副产品。

```Python
class Person:
    def __init__(self,name,age,money):
        self.__name = name
        self.age = age
        self.__money = money
    @property         #装饰器，提供“读属性”
    def money(self):
        return self.__money

    @money.setter        #装饰器，提供“修改属性”
    def money(self,money):
        self.__money = money
        return self.__money
a = Person('小花',20,1000000)
print(a.money) # 加了@property后，可以用调用属性的形式来调用方法,后面不需要加（）。
a.money = 100
print(a.money)  #没有加@property , 必须使用正常的调用方法的形式，即在后面加()
```

## 8.3 使用@deleter来删除属性

```Python
class Person:
    def __init__(self,name,age,money):
        self.__name = name
        self.age = age
        self.__money = money
    @property         #装饰器，提供“读属性”
    def money(self):
        return self.__money

    @money.setter        #装饰器，提供“修改属性”
    def money(self,money):
        self.__money = money
        return self.__money
    @money.deleter
    def money(self):
        del self.__money
a = Person('小花',20,1000000)
print(a.money) # 加了@property后，可以用调用属性的形式来调用方法,后面不需要加（）。
a.money = 100
print(a.money)  #没有加@property , 必须使用正常的调用方法的形式，即在后面加()
del a.money
print(a.money)
#AttributeError: 'Person' object has no attribute '_Person__money'
```

# 9 Python实例方法、静态方法和类方法详解（包含区别和用法）

和类属性一样，类方法也可以进行更细致的划分，具体可分为类方法、实例方法和静态方法。

和类属性的分类不同，对于初学者来说，区分这 3 种类方法是非常简单的，即采用 @classmethod 修饰的方法为类方法；采用 @staticmethod 修饰的方法为静态方法；不用任何修改的方法为实例方法。

> 其中 @classmethod 和 @staticmethod 都是函数装饰器，后续章节会对其做详细介绍。

接下来就给大家详细的介绍这 3 种类方法。

## 9.1 类实例方法

通常情况下，在类中定义的方法默认都是实例方法。前面章节中，我们已经定义了不只一个实例方法。不仅如此，类的构造方法理论上也属于实例方法，只不过它比较特殊。

比如，下面的类中就用到了实例方法：

```Python
class Dog :
    # 下面定义了一个say实例方法
    def say(self):
        print("汪汪~")
dog = Dog()
dog.say()
#汪汪~
```

实例方法最大的特点就是，它最少也要包含一个 self 参数，用于绑定调用此方法的实例对象（Python 会自动完成绑定）。实例方法通常会用类对象直接调用。

当然，Python 也支持使用类名调用实例方法，但此方式需要手动给 self 参数传值。例如：

```Python
dog = Dog()
Dog.say(dog)
#汪汪~
#汪汪~
```

## 9.2 Python类方法

Python 类方法和实例方法相似，它最少也要包含一个参数，只不过类方法中通常将其命名为 cls，Python 会自动将类本身绑定给 cls 参数（注意，绑定的不是类对象）。也就是说，我们在调用类方法时，无需显式为 cls 参数传参。

* 和 self 一样，cls 参数的命名也不是规定的（可以随意命名），只是 Python 程序员约定俗称的习惯而已。

和实例方法最大的不同在于，类方法需要使用＠classmethod修饰符进行修饰，例如：

```Python
class Dog :
    # 下面定义了一个say实例方法
    def say(self):
        print("汪汪~")
    # 下面定义一个类方法
    @classmethod
    def age(cls):
        print('3岁了')
dog = Dog()
dog.age()   #类方法推荐使用类名直接调用，当然也可以使用实例对象来调用（不推荐）。
Dog.age()
#3岁了
#3岁了
```

## 9.3 Python类静态方法

静态方法，其实就是我们学过的函数，和函数唯一的区别是，静态方法定义在类这个空间（类命名空间）中，而函数则定义在程序所在的空间（全局命名空间）中。

静态方法没有类似 self、cls 这样的特殊参数，因此 Python 解释器不会对它包含的参数做任何类或对象的绑定。也正因为如此，类的静态方法中无法调用任何类属性和类方法。

静态方法需要使用＠staticmethod修饰，例如：

```Python
class Dog :
    # 下面定义了一个say实例方法
    @staticmethod
    def say(bark):
        print('叫声为：',bark)
    # 下面定义一个类方法

Dog.say('汪汪~')
dog = Dog()
dog.say('汪汪~')
#叫声为： 汪汪~
#叫声为： 汪汪~
```

在实际编程中，几乎不会用到类方法和静态方法，因为我们完全可以使用函数代替它们实现想要的功能，但在一些特殊的场景中（使用类方法和静态方法也是很不错的选择。

# 10 Python类调用实例方法

通过前面的学习，类方法大体分为 3 类，分别是类方法、实例方法和静态方法，其中实例方法用的是最多的。我们知道，实例方法的调用方式其实有 2 种，既可以采用类对象调用，也可以直接通过类名调用。

通常情况下，我们习惯使用类对象调用类中的实例方法。但如果想用类调用实例方法，不能像如下这样：

```python
class CLanguage:
    def info(self):
        print("我正在学 Python")
#通过类名直接调用实例方法
CLanguage.info()
#报错Error
#TypeError: info() missing 1 required positional argument: 'self'
```

其中，最后一行报错信息提示我们，调用 info() 类方式时缺少给 self 参数传参。这意味着，和使用类对象调用实例方法不同，通过类名直接调用实例方法时，Python 并不会自动给 self 参数传值。

想想也应该明白，self 参数需要的是方法的**实际调用者**（是类对象），而这里只提供了类名，当然无法自动传值。

因此，如果想通过类名直接调用实例方法，就必须手动为 self 参数传值。例如修改上面的代码为：

```python
class CLanguage:
    def info(self):
        print("我正在学 Python")
#通过类名直接调用实例方法
clang = CLanguage()
CLanguage.info(clang)
#我正在学 Python
```

可以看到，通过手动将 clang 这个类对象传给了 self 参数，使得程序得以正确执行。实际上，这里调用实例方法的形式完全是等价于 clang.info()。

值得一提的是，上面的报错信息只是让我们手动为 self 参数传值，但并没有规定必须传一个该类的对象，其实完全可以任意传入一个参数，例如：

```Python
class CLanguage:
    def info(self):
        print(self,"我正在学 Python")
#通过类名直接调用实例方法
clang = CLanguage()
CLanguage.info(1)
#1 我正在学 Python
```

可以看到，1 这个字符串传给了 info() 方法的 self 参数。显然，无论是 info() 方法中使用 self 参数调用其它类方法，还是使用 self 参数定义新的实例变量，胡乱的给 self 参数传参都将会导致程序运行崩溃。

```Python
class CLanguage:
    def info(self):
        self.name = 1
        print(self,"我正在学 Python")
#通过类名直接调用实例方法
clang = CLanguage()
CLanguage.info(1)
#AttributeError: 'int' object has no attribute 'name'
```

总的来说，Python 中允许使用类名直接调用实例方法，但必须手动为该方法的第一个 self 参数传递参数，这种调用方法的方式被称为“非绑定方法”。

* 用类的实例对象访问类成员的方式称为绑定方法，而用类名调用类成员的方式称为非绑定方法。

# 11 什么是描述符，Python描述符详解



