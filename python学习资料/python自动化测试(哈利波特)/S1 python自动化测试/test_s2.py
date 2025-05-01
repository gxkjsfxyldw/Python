import pytest
import requests
from jsonpath import jsonpath

class Testdata():
    def test_hogwartss_json(self):
        payload={
            'q':'热门',
            'limit': 1,
            'trem' :''
        }
        self.r=requests.get('http://ceshiren.hogwarts.ceshiren.com/search.json',params=payload)#直接访问它的json文件
        print(self.r.json())
        assert self.r.status_code==200
        print(jsonpath(self.r.json(),'$..name'))#打印所有的name
if __name__=="__main__":
    pytest.main()
