"""Sender should not be able to send a message to a Receiver who blocked the current sender feature tests."""
import time

from appium.webdriver.common.appiumby import AppiumBy
from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)

from Base_Capabilities.App_Credentials import *
from Base_Capabilities.Sender_Driver_Initialization import *


@scenario('send_message_to_a_receiver_who_blocked_current_contact.feature', 'Try sending a message to a Receiver who blocked the current sender')
def test_try_sending_a_message_to_a_receiver_who_blocked_the_current_sender():
    """Try sending a message to a Receiver who blocked the current sender."""
    return


@given('The application is launched')
def the_application_is_launched():
    """The application is launched."""
    pass


@when('The current screen is a messages screen')
def the_current_screen_is_a_messages_screen():
    """The current screen is a messages screen."""
    pass


@then('Try sending a message to the Receiver who blocked the current sender')
def try_sending_a_message_to_the_receiver_who_blocked_the_current_sender():
    """Try sending a message to the Receiver who blocked the current sender."""
    messages_screen.click_contact_message(receiver_contact)
    messages_screen.type_message("Sending message to a contact who blocked me!!")
    messages_screen.send_button().click()
    time.sleep(3)
    blockedContacts.click_block_alert_ok_button(receiver_contact)
    #
    # ok_button = messages_screen.find_element(AppiumBy.ID, block_alert_dialog.get("ok_button"))
    # ok_button.click()



@then('Verify that the last sent message is not same as the current send message')
def verify_that_the_last_sent_message_is_not_same_as_the_current_send_message():
    """Verify that the last sent message is not same as the current send message."""
    assert messages_screen.fetch_recently_sent_message() != "Sending message to a contact who blocked me!!"

