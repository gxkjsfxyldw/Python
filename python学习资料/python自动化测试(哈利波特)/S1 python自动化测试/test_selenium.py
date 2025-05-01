#
# from asyncio import sleep
# from selenium import webdriver  #导入selenium包
#
# def test_selenium():#函数
#     driver=webdriver.Chrome()#创建一个Chrome的实例，Chrome（）会从环境变量中寻找浏览器驱动
#     driver.get("https://www.gxstnu.edu.cn/")#打开此浏览器的地址
#
#     sleep(5)#等待5秒
#     driver.quit()#关闭网页
#
# if __name__ == "__main__":#入口函数
#     test_selenium()
#
############################################################
from time import sleep
from selenium import webdriver  # 导入selenium包
from selenium.webdriver.common.by import By

class TestData():
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)  # 隐式等待  等待网页响应
        self.vars = {}
    def teardown_method(self, method):
        self.driver.quit()
    def test_ceshiren(self):
        self.driver.get("https://ceshiren.com/")
        self.driver.set_window_size(1600, 1027)

        self.driver.find_element(By.XPATH, '//*[@class="header-buttons"]/button[2]/span').click()#LINK_TEXT直接可以定位网页上面 热门这个名称的元素
        username = 'mr_li'  # qq号码
        password = 'ldw263271117'  # qq密码
        self.driver.find_element(By.XPATH, '//*[@id="credentials"]/div[1]/input[1]').send_keys(username)  # 输入账号
        self.driver.find_element(By.XPATH, '//*[@id="credentials"]/div[2]/input[1]').send_keys(password)  # 输入密码
        self.driver.find_element(By.XPATH, '//*[@id="login-button"]/span').click()  # 点击登录

        sleep(5)#等待网页响应
        self.driver.current_window_handle#刷新网页后 下面重新查找元素
        #这一句会切换到新url对象，如果不写这句，浏览器对象会去原来url页面中，
        #找元素操作，这时候我们希望操作的元素找不到就会报错。
        #self.driver.find_element(By.XPATH, '//*[@id="navigation-bar"]/li[3]/a').click()


########################################################
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# def test_search():
#     driver=webdriver.Chrome()
#     driver.implicitly_wait(5)#隐式等待
#
#     driver.get("https://www.baidu.com")#打开相应网址
#
#
#     driver.find_element(By.CSS_SELECTOR,"#kw").send_keys("广西科技师范学院")#输入框搜索内容：广西科技师范学院
#     #find element查找元素  By.ID查找方式是用ID 找到#kw的这个元素  send_keys进行输入操作
#     driver.find_element(By.CSS_SELECTOR,"#su").click()#点击按钮
#     # find element查找元素  By.ID查找方式是用ID 找到#su的这个元素  click() 点击按钮操作
#     result=driver.find_element(By.CSS_SELECTOR,"result:nth-child(2)>h3>a?em").text#找到要查找的内容
#     # CSS_SELECTOR 表示使用 CSS样式进行定位，还可以使用XPATH进行定位 找到result这个元素 里边nth-child(2)第二子元素进行输入操作
#     assert  "广西科技师范学院" in result
#
#
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# class Testwait:
#     def setup(self):
#         self.driver=webdriver.Chrome()
#         self.driver.get("https://www.baidu.com/")
#     def test_wait(self):
#         self.driver.find_element(By.CSS_SELECTOR,"[id=kw]").send_keys("广西科技师范学院")
#         self.driver.find_element(By.ID,'su').click()
#






