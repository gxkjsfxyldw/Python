import pytest
import requests
from pprint import pprint
class Testdata():
    def test_query(self):
        payload={
            'q': '热门',
            'limit': 1
        }
        headers = {
            'Cookie': '18269309661',
            'Host': 'ceshiren.hogwarts.ceshiren.com',
            'Accept': 'application/json',
            'discourse-Present': 'True',
            'discourse-Track-View': 'True',
            'X-Requested-With': 'XMLHttpRequest'
        }
        self.r=requests.get('http://ceshiren.hogwarts.ceshiren.com/search',headers=headers,params=payload)
        #self.r=requests.get('https://ceshiren.com/search',headers=headers,data=payload)
        #print(self.r.text)
        pprint(self.r.headers)
        assert self.r.status_code==200

if __name__=="__main__":
    pytest.main()