from Base_Capabilities.Fetch_Desired_Capabilities import Fetch_Desired_Capabilities
from Base_Capabilities.App_Details import *
from Base_Capabilities.Fetch_Device_ID import DeviceID

class Android_Capabilities(Fetch_Desired_Capabilities):
    # deviceID = DeviceID()
    # device1 = deviceID.getDeviceID("device1")
    # device2 = deviceID.getDeviceID("device2")
    # print(device1)

    # FOLLOWING DEFINITION INSTALLS THE APP FILE USING ANDROID Capabilities
    @classmethod
    def install_android_app(cls):
        desired_caps = {}
        desired_caps['platformName'] = cls.get_device_platformname(cls.device1)
        desired_caps['platformVersion'] = cls.get_android_device_version(cls.device1)
        desired_caps['deviceName'] = cls.get_android_device_name()
        desired_caps['automationName'] = "UiAutomator2"
        desired_caps['app'] = android_app_path
        desired_caps['noReset'] = True
        desired_caps['fullReset'] = False
        desired_caps['newCommandTimeout'] = 240
        return desired_caps

    # FOLLOWING DEFINITION PROVIDES ANDROID Capabilities
    @classmethod
    def relaunch_android_app_sender(cls):
        desired_caps = {}
        # desired_caps['platformName'] = cls.get_device_platformname(cls.device1)
        desired_caps['platformName'] = "Android"
        desired_caps['udid'] = "0123456789ABCDEF"
        # desired_caps['deviceName'] = "24191JEGR08497"
        # desired_caps['platformVersion'] = cls.get_android_device_version(cls.device1)
        desired_caps['platformVersion'] = "12"
        # desired_caps['deviceName'] = cls.get_android_device_name()
        desired_caps['automationName'] = "UiAutomator2"
        desired_caps['appPackage'] = appPackage
        desired_caps['appActivity'] = appActivity
        desired_caps['noReset'] = True
        desired_caps['fullReset'] = False
        desired_caps['newCommandTimeout'] = 240
        return desired_caps

    @classmethod
    def relaunch_android_app_receiver(cls):
        desired_caps = {}
        # desired_caps['platformName'] = cls.get_device_platformname(cls.device2)
        desired_caps['platformName'] = "Android"
        desired_caps['platformVersion'] = "12"
        desired_caps['udid'] = "24191JEGR08497"
        # desired_caps['deviceName'] = "0123456789ABCDEF"
        # desired_caps['platformVersion'] = cls.get_android_device_version(cls.device2)
        # desired_caps['deviceName'] = cls.get_android_device_name()
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
        desired_caps['platformName'] = cls.get_device_platformname(cls.device1)
        desired_caps['platformVersion'] = cls.get_android_device_version(cls.device1)
        desired_caps['deviceName'] = cls.get_android_device_name()
        desired_caps['automationName'] = "UiAutomator2"
        desired_caps['appPackage'] = appPackage
        desired_caps['appActivity'] = appActivity
        desired_caps['fastReset']  = True
        desired_caps['newCommandTimeout'] = 240
        return desired_caps