from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

class Testdata():
    def setup_method(self):
        self.driver=webdriver.Chrome()
        self.driver.implicitly_wait(10)
    def teardown_method(self):
        self.driver.quit()
    def test_second(self):
        try:
            self.driver.get("http://ceshiren.hogwarts.ceshiren.com/search?expanded=true")
            self.driver.set_window_size(1024, 1080)
            self.driver.find_element(By.XPATH, '//*[@class="search-bar"]/input').send_keys("热门")
            self.driver.find_element(By.XPATH, '//*[@class="search-bar"]/button').click()
            sleep(5)
            # assert_string = driver.find_element(By.XPATH, '//*[@id="ember58"]/h3').text
            # print(assert_string)
            # assert (assert_string != '找不到结果。')  # 断言关键字
            # 断言关键字
            assert_string = self.driver.find_element(By.XPATH, '//*[@class="search-results"]/div/div[2]/h3').text
            print(assert_string)
            assert (assert_string != '找不到结果。')  # 断言关键字
        finally:
            self.driver.quit()  # 关闭浏览器窗口
