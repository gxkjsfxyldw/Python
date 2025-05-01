# 主要操作逻辑层

from time import sleep
from ClassPage import classpage #类对象包 导入类对象

def opreation_log(driver,account,password): #操作流程函数 登录操作

    input_page = classpage.logpage(driver)  #实例化操作对象
    input_page.action_open()  # 打开网站
    #***先登录在操作***#
    input_page.click_log()
    input_page.insert_account(account)
    input_page.insert_password(password)
    input_page.click_confirm()
    sleep(5)

def opreation_comment(driver,data1,data2):  # 操作流程函数 话题发布操作
    #****调用方法进行操作网站****#
    isnert_page=classpage.insertpage(driver)
    isnert_page.click_one()
    sleep(2)
    isnert_page.insert_data1(data1)
    isnert_page.click_tow()
    isnert_page.click_three()
    isnert_page.click_four()
    isnert_page.click_five()
    isnert_page.insert_data2(data2)
    sleep(5)
    #isnert_page.click_six()
    isnert_page.click_seven()
    isnert_page.click_eight()
    sleep(5)

