from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from test_selenium.selenium_wework_main.page.add_member import AddMember
from test_selenium.selenium_wework_main.page.base_page import BasePage


class Main(BasePage):
    _base_url = 'https://work.weixin.qq.com/wework_admin/frame'

    def goto_add_member(self):
        # click add member
        # sleep(2)
        # self.find(By.CSS_SELECTOR,'.index_service_cnt_itemWrap:nth-child(1)').click()
        self.find(By.ID,'menu_contacts').click()
        locator = (By.CSS_SELECTOR,'.js_has_member>div:nth-child(1)>a:nth-child(2)')
        # WebDriverWait(self._driver,10).until(expected_conditions.element_to_be_clickable(locator))
        self.wait_for_click(locator)
        self.find(By.CSS_SELECTOR,'.js_has_member>div:nth-child(1)>a:nth-child(2)').click()
        return AddMember(self._driver)