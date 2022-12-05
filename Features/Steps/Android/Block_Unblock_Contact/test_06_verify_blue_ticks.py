"""Verify the read receipt feature tests."""
import time

from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)

from Base_Capabilities.Sender_Driver_Initialization import messages_screen


@scenario('verify_the_blue_ticks.feature', 'Verify the read receipt in the form of blue ticks on the recently sent message')
def test_verify_the_read_receipt_in_the_form_of_blue_ticks_on_the_recently_sent_message():
    """Verify the read receipt in the form of blue ticks on the recently sent message."""
    return


@given('The application is launched')
def the_application_is_launched():
    """The application is launched."""
    pass


@when('The current screen is a messages screen')
def the_current_screen_is_a_messages_screen():
    """The current screen is a messages screen."""
    pass


@then('Verify the blue ticks on the recently sent message')
def verify_the_blue_ticks_on_the_recently_sent_message():
    """Verify the blue ticks on the recently sent message."""
    time.sleep(5)
    messages_screen.verify_blue_ticks_on_the_recently_sent_message()

