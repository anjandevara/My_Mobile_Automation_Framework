"""Verify receiver is able to block a contact feature tests."""
import time

from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)

from Base_Capabilities.Receiver_Driver_Initialization import *

@scenario('block_contact_on_receiver_side.feature', '01 Block a contact on receiver side')
def test_block_a_contact_on_receiver_side():
    """01 Block a contact on receiver side."""
    return


@given('The application is launched')
def the_application_is_launched():
    """The application is launched."""
    pass


@when('The current screen is a messages screen')
def the_current_screen_is_a_messages_screen():
    """The current screen is a messages screen."""
    pass


@then('01 Click a conversation')
def click_a_conversation():
    """01 Click a conversation."""
    receiver_messages_screen.click_contact_message("Anjan Innominds")


@then('02 Block the contact')
def block_the_contact():
    """02 Block the contact."""

    try:
        receiver_messages_screen.click_block_button_button()
        assert receiver_messages_screen.no_block_state() == "true"
    except:
        assert receiver_messages_screen.no_block_state() == "false"
        return

    receiver_messages_screen.fully_block().click()

    receiver_messages_screen.block_ok_button()
    receiver_messages_screen.verify_contact_blocked_state()

