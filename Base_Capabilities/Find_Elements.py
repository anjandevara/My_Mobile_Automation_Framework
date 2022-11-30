from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.common.exceptions import NoSuchAttributeException
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class FindElements:

    def __init__(self, driver):
        self.driver = driver

    def find_element_by_id(self, elementID):
        try:
            WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.ID, elementID)))
            screen_element = self.driver.find_element_by_id(elementID)
            return screen_element
        except WebDriverException as WDE:
            if WDE.msg == "NoSuchElementError":
                raise NoSuchAttributeException(WDE.msg, WDE.stacktrace)
            else:
                raise WDE

    def find_element_by_accessibility_id(self, elementID):
        try:
            WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, elementID)))
            screen_element = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, elementID)
            return screen_element
        except WebDriverException as WDE:
            if WDE.msg == "NoSuchElementError":
                raise NoSuchAttributeException(WDE.msg, WDE.stacktrace)
            else:
                raise WDE

    def find_element_by_resource_id(self, resourceID):
        try:
            WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((AppiumBy.ID, resourceID)))
            screen_element = self.driver.find_element(AppiumBy.ID, resourceID)
            return screen_element
        except WebDriverException as WDE:
            if WDE.msg == "NoSuchElementError":
                raise NoSuchAttributeException(WDE.msg, WDE.stacktrace)
            else:
                raise WDE

    def verify_element_not_displayed(self, resourceID):
        try:
            WebDriverWait(self.driver, 30).until_not(EC.presence_of_element_located((AppiumBy.ID, resourceID)))
            screen_element = self.driver.find_element(AppiumBy.ID, resourceID).is_displayed()
            return screen_element
        except WebDriverException as WDE:
            if WDE.msg == "NoSuchElementError":
                pass

    def verify_elements_not_displayed(self, resourceID):
        try:
            WebDriverWait(self.driver, 30).until_not(EC.presence_of_elements_located((AppiumBy.ID, resourceID)))
            screen_element = self.driver.find_element(AppiumBy.ID, resourceID).is_displayed()
            return screen_element
        except WebDriverException as WDE:
            if WDE.msg == "NoSuchElementError":
                pass


    def find_elements_by_resource_id(self, resourceID):
        try:
            WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((AppiumBy.ID, resourceID)))
            screen_element = self.driver.find_elements(AppiumBy.ID, resourceID)
            return screen_element
        except WebDriverException as WDE:
            if WDE.msg == "NoSuchElementError":
                raise NoSuchAttributeException(WDE.msg, WDE.stacktrace)
            else:
                raise WDE

    def find_elements_by_id(self, elementID):
        try:
            WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.ID, elementID)))
            screen_elements = self.driver.find_elements_by_id(elementID)
            return screen_elements
        except WebDriverException as WDE:
            if WDE.msg == "NoSuchElementError":
                raise NoSuchAttributeException(WDE.msg, WDE.stacktrace)
            else:
                raise WDE

    def find_elements_by_class_name(self, elementID):
        try:
            WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.CLASS_NAME, elementID)))
            screen_elements = self.driver.find_elements_by_class_name(elementID)
            return screen_elements
        except WebDriverException as WDE:
            if WDE.msg == "NoSuchElementError":
                raise NoSuchAttributeException(WDE.msg, WDE.stacktrace)
            else:
                raise WDE

    def find_element_by_class_name(self, elementID):
        try:
            WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.CLASS_NAME, elementID)))
            screen_element = self.driver.find_element_by_class_name(elementID)
            return screen_element
        except WebDriverException as WDE:
            if WDE.msg == "NoSuchElementError":
                raise NoSuchAttributeException(WDE.msg, WDE.stacktrace)
            else:
                raise WDE

    def longpress(self, contact):
        actions = TouchAction(self.driver)
        actions.long_press(contact)
        actions.perform()