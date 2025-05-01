from pprint import pprint

import requests

url = "https://httpbin.testing-studio.com/cookies"
urls = "https://httpbin.testing-studio.com/get"

payload={

'q':'热门','limit':1,'page':2
}
headers = {
  'Cookie': '18269309661',

  'Accept': 'application/json',
  'discourse-Present': 'True',
  'discourse-Track-View': 'True',
  'X-Requested-With': 'XMLHttpRequest'
}
cookies = dict(cookies='18269309661')
response = requests.request("GET", url,cookies=cookies)

responses = requests.request("GET", urls,cookies=cookies,headers=headers,params=payload)

def test_a():
    print(response.text)
    print(responses.text)