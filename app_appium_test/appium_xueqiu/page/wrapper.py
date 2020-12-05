from selenium.webdriver.common.by import By


def handle_black(func):
    def wrapper(*args,**kwargs):
        from app_appium_test.appium_xueqiu.page.base_page import BasePage
        # 弹框处理的列表
        _black_list = [
            (By.XPATH,"//*[@resource-id='com.xueqiu.android:id/action_search']"),
            (By.XPATH, "//*[@text='确认']"),
            (By.XPATH, "//*[@text='下次再说']"),
            (By.XPATH, "//*[@text='确定']")
        ]
        _max_num = 3
        _error_num = 0
        instance:BasePage = args[0]

        try:
            element = func(*args, **kwargs)
            # 找到之前_error_num 归0
            _error_num = 0
            # 隐式等待恢复原来的等待
            instance._driver.implicitly_wait(10)
            return element

        except Exception as e:
            # 出现异常，将隐式等待设置小一点，快速的处理弹框
            instance._driver.implicitly_wait(1)
            # 判断异常处理的次数
            if _error_num > _max_num:
                raise e
            _error_num += 1
            # 处理黑名单里面的弹框
            for ele in _black_list:
                elelist = instance.finds(*ele)
                if len(elelist ) >0:
                    elelist[0].click()
                    # 处理完弹框，将再去查找目标元素
                    return wrapper(*args ,**kwargs)
            raise e

    return wrapper