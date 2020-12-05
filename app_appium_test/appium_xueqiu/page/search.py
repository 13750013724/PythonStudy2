import yaml
from selenium.webdriver.common.by import By

from app_appium_test.appium_xueqiu.page.base_page import BasePage


class Search(BasePage):
    def search(self,name):
        # self.find(By.XPATH,'//*[@resource-id="com.xueqiu.android:id/search_input_text"]').send_keys("alibaba")
        # self.find(By.XPATH,'//*[@text="BABA"]').click()
        # self.find(By.XPATH,
        #           f'//*[contains(@resource-id,"stock_item_container")]//*[@text="{name}"]/../..//*[@text="加自选"]').click()
        self._params["name"] = name
        self.steps("../page/search.yaml")

    def add(self,name):
        self._params["name"] = name
        self.steps("../page/search.yaml")

    def is_choose(self,name):
        self._params["name"] = name
        return self.steps("../page/search.yaml")
        # eles = self.finds(By.XPATH,f'//*[contains(@resource-id,"stock_item_container")]//*[@text="{name}"]/../..//*[@text="已添加"]')
        # return len(eles)>0

    def reset(self,name):
        self._params["name"] = name
        return self.steps("../page/search.yaml")
