import pytest
from appium import webdriver

class TestDW():
    def setup(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0'
        desired_caps['deviceName'] = '127.0.0.1:7555'
        # com.android.settings/com.android.settings.Settings
        desired_caps['appPackage'] = 'com.xueqiu.android'
        desired_caps['appActivity'] = 'com.xueqiu.android.common.MainActivity'
        desired_caps['unicodeKeyBoard']='ture'#将接收中文输入框
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(60)  # 隐式等待  等待网页响应
    def teardown(self):
        self.driver.quit()
    def test_search(self):
        '''
        设计一条测试案例如下：
        1.打开 雪球 app
        2.点击搜索输入框
        3.向搜索输入框输入“阿里巴巴”
        4.在搜索结果里边选择 “阿里巴巴” ，然后进行点击
        5.获取这只香港阿里巴巴的股价，并判断这只股价的价格>=200
        '''
        self.driver.find_element_by_id("com.xueqiu.android:id/tv_search").click()
        self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys("阿里巴巴")
        #self.driver.find_element_by_xpath("//*[@resource-id='com.xueqiu.android:id/code' and @text='BABA']").click()
        resoult=float(self.driver.find_element_by_id("com.xueqiu.android:id/current_price").text)
        #print("resoult")
        assert resoult>100
        print("搜索测试用例")

if __name__=="__main__":
    pytest.main()