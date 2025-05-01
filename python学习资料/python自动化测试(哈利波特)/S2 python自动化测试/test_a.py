# import pytest
#
# def func(x):
#     return x+1
#
# def test_answer():
#     assert func(3)==5
#
# def test_answer1():
#     assert func(4)==5
#
#
# class TestData:
#     def test_a(self):
#         print("a")
#     def test_b(self):
#         print("b")
#     def c(self):
#         print("c")
#
# if __name__ == '__main__': #python函数入口
#    # pytest.main(['test_a.py::test_answer','-v'])#-v 表示详细的数据
#     pytest.main()
# import pytest
# def func(x):
#     return x+1
# @pytest.mark.parametrize('a,b',[# pytest 参数化设置
#     (1,3),
#     (9,10),
#     ('a','b')
# ])
# def test_answer(a,b):
#     assert func(a)==b
#
# def test_answer1():
#     assert func(4)==5
#
# class TestData:
#     def test_a(self):
#         print("a")
#     def test_b(self):
#         print("b")
# if __name__ =='__main__':
#     pytest.main(['test_a.py::test_answer', '-v'])  # 指定进行测试的的文件， -v 表示详细的数据

##############################################
# import pytest
# class TestMethod:
#     def test_a(self):#测试单元a
#         print("----a----")
#     def test_b(self):
#         print("----b----")#测试单元b
#     def setup(self):#第二高优先级
#         print("---setup---")
#     def teardown(self):#倒数第二低优先级
#         print("---teardown---")
#     def setup_class(self):#最高优先级
#         print("---setup_class---")
#     def teardown_class(self):#最低优先级
#         print("---teardown_class---")
#
# if __name__=="__main__":
#     pytest.main(["-s","test_a.py"])

############################################
# import pytest
# class TestMethod:
#    # @pytest.mark.skip(reason="累了")#skip表示直接忽略以下的测试
#    # @pytest.mark.skipif(1>2,reason="失败")#skipif表示通过判断条件来决定是否通过测试
#     def test_a(self):
#         print("---test_a---")
#     def test_b(self):
#         print("---test_b---")
#
# if __name__=="__main__":
#     pytest.main(["-s","test_a.py"])
#

import pytest
#class TestMethod:
    # @pytest.mark.parametrize("name",["lidawang,dawangli"])#多个参数化
    # def test_a(self,name):
    #     print("---a----")
    #     print(name)
    #     assert 1==2
    # @pytest.mark.parametrize(("name","lidawang"),[('da','1'),('wang','2')])#使用元组来定义参数化
    # def test_b(self,name,lidawang):
    #     print("---b---")
    #     print(name)
    #     print(lidawang)

# @pytest.mark.parametrize('sername,password', [['小明', '18']])  # 多个参数化
# def test_main(sername, password):  # 测试主体
#     print(sername)
#
# if __name__=="__main__":
#     test_main()
import pytest
data = [('张三','男','23'),('李四','女','24'),('赵武','男','25')]
data1=['case1','case2','case3']
#需要按照某些条件或者数据进行入参时，可以按照这种方式
#'name,sex'表示入参的内容，data就是取值的列表，data1是值用例名称或标志
#data可以作为数据文件单独写一个文件
@pytest.mark.parametrize('name,sex,num',data,ids=data1)
def test_name(name,sex,num):
    print(type(name),type(sex),type(int(num)))
    print(name,sex,num)
