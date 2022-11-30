"""Verifying the maximum and minimum characters that can be sent through a message feature tests."""

from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)

from Base_Capabilities.Sender_Driver_Initialization import *


@scenario('send_location.feature', '01 Verify the location sending feature')
def test_verify_the_location_sending_feature():
    """01 Verify the location sending feature."""
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


@then('02 Click on Location Button')
def click_on_location_button():
    """02 Click on Location Button."""
    messages_screen.location_icon().click()


@then('03 Verify GEO Label')
def verify_geo_label():
    """03 Verify GEO Label."""
    assert messages_screen.geo_icon().is_displayed() == True


@then('04 Click on send Button')
def click_on_send_button():
    """04 Click on send Button."""
    messages_screen.send_button().click()


@then('05 Verify the word Location in the recently send message')
def verify_the_word_location_in_the_recently_send_message():
    """05 Verify the word Location in the recently send message."""
    assert "Location:" in messages_screen.fetch_recently_sent_message()
