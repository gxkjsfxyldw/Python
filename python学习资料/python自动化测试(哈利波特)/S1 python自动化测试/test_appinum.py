
from appium import webdriver

desire_cap={
  "platformName": "android",
  "deviceName": "127.0.0.1:7555",
  "appPackage": "com.xueqiu.android",
  "appActivity": ".view.WelcomeActivityAlias"
}

driver=webdriver.Remote("http://127.0.0.1:4723/wd/hub",desire_cap)
driver.implicitly_wait(60)

el5 = driver.find_element_by_id("com.xueqiu.android:id/tv_search")
el5.click()
driver.implicitly_wait(20)
el6 = driver.find_element_by_id("com.xueqiu.android:id/search_input_text")
el6.click()
driver.implicitly_wait(20)
el6.send_keys("alibaba")
el6.click()
driver.implicitly_wait(20)
el7 = driver.find_element_by_id("com.xueqiu.android:id/search_input_text")
el7.click()
driver.implicitly_wait(20)
el8 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[1]")
el8.click()