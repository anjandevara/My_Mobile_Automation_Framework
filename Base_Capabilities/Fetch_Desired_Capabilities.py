import subprocess

from Base_Capabilities.Commands import *


class Fetch_Desired_Capabilities:

    # FETCH ANDROID DEVICE NAME
    @classmethod
    def get_android_device_name(cls):
        p = subprocess.Popen(get_device_name, stdout=subprocess.PIPE, shell=True)
        (output, err) = p.communicate()
        p.wait()

        return str(output.decode('ascii')).rstrip()

    # FETCH ANDROID PLATFORM NAME
    @classmethod
    def get_device_platformname(cls):
        p = subprocess.Popen(get_platform_name, stdout=subprocess.PIPE, shell=True)
        (output, err) = p.communicate()
        p.wait()
        # print(str(output.decode('ascii')))
        return str(output.decode('ascii')).rstrip()

    # FETCH ANDROID DEVICE VERSION
    @classmethod
    def get_android_device_version(cls):
        p = subprocess.Popen(get_device_version, stdout=subprocess.PIPE, shell=True)
        (output, err) = p.communicate()
        p.wait()

        return str(output.decode('ascii')).rstrip()

    # FETCH ANDROID DEVICE VERSION
    @classmethod
    def get_device_udid(cls):
        p = subprocess.Popen(get_udid, stdout=subprocess.PIPE, shell=True)
        (output, err) = p.communicate()
        p.wait()

        out = str(output.decode('ascii'))
        asd = out.splitlines()
        qwe = asd[0]
        return qwe

    # FETCH IOS DEVICE VERSION
    @classmethod
    def get_device_className(cls):
        p = subprocess.Popen("ideviceinfo | grep -i DeviceClass", stdout=subprocess.PIPE, shell=True)
        (output, err) = p.communicate()
        p.wait()
        # print(str(output.decode('ascii')))
        return str(output.decode('ascii')).rstrip()


    @classmethod
    def get_ios_device_version(cls):
        p = subprocess.Popen("ideviceinfo | grep -i ProductVersion", stdout=subprocess.PIPE, shell=True)
        (output, err) = p.communicate()
        p.wait()
        # print(str(output.decode('ascii')))
        product_version = str(output.decode('ascii')).rstrip()
        version = product_version.find(":")
        # print(version)
        print(product_version[version + 2:])
        return product_version[version + 2:]

    @classmethod
    def get_ios_device_name(cls):
        p = subprocess.Popen("ideviceinfo | grep -i DeviceName", stdout=subprocess.PIPE, shell=True)
        (output, err) = p.communicate()
        p.wait()
        # print(str(output.decode('ascii')))
        product_version = str(output.decode('ascii')).rstrip()
        version = product_version.find(":")
        # print(version)
        print(product_version[version + 2:])
        deviceName = product_version[version + 2:]
        return deviceName

    @classmethod
    def get_ios_device_udid(cls):
        p = subprocess.Popen("ideviceinfo | grep -i UniqueDeviceID", stdout=subprocess.PIPE, shell=True)
        (output, err) = p.communicate()
        p.wait()
        # print(str(output.decode('ascii')))
        product_version = str(output.decode('ascii')).rstrip()
        version = product_version.find(":")
        # print(version)
        print(product_version[version + 2:])
        return product_version[version + 2:]


    @classmethod
    def confirm_platform(cls):
        connected_device_platform = cls.get_device_platformname()
        print(connected_device_platform)
        return connected_device_platform