"""Receiver should be able to unblock the contact feature tests."""

from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)

from Base_Capabilities.Receiver_Driver_Initialization import *
from Locators.Android_Locators import messages_screen as ms


@scenario('unblock_the_contact.feature', 'Try unblock the contact')
def test_try_unblock_the_contact():
    """Try unblock the contact."""
    return


@given('The application is launched')
def the_application_is_launched():
    """The application is launched."""
    pass


@when('The current screen is a messages screen')
def the_current_screen_is_a_messages_screen():
    """The current screen is a messages screen."""
    pass


@then('Open the notification panel and clear the notifications')
def open_the_notification_panel_and_clear_the_notifications():
    """Open the notification panel and clear the notifications."""
    pass


@then('Tap on back key on the screen')
def tap_on_back_key_on_the_screen():
    """Tap on back key on the screen."""
    receiver_messages_screen.tap_back_key()


@then('Unblock the sender')
def unblock_the_sender():
    """Unblock the sender."""
    try:
        receiver_messages_screen.click_block_button_button()
        assert receiver_messages_screen.fully_block_state() == "true"
    except:
        assert receiver_messages_screen.no_block_state() == "false"

    receiver_messages_screen.noblock().click()

    receiver_messages_screen.block_ok_button()
    receiver_messages_screen.verify_element_not_displayed(ms.get("block_text"))

