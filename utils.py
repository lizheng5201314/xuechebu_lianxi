"""
驱动对象获取方法
"""
from appium import webdriver


def get_driver():
    """获取驱动对象方法"""
    # 获取驱动对象
    capabilities = {
        "platformName": "Android",  # 测试平台（Android、iOS）
        "platformVersion": "5.1.1",  # 测试系统版本
        "deviceName": "模拟器",  # 测试设备名称
        "appPackage": "com.bjcsxq.chat.carfriend",  # 待测应用的包名
        "appActivity": ".MainActivity",  # 待测应用的启动名
        # 输入中文设置
        "resetKeyboard": True,
        "unicodeKeyboard": True
    }
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=capabilities)
    return driver  # 添加函数返回值


if __name__ == '__main__':
    get_driver()  # 调试使用
