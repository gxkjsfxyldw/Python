
import pytest
import requests
from jsonpath import jsonpath

class Testdata():
    # def test_get(self):
    #     self.r=requests.get('https://httpbin.testing-studio.com/get')#使用get接口发起访问
    #     print(self.r.status_code)
    #     #print(self.r.text)
    #     # print(self.r.json())
    #     assert self.r.status_code==200
    # def test_query(self): #get query请求参数构造
    #     payload={
    #         "level":1,
    #         "name":"sevenirby"
    #     }
    #     r=requests.get('https://httpbin.testing-studio.com/get',params=payload)#使用get接口发起请求，后面加上params参数
    #     print(r.text)
    #     assert r.status_code==200
    # def test_post_form(self):#post form表单请求参数构造
    #     payload={#构造url请求参数
    #         "level":1,
    #         "name":"sevenirby"
    #     }
    #     r=requests.post('https://httpbin.testing-studio.com/post',data=payload)#使用post接口发起请求
    #     print(r.text)
    #     assert r.status_code==200
    #
    # def test_header(self):#header构造请求
    #     self.r=requests.get('https://httpbin.testing-studio.com/get',headers={"h":"header dome"})#
    #    # print(self.r.status_code)
    #     print(self.r.text)
    #    # print(self.r.json())
    #     assert self.r.status_code==200
    #     assert self.r.json()['headers']["H"]=="header dome"

    # @pytest.mark.skip()
    # def test_hogwartss_json(self):  # json接口相应断言
    #     self.r = requests.get('https://ceshiren.com/categories.json')  # 直接访问它的json文件
    #     print(self.r.text)
    #     assert self.r.status_code == 200
    #     assert self.r.json()['category_list']['categories'][0]['name'] == "开源项目"
    #     print(jsonpath(self.r.json(), '$..name'))  # 打印所有的name
    #     assert jsonpath(self.r.json(), '$..name')[0] == "开源项目"  # 使用jsonpath库进行断言，第一个参数是内容，第二个参数表达式 查找里面所有name [0]表示第一个
    #     # 一个.表示一层 ，两个..表示第二层下边的所有name
    #

    #@pytest.mark.skip()
    def test_hogwarts_json(self):#json接口相应断言
            self.r=requests.get('https://ceshiren.com/tag/精华帖.json')#
            #print(self.r.text)
            assert self.r.status_code==200
            #print(self.r.json())
            #print(self.r.json()['users'][1]['name'])
            assert self.r.json()['users'][1]['name']=='安伶儿'  #用这个好一点

if __name__ == "__main__":
    pytest.main()