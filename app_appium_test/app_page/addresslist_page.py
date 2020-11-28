from appium.webdriver.common.mobileby import MobileBy

from app_appium_test.app_page.base_page import BasePage
from app_appium_test.app_page.member_invit import MemberInvite


class AddressList(BasePage):

    def add_member(self):
        self.find(MobileBy.XPATH, "//*[@text='添加成员']").click()
        return MemberInvite(self._driver)