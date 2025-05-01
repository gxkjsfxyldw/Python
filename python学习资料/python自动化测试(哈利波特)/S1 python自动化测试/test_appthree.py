import pytest
from appium import webdriver

class Testdw():

    def setup(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0'
        desired_caps['deviceName'] = '127.0.0.1:7555'
        desired_caps['appPackage'] = 'com.eusoft.ting.en'#需要打开的软件包名 每日英语
        desired_caps['appActivity'] = 'com.eusoft.ting.ui.v2.TabActivityV2'#打开到每日英语软件的主页面
        desired_caps['unicodeKeyBoard']='ture'#将接收中文输入框
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(60)  # 隐式等待  等待网页响应
    def teardown(self):
        self.driver.quit()
    def test_action(self):
        pass


if __name__ == '__main__':
    pytest.main()
