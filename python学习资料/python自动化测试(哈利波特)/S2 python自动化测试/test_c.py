from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


class page(object):#基础类

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


class loginpage(page): #页面对象类 操作网站元素 当driver传入的时候就开始初始化了

    login_location = (By.XPATH, '//*[@class="panel clearfix"]/span/button[2]')  # 页面控件对象 ：点击登录按钮
    username_location = (By.XPATH, '//*[@id="credentials"]/div[1]/input')  # 页面控件对象：输入用户名的input控件
    password_location = (By.XPATH, '//*[@id="credentials"]/div[2]/input')  # 页面控件对象：输入密码的input控件
    submit_location = (By.XPATH, '//*[@class="modal-footer"]/button[1]')  # 页面控件对象：登陆按钮的button控件

    def click_logio(self):
        self.find_element(*self.login_location).click() #点击登录窗口

    def insert_username(self, username):
        self.find_element(*self.username_location).send_keys(username)  # 输入账号

    def insert_password(self, password):
        self.find_element(*self.password_location).send_keys(password)  # 输入密码

    def click_submit(self):
        self.find_element(*self.submit_location).click()  # 点击登陆按钮


def opreation_login(driver, username, password): #主要操作流程

    #****调用方法进行操作网站****#

    login_page = loginpage(driver)          #实例化操作对象
    login_page.action_open()                #打开网站
    sleep(3)
    login_page.click_logio()                #点击网站的登录窗口
    sleep(3)
    login_page.insert_username(username)    #输入账号
    sleep(3)
    login_page.insert_password(password)    #输入密码
    sleep(3)
    login_page.click_submit()               #点击登录


def test_main():# 测试主体

    driver = webdriver.Chrome()
    try:
        username = 'mr_li'  # 登陆邮箱需要的真实账号
        password = 'ldw2632711107'  # 登陆邮箱需要的真实密码
        opreation_login(driver, username, password)  # 调用前面封装好的user_login方法
        sleep(10)  #  等待3秒
        # driver.switch_to.default_content()  # 切换出iframe
        assert_string = driver.find_element(By.XPATH, '//*[@class="icon"]/div/img').accessible_name
        print(assert_string)
        assert (assert_string == 'lidawang')  # 断言关键字
    finally:
        driver.quit()  # 关闭浏览器窗口

if __name__ == '__main__':
    test_main()