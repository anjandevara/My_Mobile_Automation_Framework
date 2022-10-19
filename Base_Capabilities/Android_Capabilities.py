from Base_Capabilities.Fetch_Desired_Capabilities import Fetch_Desired_Capabilities
from Base_Capabilities.App_Details import *


class Android_Capabilities(Fetch_Desired_Capabilities):

    # FOLLOWING DEFINITION INSTALLS THE APP FILE USING ANDROID Capabilities
    @classmethod
    def install_android_app(cls):
        desired_caps = {}
        desired_caps['platformName'] = cls.get_device_platformname()
        desired_caps['platformVersion'] = cls.get_android_device_version()
        desired_caps['deviceName'] = cls.get_android_device_name()
        desired_caps['automationName'] = "UiAutomator2"
        desired_caps['app'] = android_app_path
        desired_caps['noReset'] = True
        desired_caps['fullReset'] = False
        desired_caps['newCommandTimeout'] = 240
        return desired_caps

    # FOLLOWING DEFINITION PROVIDES ANDROID Capabilities
    @classmethod
    def relaunch_android_app(cls):
        desired_caps = {}
        desired_caps['platformName'] = cls.get_device_platformname()
        desired_caps['platformVersion'] = cls.get_android_device_version()
        desired_caps['deviceName'] = cls.get_android_device_name()
        desired_caps['automationName'] = "UiAutomator2"
        desired_caps['appPackage'] = appPackage
        desired_caps['appActivity'] = appActivity
        desired_caps['noReset'] = True
        desired_caps['fullReset'] = False
        desired_caps['newCommandTimeout'] = 240
        return desired_caps

    # FOLLOWING DEFINITION PROVIDES ANDROID Capabilities
    @classmethod
    def reset_and_launch_android_app(cls):
        desired_caps = {}
        desired_caps['platformName'] = cls.get_device_platformname()
        desired_caps['platformVersion'] = cls.get_android_device_version()
        desired_caps['deviceName'] = cls.get_android_device_name()
        desired_caps['automationName'] = "UiAutomator2"
        desired_caps['appPackage'] = appPackage
        desired_caps['appActivity'] = appActivity
        desired_caps['fastReset']  = True
        desired_caps['newCommandTimeout'] = 240
        return desired_caps
