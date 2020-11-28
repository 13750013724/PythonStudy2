from appium.webdriver.common.mobileby import MobileBy

from app_appium_test.app_page.base_page import BasePage


class ContactAdd(BasePage):

    def input_name(self):
        nameelement = self.find(MobileBy.XPATH, "//*[@text='姓名　']/..//*[@text='必填']")
        nameelement.send_keys("测试name1")
        return self

    def set_gender(self):
        self.find(MobileBy.ID, "efz").click()
        self.find(MobileBy.XPATH, "//*[@text='女']").click()
        return self

    def input_phonenum(self):
        phonenum_element = self.find(MobileBy.XPATH,
                                                    "//*[@text='手机　']/..//*[contains(@class,'EditText')]")
        phonenum_element.send_keys("18712345678")
        return self

    def click_save(self):
        from app_appium_test.app_page.member_invit import MemberInvite
        self.find(MobileBy.ID, "com.tencent.wework:id/hvk").click()
        return MemberInvite(self._driver)