
import pytest
import requests

class Testdata():

    #@pytest.mark.skip
    def test_query_1(self):# get请求参数构造  网页的多种get请求
        payload={
            'q':'技术帖'
        }
        self.driver=requests.get("https://ceshiren.com/search/query",params=payload)
        #print(self.driver.status_code)
        assert self.driver.status_code==200

    #@pytest.mark.skip
    def test_query_2(self):# get请求参数构造  网页的多种get请求
        payload={
            "q":1,
            "page":1
        }
        self.driver=requests.get("https://ceshiren.com/search",params=payload)
        #print(self.driver.status_code)
        assert self.driver.status_code == 200

    #@pytest.mark.skip
    def test_json_1(self):# json请求
        self.driver=requests.get('https://ceshiren.com/tag/精华帖.json')
        #print(self.driver.status_code)
        #print(self.driver.json())
        assert self.driver.status_code == 200

    #@pytest.mark.skip
    def test_json_2(self):# json请求
        #self.driver=requests.get('https://ceshiren.com/new.json')#new是要建立的登录之前的
        self.driver = requests.get('https://ceshiren.com/top.json')
        #print(self.driver.json())
        assert self.driver.status_code == 200

    #@pytest.mark.skip
    def test_post_from(self):#post form表单请求参数构造  登录接口自动化测试
        paylod={
            "username": "mr_li",
            "password": "ldw2632711107",
        }
        self.driver=requests.post("https://ceshiren.com/login",data=paylod,allow_redirects=False)
        #print(self.driver.status_code)
        assert self.driver.status_code == 302

    def test_post_from_2(self):#post form表单请求参数构造  登录接口自动化测试
        paylod={
            "account": "LCuser_R7029S",
            "password": "666666"
        }                       #力扣
        self.driver=requests.post("https://www.lintcode.com/api/accounts/signin/",data=paylod,allow_redirects=False)
        #print(self.driver.status_code)
        assert self.driver.status_code == 200


if __name__=="__main__":
    pytest.main()