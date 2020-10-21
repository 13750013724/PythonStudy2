import shelve
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class TestDemo():
    def setup_method(self):
        options = Options()
        options.debugger_address = "127.0.0.1:9222"
        # self.driver = webdriver.Chrome(options=options)
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def teardown_method(self):
        self.driver.quit()

    def test_demo(self):
         # cookies = [
         #     {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False,
         #     'value': '1688850945867244'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst',
         #                                    'path': '/', 'secure': False,
         #                                    'value': 'bTlHVcHolJmolvKWGRqW3XHKhWD4McJ2G3MaLpGdzAZozM-HS2qi0at_3rgm78pntzu5IbV19iS7CYQn5yo55NKY9YR5EMCczK4WylhaKXZy6_E7HgcoGDhZdAhA2xRRCDtoJOcFxTJyj3diMFAZb3GPJ4Kq0fjES_-WgMNui2qlOTsi4H0YUw0qJGfuqAZeQdnXgCjTZC1qMEaTL1DBaxMXCdKZICYUocWmfftct-Kqx2OP_6tCdlPpND2TG6G7wUwgDSraFI0i-ccf7CEJWA'}, {
         #        'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False,
         #        'value': '1688850945867244'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False,
         #                                       'name': 'wxpay.corpid', 'path': '/', 'secure': False,
         #                                       'value': '1970324942165816'}, {'domain': '.work.weixin.qq.com',
         #                                                                      'httpOnly': True, 'name': 'wwrtx.sid',
         #                                                                      'path': '/', 'secure': False,
         #                                                                      'value': 'nvL6dpp-cnwgvtYtkG8FQTg4qDqdbgkGFmqKPf7UVG7cWq5arM3SiMc2fhvjAOXn'}, {
         #        'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False,
         #        'value': '38702242481026807'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False,
         #                                        'name': 'wwrtx.d2st', 'path': '/', 'secure': False,
         #                                        'value': 'a7423274'}, {'domain': '.work.weixin.qq.com',
         #                                                               'httpOnly': True, 'name': 'wwrtx.ltype',
         #                                                               'path': '/', 'secure': False, 'value': '1'}, {
         #        'domain': 'work.weixin.qq.com', 'expiry': 1602943361, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/',
         #        'secure': False, 'value': '3lgp4bb'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True,
         #                                               'name': 'wwrtx.ref', 'path': '/', 'secure': False,
         #                                               'value': 'direct'}, {'domain': '.work.weixin.qq.com',
         #                                                                    'expiry': 1634399961, 'httpOnly': False,
         #                                                                    'name': 'Hm_lvt_9364e629af24cb52acc78b43e8c9f77d',
         #                                                                    'path': '/', 'secure': True,
         #                                                                    'value': '1602861114,1602863962'}, {
         #        'domain': '.qq.com', 'expiry': 1602998241, 'httpOnly': False, 'name': '_gid', 'path': '/',
         #        'secure': False, 'value': 'GA1.2.553910074.1602861116'}, {'domain': '.work.weixin.qq.com',
         #                                                                  'expiry': 1605503843, 'httpOnly': False,
         #                                                                  'name': 'wwrtx.i18n_lan', 'path': '/',
         #                                                                  'secure': False, 'value': 'zh'}, {
         #        'domain': '.qq.com', 'expiry': 1665983841, 'httpOnly': False, 'name': '_ga', 'path': '/',
         #        'secure': False, 'value': 'GA1.2.1528581598.1599360411'}, {'domain': '.work.weixin.qq.com',
         #                                                                   'expiry': 1630896377, 'httpOnly': False,
         #                                                                   'name': 'wwrtx.c_gdpr', 'path': '/',
         #                                                                   'secure': True, 'value': '0'}]
         #

        # print(self.driver.get_cookies())
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame')
        db = shelve.open("cookies")
        # db['cookie'] = self.driver.get_cookies()
        cookies = db['cookie']
        for cookie in cookies:
            if "expiry" in cookie.keys():
                cookie.pop("expiry")
            self.driver.add_cookie(cookie)
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame')
        self.driver.find_element_by_id("menu_contacts").click()
        sleep(2)
        db.close()