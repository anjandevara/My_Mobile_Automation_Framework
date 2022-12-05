"""Verifying the send and receive message feature tests."""

from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)

from Base_Capabilities.Sender_Driver_Initialization import *


@scenario('send_receive_message.feature', '01 Verifying sending a message')
def test_verifying_sending_a_message():
    """01 Verifying sending a message."""
    return


@given('The application is launched')
def the_application_is_launched():
    """The application is launched."""
    pass


@when('The current screen is a messages screen')
def the_current_screen_is_a_messages_screen():
    """The current screen is a messages screen."""
    pass


@then('01 Click an existing contact coversation')
def click_an_existing_contact_coversation():
    """01 Click an existing contact coversation."""
    messages_screen.click_contact_message("Tharun")


@then('02 Send a message')
def send_a_message():
    """02 Send a message."""
    messages_screen.type_message("Hello, How are you?")
    messages_screen.send_button().click()


