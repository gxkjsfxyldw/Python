import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

class page(object):#基础类  对象库层

    #url = 'http://ceshiren.hogwarts.ceshiren.com/search?expanded=true'
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

class logpage(page): #登录类   对象库层

    submit_log = (By.XPATH, '//*[@class="panel clearfix"]/span/button[2]')  # 页面控件对象：按钮的button控件
    input_account = (By.XPATH, '//*[@id="credentials"]/div[1]/input')  # 页面控件对象：输入的input控件
    input_password = (By.XPATH, '//*[@id="credentials"]/div[2]/input')  # 页面控件对象：输入的input控件
    submit_confirm = (By.XPATH, '//*[@class="modal-footer"]/button[1]')  # 页面控件对象：按钮的button控件
    def click_log(self):
        self.find_element(*self.submit_log).click()  # 点击按钮
    def insert_account(self, account):
        self.find_element(*self.input_account).send_keys(account)  # 输入数据
    def insert_password(self, password):
        self.find_element(*self.input_password).send_keys(password)  # 输入数据
    def click_confirm(self):
        self.find_element(*self.submit_confirm).click()  # 点击按钮

class insertpage(page): #新建话题类 对象库层

    input_one = (By.XPATH, '//*[@id="reply-control"]/div[3]/div[2]/div/div/div[1]/div/div/div[1]/input')  # 页面控件对象：输入的input控件
    input_tow = (By.XPATH, '//*[@id="reply-control"]/div[3]/div[2]/div/div/div[1]/div[2]/textarea')  # 页面控件对象：输入的input控件
    submit_one = (By.XPATH, '//*[@id="create-topic"]')  # 页面控件对象：按钮的button控件
    submit_tow = (By.XPATH, '//*[@id="reply-control"]/div[3]/div/div[1]/div[1]/div[1]/div[1]/div/div[2]/details')  # 页面控件对象：按钮的button控件
    submit_three = (By.XPATH, '//*[@id="reply-control"]/div[3]/div/div[1]/div[1]/div[1]/div[1]/div/div[2]/details/div/ul/li[17]')  # 页面控件对象：按钮的button控件
    submit_four = (By.XPATH, '//*[@id="reply-control"]/div[3]/div/div[1]/div[1]/div[1]/div[1]/div/details/summary')  # 页面控件对象：按钮的button控件
    submit_five = (By.XPATH, '//*[@id="reply-control"]/div[3]/div/div[1]/div[1]/div[1]/div[1]/div/details/div/ul/li[4]')  # 页面控件对象：按钮的button控件
    #submit_six = (By.XPATH, '//*[@id="reply-control"]/div[3]/div[3]/div/button')  # 页面控件对象：按钮的button控件
    submit_seven = (By.XPATH, '//*[@id="reply-control"]/div[3]/div[3]/div/a')  # 页面控件对象：按钮的button控件
    submit_nine = (By.XPATH, '//*[@class="modal-inner-container"]/div[4]/button[1]')  # 页面控件对象：按钮的button控件

    def insert_data1(self, data):
        self.find_element(*self.input_one).send_keys(data)  # 输入数据
    def insert_data2(self, data):
        self.find_element(*self.input_tow).send_keys(data)  # 输入数据
    def click_one(self):
        self.find_element(*self.submit_one).click()  # 点击按钮
    def click_tow(self):
        self.find_element(*self.submit_tow).click()  # 点击按钮
    def click_three(self):
        self.find_element(*self.submit_three).click()  # 点击按钮
    def click_four(self):
        self.find_element(*self.submit_four).click()  # 点击按钮
    def click_five(self):
        self.find_element(*self.submit_five).click()  # 点击按钮
    # def click_six(self):
    #     self.find_element(*self.submit_six).click()  # 点击按钮
    def click_seven(self):
        self.find_element(*self.submit_seven).click()  # 点击按钮
    def click_eight(self):
        self.find_element(*self.submit_nine).click()  # 点击按钮

def opreation_web(driver,account,password): #操作流程函数  逻辑层

    input_page = logpage(driver)  # 实例化操作对象
    input_page.action_open()  # 打开网站
    #***先登录在操作***#
    input_page.click_log()
    input_page.insert_account(account)
    input_page.insert_password(password)
    input_page.click_confirm()
    sleep(5)

    #****调用方法进行操作网站****#
    isnert_page=insertpage(driver)
    isnert_page.click_one()
    sleep(2)
    isnert_page.insert_data1("666")
    isnert_page.click_tow()
    isnert_page.click_three()
    isnert_page.click_four()
    isnert_page.click_five()
    isnert_page.insert_data2("999")
    sleep(5)
    #isnert_page.click_six()
    isnert_page.click_seven()
    isnert_page.click_eight()
    sleep(5)


data = [('mr_li','ldw2632711107')]
case=['case1']
@pytest.mark.parametrize('a,b',data,ids=case)
def test_one(a,b):  # 测试主体  业务层
    driver = webdriver.Chrome()
    driver.implicitly_wait(30)
    account=a
    password=b
    try:
        opreation_web(driver,account,password)
        # 断言关键字
        # assert_string = driver.find_element(By.XPATH, '//*[@class="search-results"]/div/div[2]/h3').text
        # print(assert_string)
        # assert (assert_string == '找不到结果。')  # 断言关键字
    finally:
        driver.quit()  # 关闭浏览器窗口

if __name__ == '__main__':
    pytest.main()