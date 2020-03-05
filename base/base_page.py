"""
PO文件基类
"""
from selenium.webdriver.support.wait import WebDriverWait


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver

    def find_element_func(self, location, timeout=5, poll=.5):
        """
        元素定位方法
        :param location: 元素定位信息
        :param timeout: 超时时长
        :param poll: 方法执行时间间隔
        :return: 元素对象
        """
        # 设置显示等待
        element = WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll). \
            until(lambda x: x.find_element(location[0], location[1]))
        # 返回目标元素
        return element

    def click_func(self, location):
        """元素点击方法"""
        # 定位目标元素
        element = self.find_element_func(location)
        # 调用点击方法
        element.click()

    def input_func(self, location, text):
        """元素输入方法"""
        element = self.find_element_func(location)  # 定位目标元素
        element.clear()  # 清空
        element.send_keys(text)  # 输入
