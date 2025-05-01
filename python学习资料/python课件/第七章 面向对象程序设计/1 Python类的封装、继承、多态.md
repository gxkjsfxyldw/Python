# 1 封装

“封装”就是将抽象得到的数据和行为(或功能)相结合，形成一个有机的整体(即类)；封装的目的是增强安全性和简化编程，使用者

不必了解具体的实现细节，而只是要通过外部接口，一特定的访问权限来使用类的成员。

## 1.1 把一个对象的属性和方法封装

```python
# 如果我们要定义学生jack如何定义？
name = 'jack'
age = 17
sex = '男'
```

这三个变量可以用来形容jack这个人（当然你也可以使用字典，列表去描述).但是我们用三个变量去形容这个人，有什么弊端？ 弊端：太零散，如果学生太多，需要有很多变量去描述 为了解决这个问题，因此才有了类。

```python
class Student():
    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex

one = Student('jack',17,'男') # 这里的one就相当于一个学生jack，所有的属性都封装到了one变量中。这里的Student类，相当于一个模板。只要给定它name，age，sex，它就能创建出一个学生对象。
two = Student('aaa',16,'男')
three = Student('bbb',15,'女')
four = Student('ccc',14,'男')
five = Student('ddd',13,'女')
print(f'姓名:{one.name}   年龄:{one.age}    性别:{one.sex}')
```

## 1.2 保护隐私

```python
class Student(object):

    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex


one = Student('plf',18,'男')
one.name = 'who'
one.age = -28
one.sex = '人妖'
print(f'姓名:{one.name}   年龄:{one.age}    性别:{one.sex}')
```

问题：我们在外部能随意访问到对象one的属性，并且随意修改，这样数据是不安全的，因为我们需要将属性隐藏起来。那我们应该如何去做了？

```python
class Student(object):

    def __init__(self,name,age,sex):
        self.__name = name
        self.__age = age
        self.__sex = sex

one = Student('plf',18,'男')

print(one._Student__name)   #特殊方法调用私有属性
print(one._Student__age)
print(one._Student__sex)

one._Student__age = 20	
print(one._Student__age)


rint(one.__name)       # 报错，无该属性
print(one.name)         # 报错，无该属性
```

此时发现，我们虽然不能使用`one.name`或者`__one.__name`访问到该属性。但是我们可使用`one._Studentage`访问到对象的`age`属性并且能修改。说明python在设置私有属性的时候，只是把属性的名字换成了其他的名字。

类中以_或者__的属性，都是私有属性，禁止外部调用。虽然我们可以通过特殊的手段获取到，并且赋值，但是最好不要这么做（约定俗成）

## 1.3 为私有属性建立访问接口

问题：现在我将name，age，sex设置为私有属性，但是我又想让他们通过我指定的接口去访问或者修改我的属性，应该如何实现了？

```python
class Student(object):

    def __init__(self,name,age,sex):
        self.__name = name
        self.__age = age
        self.__sex = sex
	
    def get_name(self):
        return self.__name


    def set_name(self,name):
        if len(name) > 1 :
            self.__name = name
        else:
            print("name的长度必须要大于1个长度")

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if age > 0 and age < 150:
            self.__age = age
        else:
            print("输入的年龄必须要大于0，小于150岁")

one = Student('plf',18,'男')

one.set_name('a')       # 通过自己设置接口，可以有效规避脏数据
print(one.get_name())       # 通过接口获取数据


one.set_age(-9)         # 通过自己设置接口，可以有效规避脏数据
print(one.get_age())    # 通过接口获取数据
```

这样我们就自定义了自己属性的接口，它的好处在于：规避脏数据

问题：使用接口设置获取数据 和 使用点方法（`one.name = 18` 或者`print(one.name`)）设置数据相比， 点方法使用更方便，我们有什么方法达到 既能使用点方法，同时又能让点方法直接调用到我们的接口了？ 其他python已经帮我们实现了，让我们一起看一下吧！

```python
class Student(object):

    def __init__(self,name,age,sex):
        self.__name = name
        self.__age = age
        self.__sex = sex

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self,name):
        if len(name) > 1 :
            self.__name = name
        else:
            print("name的长度必须要大于1个长度")

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if age > 0 and age < 150:
            self.__age = age
        else:
            print("输入的年龄必须要大于0，小于150岁")


one = Student('plf',18,'男')

one.name = '张三'
print(one.name)

one.age = 170
print(one.age)
```

总结：

1. 使用 @property 装饰器时，接口名不必与属性名相同.
2. 凡是赋值语句，就会触发set方法。获取属性值，会触发get方法

# 2 继承

继承机制经常用于创建和现有类功能类似的新类，又或是新类只需要在现有类基础上添加一些成员（属性和方法），但又不想直接将现有类代码复制给新类。也就是说，通过使用继承这种机制，可以轻松实现类的重复使用。

```python
class People:
    def say(self):
        print("我是一个人，名字是：",self.name)
class Animal:
    def display(self):
        print("人也是高级动物")
#同时继承 People 和 Animal 类
#其同时拥有 name 属性、say() 和 display() 方法
class Person(People, Animal):
    pass
zhangsan = Person()
zhangsan.name = "张三"
zhangsan.say()
zhangsan.display()
#我是一个人，名字是： 张三
#人也是高级动物
```

