"""Verifying the maximum and minimum characters that can be sent through a message feature tests."""
import time

from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)

from Base_Capabilities.Sender_Driver_Initialization import *


@scenario('pin_contacts.feature', '01 Try to PIN a conversation')
def test_try_to_pin_a_conversation():
    """01 Try to PIN a conversation."""
    return


@given('The application is launched')
def the_application_is_launched():
    """The application is launched."""
    pass


@when('The current screen is a messages screen')
def the_current_screen_is_a_messages_screen():
    """The current screen is a messages screen."""
    pass


@then('01 Select the top three messages')
def select_the_top_three_messages():
    """01 Select the top three messages."""
    messages_screen.select_top_3_messages()




@then('02 Click on pin button')
def click_on_pin_button():
    """02 Click on pin button."""
    time.sleep(3)
    messages_screen.click_pin_button()


@then('03 Verify the pin icons displayed on the conversations')
def verify_the_pin_icons_displayed_on_the_conversations():
    """03 Verify the pin icons displayed on the conversations."""
    messages_screen.fethc_pin_icons_count(3)

