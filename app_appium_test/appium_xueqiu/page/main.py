import yaml
from selenium.webdriver.common.by import By

from app_appium_test.appium_xueqiu.page.base_page import BasePage
from app_appium_test.appium_xueqiu.page.market import Market


class Main(BasePage):
    def goto_market(self):
        # self.find(By.XPATH,"//*[@resource-id='android:id/tabhost']//*[@text='行情']").click()
        self.set_implicitly(10)
        self.steps("../page/main.yaml")
        self.set_implicitly(5)
        return Market(self._driver)