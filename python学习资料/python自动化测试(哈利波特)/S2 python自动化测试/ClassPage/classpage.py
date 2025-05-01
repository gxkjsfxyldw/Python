# 操作对象类层
from selenium.webdriver.common.by import By
from Pages import page #基础类 导入基础类

class logpage(page.page): #登录类

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

class insertpage(page.page): #新建话题类

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
    #     self.find_element(*self.submit_six).click()  # 点击按钮 发布话题
    def click_seven(self):
        self.find_element(*self.submit_seven).click()  # 点击按钮
    def click_eight(self):
        self.find_element(*self.submit_nine).click()  # 点击按钮