可以看到，虽然 Person 类为空类，但由于其继承自 People 和 Animal 这 2 个类，因此实际上 Person 并不空，它同时拥有这 2 个类所有的属性和方法。

使用多继承经常需要面临的问题是，多个父类中包含同名的类方法。对于这种情况，Python 的处置措施是：根据子类继承多个父类时这些父类的前后次序决定，即排在前面父类中的类方法会覆盖排在后面父类中的同名类方法。

```python
class People:
    def __init__(self):
        self.name = People
    def say(self):
        print("People类",self.name)
class Animal:
    def __init__(self):
        self.name = Animal
    def say(self):
        print("Animal类",self.name)
#People中的 name 属性和 say() 会遮蔽 Animal 类中的
class Person(People, Animal):
    pass
zhangsan = Person()
zhangsan.name = "张三"
zhangsan.say()
#People类 张三
```

可以看到，当 Person 同时继承 People 类和 Animal 类时，People 类在前，因此如果 People 和 Animal 拥有同名的类方法，实际调用的是 People 类中的。

但凡事都有例外，我们可能会遇到这样一种情况，即子类从父类继承得来的类方法中，大部分是适合子类使用的，但有个别的类方法，并不能直接照搬父类的，如果不对这部分类方法进行修改，子类对象无法使用。针对这种情况，我们就需要在子类中重复父类的方法。

举个例子，鸟通常是有翅膀的，也会飞，因此我们可以像如下这样定义个和鸟相关的类：

```python
class Bird:
    #鸟有翅膀
    def isWing(self):
        print("鸟有翅膀")
    #鸟会飞
    def fly(self):
        print("鸟会飞")
class Ostrich(Bird):
    # 重写Bird类的fly()方法
    def fly(self):
        print("鸵鸟不会飞")
# 创建Ostrich对象
ostrich = Ostrich()
#调用 Ostrich 类中重写的 fly() 类方法
ostrich.fly()
#鸵鸟不会飞
```

显然，ostrich 调用的是重写之后的 fly() 类方法。

## 子类可以在继承父类方法的同时，对方法进行重构。

```python
class Fruit():
    def color(self):
        print("水果色彩丰富")

class Apple(Fruit):
    def color(self):
        super().color()
        print("苹果是红色的")

class Orange(Fruit):
    def color(self):
        super().color()
        print("橘子是橘色的")

apple = Apple()
orange = Orange()
apple.color()
orange.color()
#水果色彩丰富
#苹果是红色的
#水果色彩丰富
#橘子是橘色的
```



## 调用父类的构造方法

### 单继承

```Python
class Animal:
    def __init__(self,food):
        self.food = food
        print(self.food)

class People(Animal):
    def __init__(self,food,name):
        super().__init__(food)
        self.name = name
        print(self.name)

a = People('熟食','张三')
#熟食
#张三
```

但我们知道，Python 是一门支持多继承的面向对象编程语言，如果子类继承的多个父类中包含同名的类实例方法，则子类对象在调用该方法时，会优先选择排在最前面的父类中的实例方法。显然，构造方法也是如此。

```python
class People:
    def __init__(self,name):
        self.name = name
    def say(self):
        print("我是人，名字为：",self.name)
class Animal:
    def __init__(self,food):
        self.food = food
    def display(self):
        print("我是动物,我吃",self.food)
#People中的 name 属性和 say() 会遮蔽 Animal 类中的
class Person(People, Animal):
    pass
per = Person("zhangsan") 
per.say()       
#我是人，名字为： zhangsan
```

上面程序中，Person 类同时继承 People 和 Animal，其中 People 在前。这意味着，在创建 per 对象时，其将会调用从 People 继承来的构造函数。因此我们看到，上面程序在创建 per 对象的同时，还要给 name 属性进行赋值。

但如果运行`per.display()`行代码，Python 解释器会报如下错误：`AttributeError: 'Person' object has no attribute 'food'`

这是因为，从 Animal 类中继承的 display() 方法中，需要用到 food 属性的值，但由于 People 类的构造方法“遮蔽”了Animal 类的构造方法，使得在创建 per 对象时，Animal 类的构造方法未得到执行，所以程序出错。

针对这种情况，正确的做法是定义 Person 类自己的构造方法（等同于重写第一个直接父类的构造方法）。但需要注意，如果在子类中定义构造方法，则必须在该方法中调用父类的构造方法。

```python
super().__init__(self,...)
```

```python
class People:
    def __init__(self,name):
        self.name = name
        print(self.name)
    def say(self):
        print("我是人，名字为：",self.name)
class Animal:
    def __init__(self,food):
        self.food = food
        print(self.food)
    def display(self):
        print("我是动物,我吃",self.food)
class Person(People, Animal):
    #自定义构造方法
    def __init__(self,name,food):
        #调用 People 类的构造方法
        super().__init__(name)
        #super(Person,self).__init__(name) #执行效果和上一行相同
        #People.__init__(self,name)#使用未绑定方法调用 People 类构造方法
        #调用其它父类的构造方法，需手动给 self 传值
        Animal.__init__(self,food)
per = Person("zhangsan","熟食")
per.say()
per.display()
#zhangsan
#熟食
#我是人，名字为： zhangsan
#我是动物,我吃 熟食
```

# 3 多态

