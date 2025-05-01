
class page(object):#基础类

    #url = 'http://ceshiren.hogwarts.ceshiren.com/search?expanded=true'
    #url = 'https://ceshiren.hogwarts.ceshiren.com/'
    url = 'https://ceshiren.com/'
    def __init__(self, driver, base_url=url):#初始化 定义网站的url
        self.base_url = base_url
        self.driver = driver

    def target_page(self): #定义目标页面
        return self.driver.current_url == self.base_url

    def opreation_open(self, url):#操作打开网站 open
        url = self.base_url
        self.driver.get(url)
        print(self.driver.current_url)

    def action_open(self):# 打开网站的方法 open
        self.opreation_open(self.base_url)

    def find_element(self, *location): #查找页面元素
        return self.driver.find_element(*location)