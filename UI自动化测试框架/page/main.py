from selenium.webdriver.common.by import By

from UI自动化测试框架.page.base_page import BasePage


class Main(BasePage):
    def goto_search(self):
        # self.find(By.ID,'tv_banner').click()
        self.steps("../page/main.yaml")

    def goto_windows(self):
        self.find(By.ID,"post_status").click()
        # self.find(By.ID,"iv_close").click()
        self.find(By.ID,'tv_banner').click()


