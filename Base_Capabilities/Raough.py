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

driver.open_notifications()
time.sleep(5)

notification_titles = driver.find_elements(AppiumBy.ID, "com.android.systemui:id/notification_title")
for notification_title in notification_titles:
    title = notification_title.text
    print(title)
    if(title == "Ramya Devara"):
        notification_title.click()
        break


notification_stack_scroller = "com.android.systemui:id/notification_stack_scroller"
frameLayouts = "android.widget.FrameLayout"
notification_children_container = "com.android.systemui:id/notification_children_container"
frameLayout = "android.widget.FrameLayout"
expanded = "com.android.systemui:id/expanded"
linearLayout = "android.widget.LinearLayout"
notification_title = "com.android.systemui:id/notification_title"

driver.set_network_connection(1)
# scroller = driver.find_element(AppiumBy.ID, notification_stack_scroller)
# frLayout = scroller.find_elements(AppiumBy.CLASS_NAME, frameLayouts)
# container = frLayout[1].find_element(AppiumBy.ID, notification_children_container)
# container = scroller.find_element(AppiumBy.ID, notification_children_container)
    # print(len(container))
# frLayout1 = container.find_element(AppiumBy.CLASS_NAME, frameLayout)
# expand = frLayout1.find_element(AppiumBy.ID, expanded[2])
# liLaout = expand.find_element(AppiumBy.CLASS_NAME, linearLayout)
# ntitle = liLaout.find_element(AppiumBy.ID, notification_title).text
# print(ntitle)
# print(len(frLayout))
# for frLayo in frLayout:
#     container = frLayo.find_elements(AppiumBy.ID, notification_children_container)
#     print(len(container))
    # frLayout1 = container.find_element(AppiumBy.CLASS_NAME, frameLayout)
    # expand = frLayout1.find_elements(AppiumBy.ID, expanded)
    # liLaout = expand[2].find_element(AppiumBy.CLASS_NAME, linearLayout)
    # ntitle = liLaout.find_element(AppiumBy.ID, notification_title).text
    # print(ntitle)