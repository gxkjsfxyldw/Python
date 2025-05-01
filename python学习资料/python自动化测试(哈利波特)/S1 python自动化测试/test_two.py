#打开浏览器
#打开网页
#定位元素+输入账号密码
#点击登录
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

class Teststudent():
    def setup_method(self, method):
        self.driver=webdriver.Chrome()
        self.vars={}
    def teardown_method(self, method):
        self.driver.quit()
    def test_ceshiren(self):
        self.driver.get("http://jw.gxstnu.edu.cn/")
        self.driver.set_window_size(1600, 1027)
        zhanghao='192407117'
        mima='Lidawang666'
        self.driver.find_element(By.XPATH,'//*[@id="ul1"]/li[2]/input').send_keys(zhanghao)
        self.driver.find_element(By.XPATH, '//*[@id="ul1"]/li[3]/input').send_keys(mima)
        self.driver.find_element(By.XPATH, '//*[@id="ul1"]/li[5]').click()
        sleep(5)
        #print(self.driver.title)#教学一体化服务平台
        for handle in self.driver.window_handles:
            # 先切换到该窗口
            self.driver.switch_to.window(handle)
            # 得到该窗口的标题栏字符串，判断是不是我们要操作的那个窗口
            if '教学一体化服务平台' in self.driver.title:
                #如果是，那么这时候WebDriver对象就是对应的该该窗口，正好，跳出循环，
                print("找到")
                break
        sleep(5)