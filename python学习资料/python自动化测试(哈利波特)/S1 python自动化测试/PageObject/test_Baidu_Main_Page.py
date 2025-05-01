# encoding = utf-8
from selenium.webdriver.common.by import By
from time import sleep
class Page(object):
    """基础类，继承页面对象类"""
    login_url = "https://www.baidu.com"
    """初始化函数，定义timeout/driver/base_url"""
    def __init__(self, driver, base_url=login_url):
        self.base_url = base_url
        self.driver = driver
        self.timeout = 30
    """定义目标页面"""
    def target_page(self):
        return self.driver.current_url == self.base_url
    """定义打开网页的函数"""
    def open(self):
        url = self.base_url
        self.driver.get(url)
        print(self.driver.current_url)
    """定义获取元素基础方法"""
    def find_element(self, *loc):
        return self.driver.find_element(*loc)
class SearchPage(Page):
    """百度首页，页面对象类"""
    url = '/'
    input_loc = (By.NAME, "wd")
    search_button_loc = (By.ID, "su")
    """每个页面封装对应方法"""
    def input_search_string(self, search_string):
        self.find_element(*self.input_loc).send_Keys(search_string) #输入要检索的字符串

    def click_search_button(self):
        self.find_element(*self.search_button_loc).click() #点击百度按钮
    #定义检索字符串函数
def search_string(driver, string):
    search_Page = SearchPage(driver)
    search_Page.open()
    search_Page.input_search_string(string)
    sleep(3)
    search_Page.click_search_button()

