
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