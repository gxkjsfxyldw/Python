#测试层
from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By

from Operation import opreation #页面操作包 导入页面操作函数

data = [('mr_li','ldw2632711107')]
case=['case1']
@pytest.mark.parametrize('accounts,passwords',data,ids=case)
@pytest.mark.skip
def test_one(accounts,passwords):  # 测试主体  业务层

    driver = webdriver.Chrome()
    driver.implicitly_wait(30)
    account=accounts
    password=passwords
    try:
        opreation.opreation_log(driver,account,password)# opreation_log 登录页面
        opreation.opreation_comment(driver,"666","999")# opreation_comment新建话题页面
        # 断言关键字
        # assert_string = driver.find_element(By.XPATH, '//*[@class="modal-inner-container"]/div[2]').text
        # print(assert_string)
        # assert (assert_string == '用户名、电子邮件或密码不正确')  # 断言关键字
    finally:
        driver.quit()  # 关闭浏览器窗口


data = [('mr_li','ldw2632711107'),('mr_li','ldw263271110'),('mr_l','ldw2632711107')]
datacase=['成功','密码错误','账号错误']
@pytest.mark.parametrize('accounts,passwords',data,ids=datacase)
def test_tow(accounts,passwords):  # 测试主体  业务层
    account=accounts
    password=passwords
    #print(account,password)
    driver = webdriver.Chrome()
    driver.implicitly_wait(30)

    try:
        opreation.opreation_log(driver,account,password)# opreation_log 登录页面
        # 断言关键字
        assert_string = driver.find_element(By.XPATH, '//*[@class="modal-inner-container"]/div[2]').text
        print(assert_string)
        if(assert_string!='用户名、电子邮件或密码不正确'):
            assert (assert_string != '用户名、电子邮件或密码不正确')
            # 断言关键字
        else:
            assert (assert_string == '用户名、电子邮件或密码不正确')
    finally:
        driver.quit()  # 关闭浏览器窗口

if __name__ == '__main__':
    pytest.main()