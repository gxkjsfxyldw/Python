from pprint import pprint
import pytest
import requests
from pprint import pprint
class Testdata():

    data = [('mr_li', 'ldw2632711107')]
    case = ['case1']
    @pytest.mark.parametrize('a,b', data, ids=case) #参数化

    def test_post_form(self,a, b):  # post form表单请求参数构造
        payload = {  # 构造url请求参数
            'username': a,
            'password': b
        }
        headers = {
            'content-type': 'application/x-www-form-urlencoded'
        }
        # body={
        #
        # }
        # Content-Type:application/json 传参数 json=body
        #verify=False 忽略SSL验证
        self.responser = requests.post('https://ceshiren.com/login', headers=headers,data=payload,verify=False)  # 使用post接口发起请求
        #print(self.responser.text)
        #pprint(self.responser.headers)
        assert self.responser.status_code == 200

if __name__=="__main__":
    pytest.main()