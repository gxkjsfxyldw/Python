# 此代码是来使用百度搜索引擎，搜索“58同城”，并本页刷新进入58同城页面
import time

from selenium import webdriver
#
driver = webdriver.Chrome()
# 请求百度 链接
url = 'http://www.baidu.com'

# 执行操作，打开浏览器输入url
driver.get(url)

# 定位页面表单
ele_kw = driver.find_element_by_id('kw')
# 向表单中填入数据
ele_kw.send_keys('58同城')
# 定位页面搜索按钮
ele_su = driver.find_element_by_id('su')
# 延时几秒确保页面加载完毕
time.sleep(3)
sreach_window=driver.current_window_handle
# 点击“百度一下”按钮
ele_su.click()

# 延时几秒确保页面加载完毕
time.sleep(3)
# 找到“58同城”官网的xpath，点击该标签进入
tongcheng = driver.find_element_by_xpath('//*[@class="wbrjf67"]/a[1]').click()

# 页面全加载完毕后会关闭浏览器
driver.close()