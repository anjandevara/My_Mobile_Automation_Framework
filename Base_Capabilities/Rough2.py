# __author__ = 'Anjan Kumar Devara"
import time

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy


desired_caps = {}
desired_caps['platformName'] = "Android"
# desired_caps['platformVersion'] = "11"
desired_caps['platformVersion'] = "12"
# desired_caps['platformVersion'] = "10"
# desired_caps['deviceName'] = "BM1S1B"
# desired_caps['deviceName'] = "BM1S1B"
desired_caps['deviceName'] = "0123456789ABCDEF"
# desired_caps['deviceName'] = "RC545L"
desired_caps['automationName'] = "UiAutomator2"
desired_caps['appPackage'] = "com.bullitt.wave"
desired_caps['appActivity'] = "com.bullitt.wave.MainActivity"
desired_caps['noReset'] = True
desired_caps['fullReset'] = False
desired_caps['newCommandTimeout'] = 240
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

time.sleep(5)
# el1 = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Open navigation drawer")
# el1.click()

driver.toggle_wifi()