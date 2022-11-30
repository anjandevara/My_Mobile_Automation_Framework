# __author__ = 'Anjan Kumar Devara"
# __author__ = 'Anjan Kumar Devara"
# __author__ = 'Anjan Kumar Devara"
import time

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By

desired_caps = {}
desired_caps['platformName'] = "Android"
desired_caps['platformVersion'] = "11"
# desired_caps['platformVersion'] = "12"
# desired_caps['platformVersion'] = "10"
# desired_caps['deviceName'] = "BM1S1B"
desired_caps['deviceName'] = "a70qdd"
# desired_caps['deviceName'] = "RC545L"
desired_caps['automationName'] = "UiAutomator2"
desired_caps['appPackage'] = "com.bullitt.wave"
desired_caps['appActivity'] = "com.bullitt.wave.LoginActivity"
desired_caps['noReset'] = True
desired_caps['fullReset'] = False
desired_caps['newCommandTimeout'] = 240
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

time.sleep(3)
el1 = driver.find_element(AppiumBy.ID, "com.bullitt.wave:id/phone_number")
el1.click()
el1.send_keys("9515483896")
el2 = driver.find_element(AppiumBy.ID, "com.bullitt.wave:id/password")
el2.click()
el2.send_keys("thaun88")
el3 = driver.find_element(AppiumBy.ID, "com.bullitt.wave:id/sign_in_button")
el3.click()

time.sleep(5)
contact_user_names = driver.find_elements(AppiumBy.ID, "com.bullitt.wave:id/contact_user_name")
for contact_user_name in contact_user_names:
    username = contact_user_name.text
    if username == "AkhilaInnominds":
        contact_user_name.click()
        break

text_message_bodys = driver.find_elements(AppiumBy.ID, "com.bullitt.wave:id/text_message_body")
for text_message_body in text_message_bodys:
    text_message_body.click()