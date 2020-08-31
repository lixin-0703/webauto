# coding utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
import pytest
import allure
import configparser
from selenium.webdriver.chrome.options import Options

def init():
        # driver = webdriver.Firefox()  # 初始化一个火狐浏览器实例：driver
        #options = Options()  # 网上找到 你可以试试
        #options.binary_location = "D:\\tools\\chrome\\ChromePortable\\ChromePortable.exe"  # 这里是你指定浏览器的路径
        global driver


        config = configparser.ConfigParser()
        config.read(os.path.join(os.environ['HOME'], 'iselenium.ini'))

        try:
            using_headless = os.environ["using_headless"]
        except KeyError:
            using_headless = 'true'
            print('没有配置环境变量 using_headless, 按照有界面方式运行自动化测试')

        chrome_options = Options()
        if using_headless is not None and using_headless.lower() == 'true':
            print('使用无界面方式运行')
            chrome_options.add_argument("--headless")
        driver = webdriver.Chrome(chrome_options=chrome_options)
        driver.maximize_window()  # 最大化浏览器
        driver.get("http://pre.33reading.cn/#/index")  # 通过get()方法，打开一个url站点

@allure.feature("PC測試")
class Test_pc:

     @allure.story("登錄")
     def test_login(self):
          init()
          #在首页点击进入登录界面
          driver.find_element_by_xpath(".//*[@id='app']/div/section/header/div/div/div/div[2]/a[4]").click()
          time.sleep(3)
          #输入用户名find_element(By,CSS_Selector,".el-input__inner")
          #driver.find_element(By.CSS_SELECTOR,".el-input__inner").clear()
          driver.find_element_by_xpath(".//*[@id='app']/div/section/main/div/div[2]")
          driver.find_element_by_tag_name("form").find_element_by_xpath(".//div/div/div/input").clear()
          driver.find_element_by_tag_name("form").find_element_by_xpath(".//div/div/div/input").send_keys("15210881156")
          #输入密码
          driver.find_element_by_xpath(".//*[@id='app']/div/section/main/div/div[2]")
          driver.find_element_by_tag_name("form").find_element_by_xpath(".//div[2]/div/div/input").clear()
          driver.find_element_by_xpath(".//*[@id='app']/div/section/main/div/div[2]")
          driver.find_element_by_tag_name("form").find_element_by_xpath(".//div[2]/div/div/input").send_keys("123456")
          time.sleep(5)
          #点击登录
          driver.find_element_by_xpath(".//*[@id='app']/div/section/main/div/div[2]/form/div[3]/div/button").click()
          time.sleep(3)
          #登录成功后的校验  校验机构名称
          name = driver.find_element_by_xpath(".//*[@id='app']/div/section/main/div[2]/div[1]/div/h2").text
          if("您好：北京李子文化教育有限公司"==name):
                assert True
          print("机构名称",name)

     # @allure.story("企業資料")
     def test_cominfo(self):
          # 點擊企業資料
          driver.find_element_by_xpath(".//*[@id='app']/div/section/main/div[1]/ul/li[1]/a").click()
          name = driver.find_element_by_xpath(".//*[@id='app']/div/section/main/div[2]/div[2]/div[1]/div[1]/div/span/span/a").text
          if("企业资料"==name):
             assert True
          time.sleep(3)

     # @allure.story("学员管理")
     def test_stuinfo(self):
        # 点击学员管理
        driver.find_element_by_xpath(".//*[@id='app']/div/section/main/div[1]/ul/li[2]/a").click()
        name = driver.find_element_by_xpath(".//*[@id='app']/div/section/main/div[2]/div[2]/div[1]/div[1]/div/span/span/a").text
        if ("学员列表" == name):
            assert True
        time.sleep(3)

     # @allure.story("测试情况")
     def test_testinfo(self):
        # 点击测试情况
        driver.find_element_by_xpath(".//*[@id='app']/div/section/main/div[1]/ul/li[3]/a").click()
        name = driver.find_element_by_xpath(
                        ".//*[@id='app']/div/section/main/div[2]/div[2]/div[1]/div[1]/div/span/span/a").text
        if ("测试情况" == name):
                assert True
        time.sleep(3)

     # @allure.story("阅读情况")
     def test_readinfo(self):
        # 点击阅读情况
        driver.find_element_by_xpath(".//*[@id='app']/div/section/main/div[1]/ul/li[4]/a").click()
        name = driver.find_element_by_xpath(
                        ".//*[@id='app']/div/section/main/div[2]/div[2]/div[1]/div[1]/div/span/span/a").text
        if ("阅读列表" == name):
                assert True
        time.sleep(3)

     # @allure.story("订单情况")
     def test_orderinfo(self):
     # 点击阅读情况
        driver.find_element_by_xpath(".//*[@id='app']/div/section/main/div[1]/ul/li[5]/a").click()
        name = driver.find_element_by_xpath(
                        ".//*[@id='app']/div/section/main/div[2]/div[2]/div[1]/div[1]/div/span/span/a").text
        if ("订单列表" == name):
            assert True
        time.sleep(3)
        #进入订单详情
        driver.find_element_by_xpath(".//*[@id='app']/div/section/main/div[2]/div[2]/div[1]/div[2]/div/div[2]/div/div[1]/div[3]/table/tbody/tr[1]/td[10]/div/a").click()
        #验证界面出现订单详情字样
        title = driver.find_element_by_xpath(".//*[@id='app']/div/section/main/div[2]/div[2]/div[1]/div[1]/div/span[2]/span/a").text
        if ("订单详情" == title):
             assert True
        time.sleep(3)
        #关闭并退出浏览器
        driver.close()

if __name__ == "__main__":
    pytest.main(['test_sanreadingpc.py::Test_pc','-v'])