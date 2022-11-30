from appium import webdriver
from selenium.common.exceptions import WebDriverException
from Base_Capabilities.Fetch_Desired_Capabilities import Fetch_Desired_Capabilities
from selenium.common.exceptions import NoSuchAttributeException

from Base_Capabilities.Fetch_Device_ID import DeviceID
from Base_Capabilities.iOS_Capabilities import IOS_Capabilities
from Base_Capabilities.Android_Capabilities import Android_Capabilities
from Base_Capabilities.Device_Actions import DeviceActions
from Locators.Android_Locators import *
from Modules.Android_Modules.login_screen import TestSenderLoginScreenA
from Modules.Android_Modules.receiver_messages import TestAndroidMessagesScreenR

device2 = "24191JEGR08497"

try:
    if Fetch_Desired_Capabilities.confirm_platform(device2) != "Android":
        # Connecting to APPIUM SERVER with default port
        # http://localhost:4723/wd/hub
        driver = webdriver.Remote('http://localhost:4723/wd/hub', IOS_Capabilities.install_ios_app())
    else:
        # Connecting to APPIUM SERVER with default port
        # http://localhost:4723/wd/hub
        receiverdriver = webdriver.Remote('http://localhost:4724/wd/hub', Android_Capabilities.relaunch_android_app_receiver())
        # receiverdriver = webdriver.Remote('http://localhost:4724/wd/hub', Android_Capabilities.relaunch_android_app_receiver())
except WebDriverException as WDE:
    if WDE.msg == "Unknown Error":
        raise NoSuchAttributeException(WDE.msg, WDE.stacktrace)
    else:
        raise WDE

#
#
# android_email_error_id = android_email_input_error
# ios_email_error_id = ios_input_email_error

# _______________________________________________________________________________________________________________

# CREATE OBJECTS & INITIATE ALL THE CLASSES HERE IN THIS SECTION
# _______________________________________________________________________________________________________________


__messages_screen = TestAndroidMessagesScreenR(receiverdriver)
# __sender_a = TestSenderLoginScreenA(receiverdriver)
# __receiver_a = TestReceiverLoginScreenA(receiverdriver)
# __login_i = TestLoginScreenI(driver)

# _______________________________________________________________________________________________________________
# ***************************************************************************************************************
# _______________________________________________________________________________________________________________
device_actions = DeviceActions()

if Fetch_Desired_Capabilities.confirm_platform(device2) != "Android":
    # senderloginscreen = __login_i
    pass
else:
    receiver_messages_screen = __messages_screen
    # receiverloginscreen = __receiver_a



