"""Testing Fingerprint Enable & Disable Access feature tests."""
import pytest

from Base_Capabilities.Driver_Initialization import *
from Locators.LoginScreen_Locators import *
from pytest_bdd import (
    given,
    scenario,
    then,
    when
)
import time
from appium import webdriver as driver
from Base_Capabilities.App_Credentials import *

@pytest.fixture
def browser():

    yield driver

    driver.quit()

@scenario('LoginScenarios.feature', 'Verify the login screen components')
def test_verify_the_login_screen_components():
    """Verify the login screen components."""
    return


@scenario('LoginScenarios.feature', 'Click on the Unchecked RememberMe and verify the state is TRUE')
def test_click_on_the_unchecked_rememberme_and_verify_the_state_is_true():
    """Click on the Unchecked RememberMe and verify the state is TRUE."""
    return


@scenario('LoginScenarios.feature',
          'Verify Error Message "Please enter a valid email." when empty Username & Valid Password are entered')
def test_verify_error_message_please_enter_a_valid_email_when_empty_username__valid_password_are_entered():
    """Verify Error Message "Please enter a valid email." when empty Username & Valid Password are entered."""
    return


@scenario('LoginScenarios.feature',
          'Verify the error messages displayed when login button is clicked without entering the credentials')
def test_verify_the_error_messages_displayed_when_login_button_is_clicked_without_entering_the_credentials():
    """Verify the error messages displayed when login button is clicked without entering the credentials."""
    return


@given('The application is launched')
def the_application_is_launched():
    """The application is launched."""
    pass


@when('Current Screen Is Login Screen')
def current_screen_is_login_screen():
    """Current Screen Is Login Screen."""
    pass


@then('Verify the Email Field Place Holder')
def verify_the_email_field_place_holder():
    """Verify the Email Field Place Holder."""
    assert loginscreen.get_login_username() == "Email"


@then('Verify the Password Field Place Holder')
def verify_the_password_field_place_holder():
    """Verify the Password Field Place Holder."""
    assert loginscreen.get_login_password() == "Password"


@then('Verify iOS: REMEMBER ME or Android: REMEMBER EMAIL checkbox is in UNCHECKED State')
def verify_ios_remember_me_or_android_remember_email_checkbox_is_in_unchecked_state():
    """Verify iOS: REMEMBER ME or Android: REMEMBER EMAIL checkbox is in UNCHECKED State."""
    assert loginscreen.get_rememberme() == "false"


@then('Verify the LOGIN Button')
def verify_the_login_button():
    """Verify the LOGIN Button."""
    loginscreen.verify_Login_Button()


@then('Verify iOS: REMEMBER ME or Android: REMEMBER EMAIL checkbox is in UNCHECKED State')
def verify_ios_remember_me_or_android_remember_email_checkbox_is_in_unchecked_state():
    """Verify the REMEMBER ME or Android: REMEMBER EMAIL checkbox state is TRUE."""
    time.sleep(5)
    assert loginscreen.get_rememberme() == "false"


@then('Click on the REMEMBER ME checkbox')
def click_on_the_remember_me_checkbox():
    """Click on the REMEMBER ME checkbox."""
    loginscreen.click_RememberMe_Button()


@then('Verify the REMEMBER ME or Android: REMEMBER EMAIL checkbox state is TRUE')
def verify_the_remember_me_or_android_remember_email_checkbox_state_is_true():
    """Verify the REMEMBER ME or Android: REMEMBER EMAIL checkbox state is TRUE."""
    time.sleep(5)
    assert loginscreen.get_rememberme() == "true"


@then('Click on the REMEMBER ME or Android: REMEMBER EMAIL checkbox')
def click_on_the_remember_me_or_android_remember_email_checkbox():
    """Click on the REMEMBER ME or Android: REMEMBER EMAIL checkbox."""
    loginscreen.click_RememberMe_Button()


@then('Verify the REMEMBER ME or Android: REMEMBER EMAIL checkbox state is False')
def verify_the_remember_me_or_android_remember_email_checkbox_state_is_false():
    """Verify the REMEMBER ME or Android: REMEMBER EMAIL checkbox state is False."""
    assert loginscreen.get_rememberme() == "false"


@then('Enter Email ID as <username>')
def enter_email_id_as_username(username):
    """Enter Email ID as <username>."""
    assert isinstance(username, str)
    loginscreen.enter_username(username)


@then('Enter Password as <password>')
def enter_password_as_password(password):
    """Enter Password as <password>."""
    assert isinstance(password, str)
    loginscreen.enter_password(password)


@then('Click on LOGIN Button')
def click_on_login_button():
    """Click on LOGIN Button."""
    loginscreen.click_Login_Button()


@then('Verify the Error Message displayed as <error>')
def verify_the_error_message_displayed_as_error(error):
    """Verify the Error Message displayed as <error>."""
    if Fetch_Desired_Capabilities.confirm_platform() != "Android":
        time.sleep(2)
        assert loginscreen.find_element_by_id(username_tf).get_attribute("label") == error or loginscreen.find_element_by_id(
            password_tf).get_attribute("label")
    else:
        time.sleep(2)
        error_msg_label = loginscreen.find_element_by_class_name("android.widget.TextView").get_attribute("text")
        assert error_msg_label == error


@then('Without entering username & password, Click on LOGIN Button')
def without_entering_username__password_click_on_login_button():
    """Without entering username & password, Click on LOGIN Button."""
    time.sleep(2)
    loginscreen.click_Login_Button()


@then('Verify the Error Message displayed at EMAIL Field')
def verify_the_error_message_displayed_at_email_field():
    """Verify the Error Message displayed at EMAIL Field."""
    if Fetch_Desired_Capabilities.confirm_platform() != "Android":
        loginscreen.clear_username()
        assert loginscreen.get_login_username() == "Email"
        assert loginscreen.get_login_password() == "Password"
        loginscreen.click_Login_Button()
        time.sleep(4)
        assert loginscreen.find_element_by_id(ios_email_error_id).get_attribute("label") == "Please enter a valid email."
    else:
        loginscreen.clear_username()
        assert loginscreen.get_login_username() == "Email"
        assert loginscreen.get_login_password() == "Password"
        loginscreen.click_Login_Button()
        time.sleep(4)
        # element = driver.find_elements_by_id(android_email_error_id)
        element = loginscreen.find_elements_by_class_name("android.widget.TextView")
        for x in element:
            if x.get_attribute("text") == "Please enter a valid email.":
                assert x.get_attribute("text") == "Please enter a valid email."


@then('Verify the Error Message displayed at PASSWORD Field')
def verify_the_error_message_displayed_at_password_field():
    """Verify the Error Message displayed at PASSWORD Field."""
    if Fetch_Desired_Capabilities.confirm_platform() != "Android":
        loginscreen.clear_username()
        assert loginscreen.get_login_username() == "Email"
        assert loginscreen.get_login_password() == "Password"
        loginscreen.click_Login_Button()
        time.sleep(4)
        assert loginscreen.find_element_by_id(ios_email_error_id).get_attribute("label") == "Please enter a valid email."
        assert loginscreen.find_element_by_id(ios_input_password_error).get_attribute("label") == "Please enter a valid password."
    else:
        loginscreen.clear_username()
        assert loginscreen.get_login_username() == "Email"
        assert loginscreen.get_login_password() == "Password"
        loginscreen.click_Login_Button()
        time.sleep(4)
        element = loginscreen.find_elements_by_id(android_email_error_id)
        for x in element:
            if x.get_attribute("text") == "Please enter a valid password.":
                assert x.get_attribute("text") == "Please enter a valid password."
