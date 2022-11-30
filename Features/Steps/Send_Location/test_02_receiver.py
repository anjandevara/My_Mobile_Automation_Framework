"""Verifying the send and receive message feature tests."""

from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)

from Base_Capabilities.Receiver_Driver_Initialization import *


@scenario('receive_location.feature', '01 Verify the location receiving feature')
def test_verify_the_location_receiving_feature():
    """01 Verify the location receiving feature."""
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
    receiver_messages_screen.click_contact_message("Anjan Innominds")


@then('02 Verify the laste received message')
def verify_the_laste_received_message():
    """02 Verify the laste received message."""
    assert "Location:" in receiver_messages_screen.fetch_recently_sent_message()

