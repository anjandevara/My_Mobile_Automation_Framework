"""Sender should be able to send the message feature tests."""

from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)

from Base_Capabilities.Sender_Driver_Initialization import *


@scenario('send_a_message.feature', 'Try sending a message')
def test_try_sending_a_message():
    """Try sending a message."""
    return


@given('The application is launched')
def the_application_is_launched():
    """The application is launched."""
    pass


@when('The current screen is a messages screen')
def the_current_screen_is_a_messages_screen():
    """The current screen is a messages screen."""
    pass


@then('Send a message')
def send_a_message():
    """Send a message."""
    messages_screen.tap_back_key()
    messages_screen.click_contact_message("Tharun")
    messages_screen.type_message("Sending a message to the contact after unblocking my phone number!!")
    messages_screen.send_button().click()

