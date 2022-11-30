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
desired_caps['appPackage'] = "com.microsoft.android.smsorganizer"
desired_caps['appActivity'] = "com.microsoft.android.smsorganizer.StartupActivity"
desired_caps['noReset'] = True
desired_caps['fullReset'] = False
desired_caps['newCommandTimeout'] = 240
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

textViewNames = driver.find_elements(AppiumBy.ID, "com.microsoft.android.smsorganizer:id/textViewName")
for textViewName in textViewNames:
    name = textViewName.text
    print(name)
    if(name == "SBICRD"):
        textViewName.click()
        break

time.sleep(3)
message_text_views = driver.find_elements(AppiumBy.ID, "com.microsoft.android.smsorganizer:id/message_text_view")
recent_message = message_text_views[-1].text
print(recent_message)