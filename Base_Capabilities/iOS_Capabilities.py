from Base_Capabilities.Fetch_Desired_Capabilities import Fetch_Desired_Capabilities
from Base_Capabilities.App_Details import *


class IOS_Capabilities(Fetch_Desired_Capabilities):
    fetch_Device_details = Fetch_Desired_Capabilities()

    # FOLLOWING DEFINITION INSTALLS THE APP FILE USING IOS Capabilities
    @classmethod
    def install_ios_app(cls):
        desired_caps = {}
        desired_caps['platformName'] = "iOS"
        desired_caps['platformVersion'] = cls.get_ios_device_version()
        desired_caps['deviceName'] = cls.get_ios_device_name()
        desired_caps['udid'] = cls.get_ios_device_udid()
        desired_caps['automationName'] = "XCUITest"
        desired_caps['app'] = ios_app_path
        desired_caps['noReset'] = True
        desired_caps['fullReset'] = False
        desired_caps['newCommandTimeout'] = 240
        return desired_caps

    # FOLLOWING DEFINITION RELAUNCHES THE APP FILE USING IOS Capabilities
    @classmethod
    def relaunch_ios_app(cls):
        desired_caps = {}
        desired_caps['platformName'] = "iOS"
        desired_caps['platformVersion'] = cls.get_ios_device_version()
        desired_caps['deviceName'] = cls.get_ios_device_name()
        desired_caps['automationName'] = "XCUITest"
        desired_caps['bundleId'] = "com.example.manager.debug"
        desired_caps['noReset'] = True
        desired_caps['fullReset'] = False
        desired_caps['newCommandTimeout'] = 240
        return desired_caps

    # FOLLOWING DEFINITION RELAUNCHES THE APP FILE USING IOS Capabilities
    @classmethod
    def reset_and_launch_android_app(cls):
        fdc = Fetch_Desired_Capabilities()

        desired_caps = {}
        desired_caps['platformName'] = "iOS"
        desired_caps['platformVersion'] = cls.get_ios_device_version()
        desired_caps['deviceName'] = cls.get_ios_device_name()
        desired_caps['udid'] = cls.get_ios_device_udid()
        desired_caps['automationName'] = "XCUITest"
        desired_caps['bundleId'] = "com.example.manager.debug"
        desired_caps['fastReset'] = True
        desired_caps['newCommandTimeout'] = 240
        return desired_caps
