import time

from selenium.common.exceptions import NoSuchAttributeException
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from Base_Capabilities.Find_Elements import FindElements
from Locators.Android_Locators import *


class TestReceiverLoginScreenA(FindElements):
    # --------------------- LOGIN FIELDS VERIFICATION SECTION ---------------------

    def get_login_username(self):
        user_mail = self.find_element_by_id(username_tf).get_attribute("text")
        return user_mail

    def get_login_password(self):
        user_password = self.find_element_by_id(password_tf).get_attribute("text")
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
        time.sleep(10)
        self.driver.hide_keyboard()

        login_button = self.find_element_by_id(login_bt)
        assert login_button

    def click_Login_Button(self):
        time.sleep(10)
        self.driver.hide_keyboard()

        login_button = self.find_element_by_id(login_bt)
        if login_button.is_displayed():
            login_button.click()

    def click_agreebutton(self):
        self.click_AgreeButton_Android()

    def click_cancelbutton(self):
        self.click_CancelButton_Android()

    def click_RememberMe_Button(self):
        WebDriverWait(self.driver, 60).until(
            EC.presence_of_element_located((By.ID, android_remember_me_bt)))
        rememberme_checkbox = self.find_element_by_id(android_remember_me_bt)
        rememberme_checkbox.click()

    def verify_password(self):
        self.get_Password_Android()

    def get_rememberme(self):
        WebDriverWait(self.driver, 60).until(EC.presence_of_element_located((By.CLASS_NAME, "android.widget.CheckBox")))
        rememberme_checkbox = self.find_element_by_class_name("android.widget.CheckBox")
        state = rememberme_checkbox.get_attribute("checked")
        # logging.debug("Current Remember State :: ", state)
        return state

    def verify_hideunhide_state(self):
        WebDriverWait(self.driver, 50).until(EC.presence_of_element_located((By.ID, hide_unhide_android)))
        HideUnhide_button_state = self.find_element_by_id(hide_unhide_android)
        state = HideUnhide_button_state.get_attribute("checked")
        return state

    def click_hideunhide_button(self):
        WebDriverWait(self.driver, 50).until(EC.presence_of_element_located((By.ID, hide_unhide_android)))
        HideUnhide_button_state = self.find_element_by_id(hide_unhide_android)
        HideUnhide_button_state.click()

    def verify_login_errorMessage(self):
        self.verify_login_errorMessage_Android()

    def verify_email_input_error(self):
        self.verify_email_inputError_Android()

    def verify_password_input_error(self):
        self.verify_password_inputError_Android()

    def verify_eula_title(self):
        time.sleep(10)
        self.driver.switch_to.context("WEBVIEW_com.example.manager.debug")
        time.sleep(2)
        eula_agree = self.driver.find_element_by_css_selector(
            "body > p:nth-child(1) > font > font > font > font > font > b")
        # eula_agree = WebDriverWait(self.driver, 60).until(
        #     EC.presence_of_element_located((By.CLASS_NAME, self.android_eula_title)))
        return eula_agree.is_displayed()

    def verify_eula_agree_button(self):
        WebDriverWait(self.driver, 60).until(EC.presence_of_element_located((By.ID, android_eula_agree)))
        eula_agree = self.find_element_by_id(android_eula_agree)
        return eula_agree.is_displayed()

    def click_eula_cancel_button(self):
        WebDriverWait(self.driver, 60).until(EC.presence_of_element_located((By.ID, android_eula_cancel)))
        eula_cancel = self.find_element_by_id("android_eula_cancel")
        eula_cancel.click()

    def click_eula_agree_button(self):
        WebDriverWait(self.driver, 60).until(EC.presence_of_element_located((By.ID, android_eula_agree)))
        eula_agree = self.driver.find_element_by_id(android_eula_agree)
        eula_agree.click()

    def verify_nothanks_biometrics(self):
        try:
            webview = self.driver.contexts[1]
            self.driver.switch_to.context(webview)
            time.sleep(3)
            biometrics_nothanks = self.driver.find_element_by_name("Licensed Application Terms and Conditions")
            return biometrics_nothanks.is_displayed()
        except WebDriverException as WDE:
            if WDE.msg == "NoSuchElementError":
                raise NoSuchAttributeException(WDE.msg, WDE.stacktrace)
            else:
                raise WDE

    def click_nothanks_biometrics(self):
        try:
            WebDriverWait(self.driver, 60).until(EC.presence_of_element_located((By.ID, android_biometric_notthanks)))
            biometrics_nothanks = self.driver.find_element_by_id(android_biometric_notthanks)
            biometrics_nothanks.click()
        except WebDriverException as WDE:
            if WDE.msg == "NoSuchElementError":
                raise NoSuchAttributeException(WDE.msg, WDE.stacktrace)
            else:
                raise WDE

    def get_rememberMe_Android(self):
        try:
            WebDriverWait(self.driver, 60).until(EC.presence_of_element_located((By.ID, android_remember_me_bt)))
            rememberme_checkbox = self.find_element_by_id(android_remember_me_bt)
            state = rememberme_checkbox.get_attribute("checked")
            return state
        except WebDriverException as WDE:
            if WDE.msg == "NoSuchElementError":
                raise NoSuchAttributeException(WDE.msg, WDE.stacktrace)
            else:
                raise WDE

    # --------------------- ANDROID HIDE/UNHIDE VERIFICATION CODE SECTION ---------------------
    def hideUnhide_Button(self):
        HideUnhide_button = self.find_element_by_id(hide_unhide_android)
        return HideUnhide_button

    def get_HideUnhide_state_Android(self):
        try:
            WebDriverWait(self.driver, 50).until(EC.presence_of_element_located((By.ID, hide_unhide_android)))
            HideUnhide_button_state = self.find_element_by_id(hide_unhide_android)
            state = HideUnhide_button_state.get_attribute("checked")
            return state
        except WebDriverException as WDE:
            if WDE.msg == "NoSuchElementError":
                raise NoSuchAttributeException(WDE.msg, WDE.stacktrace)
            else:
                raise WDE

    def get_Password_Android(self):
        try:
            HideUnhide_button_state = self.hideUnhide_Button().get_attribute("checked")
            return HideUnhide_button_state
        except WebDriverException as WDE:
            if WDE.msg == "NoSuchElementError":
                raise NoSuchAttributeException(WDE.msg, WDE.stacktrace)
            else:
                raise WDE

    # --------------------- ERROR MESSAGE VERIFICATION CODE SECTION ---------------------
    def verify_login_errorMessage_Android(self):
        try:
            invalid_credentials_error_msg_label = self.find_element_by_id(
                invalid_credentials_error_android_label).get_attribute("text")
            return invalid_credentials_error_msg_label
        except WebDriverException as WDE:
            if WDE.msg == "NoSuchElementError":
                raise NoSuchAttributeException(WDE.msg, WDE.stacktrace)
            else:
                raise WDE

    def verify_email_inputError_Android(self):
        try:
            error_msg_label = self.driver.find_element_by_id(android_email_input_error).get_attribute("text")
            return error_msg_label
        except WebDriverException as WDE:
            if WDE.msg == "NoSuchElementError":
                raise NoSuchAttributeException(WDE.msg, WDE.stacktrace)
            else:
                raise WDE

    def verify_password_inputError_Android(self):
        try:
            invalid_credentials_error_msg_label = self.find_element_by_id(android_password_input_error).get_attribute(
                "text")
            return invalid_credentials_error_msg_label
        except WebDriverException as WDE:
            if WDE.msg == "NoSuchElementError":
                raise NoSuchAttributeException(WDE.msg, WDE.stacktrace)
            else:
                raise WDE

    # --------------------- AGREE BUTTON CODE SECTION ---------------------
    def click_AgreeButton_Android(self):
        try:
            WebDriverWait(self.driver, 60).until(EC.presence_of_element_located((By.ID, android_eula_agree)))
            elementFound = self.driver.find_element_by_id(android_eula_agree)
            elementFound.click()
        except WebDriverException as WDE:
            if WDE.msg == "NoSuchElementError":
                raise NoSuchAttributeException(WDE.msg, WDE.stacktrace)
            else:
                raise WDE

    def click_CancelButton_Android(self):
        try:
            WebDriverWait(self.driver, 60).until(EC.presence_of_element_located((By.ID, android_eula_cancel)))
            elementFound = self.driver.find_element_by_id(android_eula_cancel)
            elementFound.click()
        except WebDriverException as WDE:
            if WDE.msg == "NoSuchElementError":
                raise NoSuchAttributeException(WDE.msg, WDE.stacktrace)
            else:
                raise WDE
