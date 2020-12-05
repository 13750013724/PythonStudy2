import yaml
from appium import webdriver

from UI自动化测试框架.page.base_page import BasePage
from UI自动化测试框架.page.main import Main


class App(BasePage):
    _package = "com.xueqiu.android"
    _activity = ".view.WelcomeActivityAlias"

    def start(self):
        if  self._driver is None:
            caps = {}
            caps["platformName"] = "Android"
            caps["deviceName"] = "test"
            caps["appPackage"] = self._package
            caps["appActivity"] = self._activity
            caps["noReset"] = True
            # caps["udid"] = yaml.safe_load(open("../page/configuation.yaml"))['caps']['udid']
            #初始华driver
            self._driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        else:
            self._driver.start_activity(self._package,self._activity)

        self._driver.implicitly_wait(10)
        return self

    def main(self) -> Main:
        return Main(self._driver)