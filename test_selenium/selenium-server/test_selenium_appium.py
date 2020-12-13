import sys
import os
# sys.path.append('H:\\python_pycharm\\PythonStudy')
# sys.path.append('H:\\python_pycharm\\PythonStudy\\venv\\Lib\\site-packages')
import yaml
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy


class TestApp():
    def setup(self):
            caps = {}
            caps["platformName"] = "Android"
            caps["deviceName"] = "127.0.0.1:7555"
            caps["udid"] = os.getenv("udid", None)
            # caps["udid"] = yaml.safe_load(open("../selenium-server/configuation.yaml"))['caps']['udid2']
            caps["appPackage"] = "com.xueqiu.android"
            caps["appActivity"] = ".view.WelcomeActivityAlias"
            caps["noReset"] = "true"
            # caps["skipServerInstallation"] = True
            # caps["skipDeviceInitialization"] = True

            self.driver = webdriver.Remote("http://192.168.3.4:4444/wd/hub",caps)

            self.driver.implicitly_wait(50)


    def teardown(self):
        self.driver.quit()

    def stop(self):
        pass

    def test_main(self):
        self.driver.find_element(MobileBy.XPATH,"//*[@resource-id='android:id/tabhost']//*[@text='行情']").click()

    # def test_main1(self):
    #     self.driver.find_element(MobileBy.XPATH, "//*[@resource-id='android:id/tabhost']//*[@text='行情']").click()
    #
    # def test_main2(self):
    #     self.driver.find_element(MobileBy.XPATH, "//*[@resource-id='android:id/tabhost']//*[@text='行情']").click()
    #
    # def test_main3(self):
    #     self.driver.find_element(MobileBy.XPATH, "//*[@resource-id='android:id/tabhost']//*[@text='行情']").click()