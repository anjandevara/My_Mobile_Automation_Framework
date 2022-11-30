# __author__ = 'Anjan Kumar Devara"
import subprocess

from Base_Capabilities.androidDevicesList import devicesList


class DeviceID:

    def adbDevices(self):
        file1 = open('Base_Capabilities/androidDevicesList.txt', 'w')
        p = subprocess.Popen("adb devices", stdout=subprocess.PIPE, shell=True)
        (output, err) = p.communicate()
        p.wait()

        # Writing multiple strings
        # at a time
        result = str(output.decode('ascii')).rstrip()
        file1.write(result)
        # Closing file
        file1.close()

    def readFile(self, filename):
        self.adbDevices()
        emptyList = []
        with open(filename, 'r', encoding='UTF-8') as file:
            while (line := file.readline().rstrip()):
                emptyList.append(line)
        return emptyList

    def fetchingDevicesList(self):
        ddd = self.readFile('Base_Capabilities/androidDevicesList.txt')

        deviceslist = []
        deviceDict = {}
        for item in range(1, len(ddd)):
            aaa = ddd[item]
            sss = aaa[:-7]
            deviceslist.append(sss)
            deviceSerialNumber = 'device' + str(item)
            deviceSerialNumberList = [deviceSerialNumber]
            for k in deviceslist:
                # k:
                deviceDict[deviceSerialNumber] = k
            # print(deviceDict)
        print(deviceDict)
        return deviceDict

    def writeDevicesListToPythonFile(self):
        file1 = open('Base_Capabilities/androidDevicesList.py', 'w')

        # Writing multiple strings
        # at a time
        file1.write("devicesList=")
        devList = self.fetchingDevicesList()
        print(devList)
        file1.write(str(devList))

        # Closing file
        file1.close()

    def getDeviceID(self, deviceNumber):
        self.writeDevicesListToPythonFile()
        devicename = devicesList[deviceNumber]
        print(devicename)
        return devicename
