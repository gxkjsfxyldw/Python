# # encoding = utf-8
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from time import sleep
#
#
# class Page(object):
#     """
#     基础类，用于页面对象类的继承
#     """
#     login_url = 'https://ceshiren.com/'
#     def __init__(self, driver, base_url=login_url):
#         self.base_url = base_url
#         self.driver = driver
#
#     def target_page(self):
#         return self.driver.current_url == self.base_url
#
#     def _open(self, url):
#         url = self.base_url
#         self.driver.get(url)
#         print(self.driver.current_url)
#
#     def open(self):
#         self._open(self.base_url)
#
#     def find_element(self, *loc):
#         return self.driver.find_element(*loc)
#
#
# class LoginPage(Page):
#
#     login_location = (By.XPATH, '//*[@class="panel clearfix"]/span/button[2]')  # 页面控件对象 ：点击登录按钮
#     username_loc = (By.XPATH, '//*[@id="credentials"]/div[1]/input')  # 页面控件对象：输入用户名的input控件
#     password_loc = (By.XPATH, '//*[@id="credentials"]/div[2]/input')  # 页面控件对象：输入密码的input控件
#     submit_loc = (By.XPATH, '//*[@class="modal-footer"]/button[1]')  # 页面控件对象：登陆按钮的button控件
#
#     def click_logio(self):
#         self.find_element(*self.login_location).click()
#
#     def input_username(self, username):
#         self.find_element(*self.username_loc).send_keys(username)
#
#     def input_password(self, password):
#         self.find_element(*self.password_loc).send_keys(password)  # 输入密码
#
#     def click_submitbutton(self):
#         self.find_element(*self.submit_loc).click()  # 点击登陆按钮
#
#
# def user_login(driver, username, password):
#     login_page = LoginPage(driver)
#     login_page.open()
#     sleep(5)
#     #driver.switch_to.frame(driver.find_element_by_xpath("//*[@id='loginDiv']/iframe"))
#     login_page.click_logio()
#     sleep(3)
#     login_page.input_username(username)
#     sleep(3)
#     login_page.input_password(password)
#     sleep(3)
#     login_page.click_submitbutton()
#
#
# def test_main():
#     driver = webdriver.Chrome()
#     try:
#         username = '2632711107'  # 登陆邮箱需要的真实账号
#         password = 'ldw2632711107'  # 登陆邮箱需要的真实密码
#         user_login(driver, username, password)  # 调用前面封装好的user_login方法
#         # sleep(3)  #  等待3秒
#         # driver.switch_to.default_content()  # 切换出iframe
#         # assert_string = driver.find_element_by_xpath("/html/body/div[1]/nav/div[1]/ul/li[1]/span[2]").text
#         # print(assert_string)
#         # assert (assert_string == '收 信')  # 断言关键字
#     finally:
#         driver.quit()  # 关闭浏览器窗口
#
#
# if __name__ == '__main__':
#     test_main()

# encoding = utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


class Page(object):
    """
    基础类，用于页面对象类的继承
    """
    login_url = 'https://ceshiren.com/'
    def __init__(self, driver, base_url=login_url):
        self.base_url = base_url
        self.driver = driver

    def target_page(self):
        return self.driver.current_url == self.base_url

    def _open(self, url):
        url = self.base_url
        self.driver.get(url)
        print(self.driver.current_url)

    def open(self):
        self._open(self.base_url)

    def find_element(self, *loc):
        return self.driver.find_element(*loc)


class LoginPage(Page):

    login_location = (By.XPATH, '//*[@class="panel clearfix"]/span/button[2]')  # 页面控件对象 ：点击登录按钮
    username_loc = (By.XPATH, '//*[@id="credentials"]/div[1]/input')  # 页面控件对象：输入用户名的input控件
    password_loc = (By.XPATH, '//*[@id="credentials"]/div[2]/input')  # 页面控件对象：输入密码的input控件
    submit_loc = (By.XPATH, '//*[@class="modal-footer"]/button[1]')  # 页面控件对象：登陆按钮的button控件

    def click_logio(self):
        self.find_element(*self.login_location).click()

    def input_username(self, username):
        self.find_element(*self.username_loc).send_keys(username)

    def input_password(self, password):
        self.find_element(*self.password_loc).send_keys(password)  # 输入密码

    def click_submitbutton(self):
        self.find_element(*self.submit_loc).click()  # 点击登陆按钮


def user_login(driver, username, password):
    login_page = LoginPage(driver)
    login_page.open()
    sleep(5)
    #driver.switch_to.frame(driver.find_element_by_xpath("//*[@id='loginDiv']/iframe"))
    login_page.click_logio()
    sleep(3)
    login_page.input_username(username)
    sleep(3)
    login_page.input_password(password)
    sleep(3)
    login_page.click_submitbutton()


def test_main():
    driver = webdriver.Chrome()
    try:
        username = '2632711107'  # 登陆邮箱需要的真实账号
        password = 'ldw2632711107'  # 登陆邮箱需要的真实密码
        user_login(driver, username, password)  # 调用前面封装好的user_login方法
        # sleep(3)  #  等待3秒
        # driver.switch_to.default_content()  # 切换出iframe
        # assert_string = driver.find_element_by_xpath("/html/body/div[1]/nav/div[1]/ul/li[1]/span[2]").text
        # print(assert_string)
        # assert (assert_string == '收 信')  # 断言关键字
    finally:
        driver.quit()  # 关闭浏览器窗口


if __name__ == '__main__':
    test_main()