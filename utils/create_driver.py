import os

from appium import webdriver
from appium.options.android import UiAutomator2Options
from dotenv import load_dotenv

load_dotenv()


def create_driver(app_activity=None):
    capabilities = {
        "platformName": os.getenv("PLATFORM_NAME") or "Android",
        "app": os.path.join(os.getcwd(), "app", "Ali.apk"),
        "automationName": "UIAutomator2",
        "deviceName": os.getenv("DEVICE_VERSION") or "Android",
        "lastScrollData": "null",
        "unicodeKeyboard": False,
        "resetKeyboard": False,
        "appPackage": "com.alibaba.aliexpresshd"
    }

    if app_activity:
        capabilities["appActivity"] = app_activity

    appium_server_url = "http://localhost:4723"
    capabilities_options = UiAutomator2Options().load_capabilities(capabilities)

    driver = webdriver.Remote(appium_server_url, options=capabilities_options)
    return driver
