"""Verifying the maximum and minimum characters that can be sent through a message feature tests."""
import time

from pytest_bdd import (
    given,
    scenario,
    then,
    when, parsers,
)

from Base_Capabilities.Sender_Driver_Initialization import *


@scenario('max_min_characters.feature', '01 Verifying send button state without sending the message')
def test_verifying_send_button_state_without_sending_the_message():
    """01 Verifying send button state without sending the message."""
    return


@scenario('max_min_characters.feature', '02 Verify the maximum and minimum characters that can be sent through a message')
def test_verify_the_maximum_and_minimum_characters_that_can_be_sent_through_a_message():
    """02 Verify the maximum and minimum characters that can be sent through a message."""
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
    time.sleep(3)
    messages_screen.click_contact_message("Narayanan")


@then('02 Verify the Send Button State')
def verify_the_send_button_state():
    """02 Verify the Send Button State."""
    time.sleep(3)
    assert messages_screen.send_button_state() == "true"
    # assert messages_screen.send_button_state() == "false"


@then(parsers.parse('03 Enter the {characters}'))
def enter_the_characters(characters):
    """03 Enter the <characters>."""
    messages_screen.type_message(characters)
    messages_screen.send_button().click()


@then(parsers.parse('04 Verify the {button_state}'))
def verify_the_button_state(button_state):
    """04 Verify the <button_state>."""
    assert messages_screen.send_button_state() == button_state

