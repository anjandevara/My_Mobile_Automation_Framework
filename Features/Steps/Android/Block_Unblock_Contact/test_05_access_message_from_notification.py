"""Receiver should get a notification on receiving a message feature tests."""

from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)

from Base_Capabilities.Receiver_Driver_Initialization import receiver_messages_screen


@scenario('access_notification.feature', 'Tty accessing the notitfication')
def test_tty_accessing_the_notitfication():
    """Tty accessing the notitfication."""
    return


@given('The application is launched')
def the_application_is_launched():
    """The application is launched."""
    pass


@when('The current screen is a messages screen')
def the_current_screen_is_a_messages_screen():
    """The current screen is a messages screen."""
    pass


@then('01 Open the notification panel and access the WAVE Notification')
def open_the_notification_panel_and_access_the_wave_notification():
    """01 Open the notification panel and access the WAVE Notification."""
    receiver_messages_screen.fetch_wave_notification("Anjan Innominds")


@then('02 Verify the current name and recently received message')
def verify_the_current_name_and_recently_received_message():
    """02 Verify the current name and recently received message."""
    assert receiver_messages_screen.fetch_recently_sent_message() == "Sending a message to the contact after unblocking my phone number!!"

