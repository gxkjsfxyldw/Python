import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

class page(object):#基础类

    url = 'http://ceshiren.hogwarts.ceshiren.com/search?expanded=true'

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


class objectpage(page): #页面对象类 操作网站元素 当driver传入的时候就开始初始化了

    input_location = (By.XPATH, '//*[@class="search-bar"]/input')  # 页面控件对象：输入的input控件
    submit_location = (By.XPATH, '//*[@class="search-bar"]/button')  # 页面控件对象：按钮的button控件
    def insert_tada(self, data):
        self.find_element(*self.input_location).send_keys(data)  # 输入数据
    def click_submit(self):
        self.find_element(*self.submit_location).click()  # 点击搜索按钮


def opreation_main(driver,keyinput): #主要操作流程
    #****调用方法进行操作网站****#
    input_page = objectpage(driver)          #实例化操作对象
    input_page.action_open()                #打开网站
    sleep(3)
    input_page.insert_tada(keyinput)
    sleep(5)
    input_page.click_submit()
    sleep(5)

def opreation_opreation(driver,keyinput): #主要操作流程
    #****调用方法进行操作网站****#
    input_page = objectpage(driver)          #实例化操作对象
    input_page.action_open()                #打开网站
    sleep(3)
    input_page.insert_tada(keyinput)
    sleep(5)
    input_page.click_submit()
    sleep(5)


@pytest.mark.skip()
def test_one():# 测试主体

    driver = webdriver.Chrome()
    driver.implicitly_wait(30)
    try:
        opreation_opreation(driver,'精华帖')
     # 断言关键字
    finally:
        assert_string = driver.find_element(By.XPATH, '//*[@id="ember58"]/h3').text
        print(assert_string)
        assert (assert_string != '找不到结果。')  # 断言关键字
        driver.quit()  # 关闭浏览器窗口

@pytest.mark.skip()
def test_tow():  # 测试主体

    driver = webdriver.Chrome()
    driver.implicitly_wait(30)
    try:
        opreation_opreation(driver,'广西科技师范学院')
        # 断言关键字
        assert_string = driver.find_element(By.XPATH, '//*[@id="ember58"]/h3').text
        print(assert_string)
        assert (assert_string == '找不到结果。')  # 断言关键字
    finally:
        driver.quit()  # 关闭浏览器窗口

def test_three():  # 测试主体

    driver = webdriver.Chrome()
    driver.implicitly_wait(30)
    try:
        opreation_opreation(driver,'')
        # 断言关键字
        assert_string = driver.find_element(By.XPATH, '//*[@id="ember58"]/h3').text
        print(assert_string)
        assert (assert_string == '找不到结果。')  # 断言关键字
    finally:
        driver.quit()  # 关闭浏览器窗口


if __name__ == '__main__':
    pytest.main()