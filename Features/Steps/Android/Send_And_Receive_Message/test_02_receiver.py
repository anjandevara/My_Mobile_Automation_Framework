"""Verifying the send and receive message feature tests."""
import time

from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)

from Base_Capabilities.Receiver_Driver_Initialization import *


@scenario('receive_message.feature', '01 Verifying receiving a message')
def test_verifying_receiving_a_message():
    """01 Verifying receiving a message."""
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
    time.sleep(5)
    receiver_messages_screen.click_contact_message("Anjan Innominds")


@then('02 Verify the laste received message')
def verify_the_laste_received_message():
    """02 Verify the laste received message."""
    assert "Hello, How are you?" in receiver_messages_screen.fetch_recently_sent_message()

