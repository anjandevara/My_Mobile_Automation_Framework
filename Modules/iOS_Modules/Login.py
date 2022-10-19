from selenium.common.exceptions import NoSuchAttributeException
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from Base_Capabilities.Fetch_Desired_Capabilities import Fetch_Desired_Capabilities
from Base_Capabilities.Find_Elements import FindElements
from Locators.LoginScreen_Locators import *


class TestLoginScreenI(FindElements):
    # --------------------- LOGIN FIELDS VERIFICATION CODE SECTION ---------------------

    def get_login_username(self):
        user_mail = self.find_element_by_id(username_tf).get_attribute("value")
        return user_mail

    def get_login_password(self):
        user_password = self.find_element_by_id(password_tf).get_attribute("value")
        return user_password

    def enter_username(self, username):

        username_textbox = self.find_element_by_id(username_tf)

        if username_textbox.is_displayed():
            username_textbox.click()
            username_textbox.clear()
            username_textbox.send_keys(username)

    def clear_username(self):

        username_textbox = self.find_element_by_id(username_tf)

        if username_textbox.is_displayed():
            username_textbox.click()
            username_textbox.clear()

    def enter_password(self, password):

        password_textbox = self.find_element_by_id(password_tf)

        if password_textbox.is_displayed():
            password_textbox.click()
            password_textbox.clear()
            password_textbox.send_keys(password)

    def clear_password(self):

        password_textbox = self.find_element_by_id(password_tf)

        if password_textbox.is_displayed():
            password_textbox.click()
            password_textbox.clear()

    def verify_Login_Button(self):
        login_button = self.find_element_by_id(login_bt)
        assert login_button.is_displayed() == True

    def click_Login_Button(self):
        login_button = self.find_element_by_id(login_bt)
        if login_button.is_displayed():
            login_button.click()

    def click_agreebutton(self):
        self.click_AgreeButton_ios()

    def click_cancelbutton(self):
        self.click_CancelButton_ios()

    def click_RememberMe_Button(self):
        rememberme_checkbox = WebDriverWait(self.driver, 50).until(
            EC.presence_of_element_located((By.ID, ios_remember_me_bt)))
        rememberme_checkbox.click()

    def verify_password(self):
        self.get_Password_ios()

    def get_rememberme(self):
        rememberme_checkbox = WebDriverWait(self.driver, 50).until(
            EC.presence_of_element_located((By.ID, ios_remember_me_bt)))
        state = rememberme_checkbox.get_attribute("value")
        return state

    def verify_hideunhide_state(self):
        HideUnhide_button_state = WebDriverWait(self.driver, 50).until(
            EC.presence_of_element_located((By.ID, hide_unhide_iOS)))
        state = HideUnhide_button_state.get_attribute("value")
        return state

    def click_hideunhide_button(self):
        HideUnhide_button_state = WebDriverWait(self.driver, 50).until(
            EC.presence_of_element_located((By.ID, hide_unhide_iOS)))
        HideUnhide_button_state.click()

    def verify_login_errorMessage(self):
        self.verify_login_errorMessage_ios()

    def verify_email_input_error(self):
        self.verify_email_inputError_ios()

    def verify_password_input_error(self):
        self.verify_password_inputError_ios()

    def click_eula_cancel_button(self):
        eula_cancel = WebDriverWait(self.driver, 60).until(
            EC.presence_of_element_located((By.ID, ios_eula_cancel)))
        eula_cancel.click()

    def verify_eula_title(self):
        eula_agree = WebDriverWait(self.driver, 60).until(
            EC.presence_of_element_located((By.ID, ios_eula_title)))
        return eula_agree.is_displayed()

    def verify_eula_agree_button(self):
        eula_agree = WebDriverWait(self.driver, 60).until(
            EC.presence_of_element_located((By.ID, ios_eula_agree)))
        return eula_agree.is_displayed()

    def click_eula_agree_button(self):
        eula_agree = WebDriverWait(self.driver, 60).until(
            EC.presence_of_element_located((By.ID, ios_eula_agree)))
        eula_agree.click()

    def verify_nothanks_biometrics(self):
        try:
            WebDriverWait(self.driver, 60).until(EC.presence_of_element_located((By.ID, ios_biometric_notthanks)))
            biometrics_nothanks = self.driver.find_element_by_id(ios_biometric_notthanks)
            return biometrics_nothanks.is_displayed()
        except WebDriverException as WDE:
            if WDE.msg == "NoSuchElementError":
                raise NoSuchAttributeException(WDE.msg, WDE.stacktrace)
            else:
                raise WDE

    def click_nothanks_biometrics(self):
        try:
            WebDriverWait(self.driver, 60).until(EC.presence_of_element_located((By.ID, ios_biometric_notthanks)))
            biometrics_nothanks = self.driver.find_element_by_id(ios_biometric_notthanks)
            biometrics_nothanks.click()
        except WebDriverException as WDE:
            if WDE.msg == "NoSuchElementError":
                raise NoSuchAttributeException(WDE.msg, WDE.stacktrace)
            else:
                raise WDE

    # --------------------- REMEMBER ME VERIFICATION CODE SECTION ---------------------
    # def click_RememberMe_Button(self):
    #     rememberMe_button = self.find_element_by_id(ios_remember_me_bt)
    #     rememberMe_button.click()

    def get_rememberMe_iOS(self):
        try:
            rememberme_checkbox = WebDriverWait(self.driver, 50).until(
                EC.presence_of_element_located((By.ID, ios_remember_me_bt)))
            state = rememberme_checkbox.get_attribute("value")
            return state
        except WebDriverException as WDE:
            if WDE.msg == "NoSuchElementError":
                raise NoSuchAttributeException(WDE.msg, WDE.stacktrace)
            else:
                raise WDE

    # --------------------- ios HIDE/UNHIDE VERIFICATION CODE SECTION ---------------------
    def hideUnhide_Button(self):
        try:
            HideUnhide_button = self.find_element_by_id(hide_unhide_iOS)
            return HideUnhide_button
        except WebDriverException as WDE:
            if WDE.msg == "NoSuchElementError":
                raise NoSuchAttributeException(WDE.msg, WDE.stacktrace)
            else:
                raise WDE

    def get_HideUnhide_state_ios(self):
        try:
            HideUnhide_button_state = WebDriverWait(self.driver, 50).until(
                EC.presence_of_element_located((By.ID, hide_unhide_iOS)))
            state = HideUnhide_button_state.get_attribute("value")
            return state
        except WebDriverException as WDE:
            if WDE.msg == "NoSuchElementError":
                raise NoSuchAttributeException(WDE.msg, WDE.stacktrace)
            else:
                raise WDE

    def get_Password_ios(self):
        try:
            HideUnhide_button_state = self.hideUnhide_Button().get_attribute("value")
            return HideUnhide_button_state
        except WebDriverException as WDE:
            if WDE.msg == "NoSuchElementError":
                raise NoSuchAttributeException(WDE.msg, WDE.stacktrace)
            else:
                raise WDE

    # --------------------- ERROR MESSAGE VERIFICATION CODE SECTION ---------------------
    def verify_login_errorMessage_ios(self):
        try:
            # invalid_credentials_error_msg_label = WebDriverWait(self.driver, 50).until(
            #     EC.presence_of_element_located((By.ID, invalid_credentials_error_ios_notification)))
            invalid_credentials_error_msg_label = WebDriverWait(self.driver, 50).until(
                EC.presence_of_element_located((By.XPATH, invalid_credentials_error_ios_notification)))
            # invalid_credentials_error_msg_label = self.driver.find_element_by_id(invalid_credentials_error_ios_notification).get_attribute("label")
            return invalid_credentials_error_msg_label
        except WebDriverException as WDE:
            if WDE.msg == "NoSuchElementError":
                raise NoSuchAttributeException(WDE.msg, WDE.stacktrace)
            else:
                raise WDE

    def verify_email_inputError_ios(self):
        try:
            invalid_credentials_error_msg_label = self.find_element_by_id(username_tf).get_attribute("label")
            return invalid_credentials_error_msg_label
        except WebDriverException as WDE:
            if WDE.msg == "NoSuchElementError":
                raise NoSuchAttributeException(WDE.msg, WDE.stacktrace)
            else:
                raise WDE

    def verify_password_inputError_ios(self):
        try:
            invalid_credentials_error_msg_label = self.find_element_by_id(password_tf).get_attribute("label")
            return invalid_credentials_error_msg_label
        except WebDriverException as WDE:
            if WDE.msg == "NoSuchElementError":
                raise NoSuchAttributeException(WDE.msg, WDE.stacktrace)
            else:
                raise WDE

    # --------------------- AGREE BUTTON CODE SECTION ---------------------
    def click_AgreeButton_ios(self):
        try:
            self.dc = Fetch_Desired_Capabilities()
            wait = WebDriverWait(self.driver, 20)
            element = WebDriverWait(self.driver, 50).until(EC.presence_of_element_located((By.NAME, "AGREE")))
            elementFound = self.driver.find_element_by_name("AGREE")
            elementFound.click()
        except WebDriverException as WDE:
            if WDE.msg == "NoSuchElementError":
                raise NoSuchAttributeException(WDE.msg, WDE.stacktrace)
            else:
                raise WDE

    def click_CancelButton_ios(self):
        self.find_element_by_id(ios_eula_cancel).click()
