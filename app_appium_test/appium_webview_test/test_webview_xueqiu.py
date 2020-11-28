from appium import webdriver
from  time import sleep

from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.mobilecommand import MobileCommand
from selenium.webdriver.common.by import By


class TestBrowser():
    def setup(self):
        des_caps = {
            'platformName':'android',
            'platformVersion':'6.0',
            'appPackage': 'com.xueqiu.android',
            'appActivity': 'com.xueqiu.android.main.view.MainActivity',
            # 'browserName':'Browser',
            #'browserName': 'Chrome',
            'noReset':True,
            # 'deviceName':'emulator-5554',
            # 'deviceName': 'mumu',
            'deviceName':'192.168.237.101:5555',
            'chromedriverExecutable':'H:\Program Files\Python\Python38\chromedrivers\chromedriver_74.exe'
        }
        #chromedriverExecutable的路径需要完整路径
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",des_caps)
        self.driver.implicitly_wait(10)

    def teardown(self):
        self.driver.quit()
        # pass

    def test_webview(self):
        self.driver.find_element(MobileBy.XPATH,'//*[@text="交易"]').click()
        sleep(3)
        print(self.driver.contexts)
        # contexts = self.driver.contexts
        # self.driver.switch_to.content(contexts[1])
        self.driver.find_element(MobileBy.XPATH, '//*[@text="A股开户"]').click()
        sleep(2)
        print(self.driver.contexts)
        # self.driver.execute(MobileCommand.SWITCH_TO_CONTEXT, {"name": "WEBVIEW_com.xueqiu.android"})
        self.driver.switch_to.context(self.driver.contexts[-1])
        sleep(3)
        # print(self.driver.current_context)
        print(self.driver.page_source)
        self.driver.find_element(MobileBy.ID, 'phone-number').send_keys("11212555544")
        sleep(2)
        self.driver.find_element(MobileBy.ID,'code').send_keys("1234")
        sleep(2)#/html/body/div/div/div[5] body > div > div > div.form-wrap > div > div.btn-submit
        self.driver.find_element(MobileBy.CSS_SELECTOR,'body > div > div > div.form-wrap > div > div.btn-submit').click()
        # print(self.driver.window_handles)
        # self.driver.find_element(MobileBy.XPATH, '//*[@content-desc="输入11位手机号"]').send_keys("1111111411")
        # self.driver.find_element(MobileBy.XPATH, '//*[@content-desc="输入验证码"]').click()
        # self.driver.find_element(MobileBy.XPATH, '//*[@content-desc="输入验证码"]').send_keys('15155')
        sleep(5)
