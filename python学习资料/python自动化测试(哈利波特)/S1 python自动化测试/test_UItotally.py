from time import sleep
import pytest
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

class Testdata():
    def setup(self):#包括打开网页，调用登录
        self.driver=webdriver.Chrome()
        self.driver.implicitly_wait(30)

        self.driver.get('https://ceshiren.com/')
        self.driver.set_window_size(1920,1080)
        self.driver.find_element_by_xpath('//*[@class="panel clearfix"]/span/button[2]').click()

        self.driver.find_element_by_xpath('//*[@id="credentials"]/div[1]/input').send_keys('mr_li')
        self.driver.find_element_by_xpath('//*[@id="credentials"]/div[2]/input').send_keys('ldw2632711107')

        self.driver.find_element_by_xpath('//*[@class="modal-footer"]/button[1]').click()

    def teardowm(self):#关闭网页
        self.driver.quit()

    #@pytest.mark.skip()
    def test_operation_click(self):#操作网页的点击UI
        #Action = ActionChains(self.driver)#滑动鼠标
        #for i in range(7):
        #Action.move_to_element_with_offset(self.driver, 0, 0).perform()     #鼠标移动到某个元素.perform()
        #sleep(10)
        for i in range(1, 8):
            sleep(2)
            i = i + 1
            x = '//*[@id="navigation-bar"]/li[' + str(i) + ']/a'
            # print(x)
            self.driver.find_element_by_xpath(x).click()
        sleep(2)
        self.driver.find_element_by_xpath('//*[@id="navigation-bar"]/li[2]/a').click()

        for i in range(1, 4):
            sleep(2)
            i = i + 2
            x = '//*[@class="topic-list-header"]/tr/th[' + str(i) +']'
            # print(x)
            self.driver.find_element_by_xpath(x).click()

    #@pytest.mark.skip()
    def test_operation_input(self):#操作网页的输入UI
        sleep(2)
        self.driver.find_element_by_xpath('//*[@id="create-topic"]').click()
        sleep(2)
        self.driver.find_element_by_xpath('//*[@id="reply-control"]/div[3]/div[2]/div/div/div[1]/div/div/div[1]/input').send_keys("selenium")
        self.driver.find_element_by_xpath('//*[@id="reply-control"]/div[3]/div[2]/div/div/div[1]/div[2]/textarea').send_keys("what's?")
        sleep(2)  # 上边的两句变量的动态生成的 必须要找到不变的因素

        self.driver.find_element_by_xpath('//*[@class="icons d-header-icons"]/li[1]/a').click()
        self.driver.find_element_by_xpath('//*[@class="search-input"]/input').send_keys("技术帖")
        self.driver.find_element_by_xpath('//*[@class="results"]/ul/li/a').click()
        sleep(2)
        self.driver.find_element_by_xpath('//*[@class="title"]/a/img').click()

    #@pytest.mark.skip()
    def test_operation_bounce(self):#操作网页的跳转UI
        sleep(3)
        self.driver.find_element_by_xpath('//*[@class="icons d-header-icons"]/li[1]/a').click()
        #self.driver.find_element(By.XPATH,'//*[@class="searching"]/a[1]').click()
        self.driver.find_element(By.XPATH,'//*[@class="searching"]/a').click()

        sleep(5)
        self.driver.find_element_by_xpath('//*[@class="search-bar"]/input').send_keys('技术贴')
        self.driver.find_element_by_xpath('//*[@class="search-bar"]/button').click()

    # @pytest.mark.skip()
    def test_operation_exit(self): #操作退出登录
        sleep(2)
        self.driver.find_element_by_xpath('//*[@id="current-user"]/a').click()
        self.driver.find_element_by_xpath('//*[@class="menu-links-row"]/div/button[4]').click()
        self.driver.find_element_by_xpath('//*[@class="menu-links-row"]/div/button[4]').click()
        self.driver.find_element_by_xpath('//*[@id="quick-access-profile"]/ul/li[7]/button').click()

if __name__ =='__main__':
    pytest.main(['-s',"test_UItotally.py"])