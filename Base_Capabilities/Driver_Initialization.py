from appium import webdriver
from selenium.common.exceptions import WebDriverException
from Base_Capabilities.Fetch_Desired_Capabilities import Fetch_Desired_Capabilities
from selenium.common.exceptions import NoSuchAttributeException
from Base_Capabilities.iOS_Capabilities import IOS_Capabilities
from Base_Capabilities.Android_Capabilities import Android_Capabilities
from Base_Capabilities.Device_Actions import DeviceActions
from Locators.LoginScreen_Locators import *
from Modules.Android_Modules.Login import TestLoginScreenA
from Modules.iOS_Modules.Login import TestLoginScreenI


try:
    if Fetch_Desired_Capabilities.confirm_platform() != "Android":
        # Connecting to APPIUM SERVER with default port
        # http://localhost:4723/wd/hub
        driver = webdriver.Remote('http://localhost:4723/wd/hub', IOS_Capabilities.install_ios_app())
    else:
        # Connecting to APPIUM SERVER with default port
        # http://localhost:4723/wd/hub
        driver = webdriver.Remote('http://localhost:4723/wd/hub', Android_Capabilities.install_android_app())
except WebDriverException as WDE:
    if WDE.msg == "Unknown Error":
        raise NoSuchAttributeException(WDE.msg, WDE.stacktrace)
    else:
        raise WDE



android_email_error_id = android_email_input_error
ios_email_error_id = ios_input_email_error

# _______________________________________________________________________________________________________________

# CREATE OBJECTS & INITIATE ALL THE CLASSES HERE IN THIS SECTION
# _______________________________________________________________________________________________________________


__login_a = TestLoginScreenA(driver)
__login_i = TestLoginScreenI(driver)

# _______________________________________________________________________________________________________________
# ***************************************************************************************************************
# _______________________________________________________________________________________________________________
device_actions = DeviceActions()

if Fetch_Desired_Capabilities.confirm_platform() != "Android":
    loginscreen = __login_i

else:
    loginscreen = __login_a




