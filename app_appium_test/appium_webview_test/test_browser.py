from appium import webdriver
from  time import sleep


class TestBrowser():
    def setup(self):
        des_caps = {
            'platformName':'android',
            'platformVersion':'6.0',
            # 'appPackage': 'com.android.browser',
            # 'appActivity': 'com.android.browser.BrowserActivity',
            'browserName':'Browser',
            #'browserName': 'Chrome',
            'noReset':True,
            #'deviceName':'emulator-5554',
            'deviceName': 'mumu',
            'chromedriverExecutable':'H:\Program Files\Python\Python38\chromedrivers\chromedriver_2.24.exe'
        }
        #chromedriverExecutable的路径需要完整路径
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",des_caps)
        self.driver.implicitly_wait(15)

    def teardown(self):
        self.driver.quit()

    def test_browser(self):
        self.driver.get("http://m.baidu.com")
        print(self.driver.contexts)
        contexts = self.driver.contexts
        # self.driver.switch_to.content(contexts[1])
        print(self.driver.current_context)
        # self.driver.switch_to.default_content('WEBVIEW_com.android.browser')
        #sleep(5)
        self.driver.find_element_by_id("index-kw").send_keys("appium")
        sleep(5)
        # self.driver.find_element_by_accessibility_id("百度一下").click()
        # #sleep(5)
        # self.driver.find_element_by_id("index-kw").send_keys("appium")
        # sleep(5)
        self.driver.find_element_by_id("index-bn").click()
        sleep(5)
