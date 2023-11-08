import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
import time
import os

def appium_options():
    current_directory = os.path.dirname(os.path.abspath(__file__))
    relative_apk_path = "test.apk"
    full_apk_path = os.path.join(current_directory, relative_apk_path)
    options = UiAutomator2Options()
    options.device_name = "aditya-phone"
    options.app = full_apk_path
    caps = dict(
        autoGrantPermissions=True
    )
    options.load_capabilities(caps)
    return options


@pytest.fixture()
def driver():
    appium_server_url = "http://127.0.0.1:4723"
    driver = webdriver.Remote(command_executor=appium_server_url, options=appium_options())
    time.sleep(2)
    yield driver
    driver.quit()
