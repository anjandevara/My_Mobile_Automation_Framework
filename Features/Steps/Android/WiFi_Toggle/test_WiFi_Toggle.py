"""Verify whether the user is able to send a message when the WiFi State is toggle to On or Off. feature tests."""
import time

from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)
from selenium.common.exceptions import WebDriverException, NoSuchAttributeException

from Base_Capabilities.Receiver_Driver_Initialization import receiver_messages_screen
from Base_Capabilities.Sender_Driver_Initialization import messages_screen, device1


@scenario('WiFi_Toggle.feature', '01 Try sending a message when WiFi is ON')
def test_try_sending_a_message_when_wifi_is_on():
    """01 Try sending a message when WiFi is ON."""
    return


@scenario('WiFi_Toggle.feature', '02 Try sending a message when WiFi is OFF')
def test_try_sending_a_message_when_wifi_is_off():
    """02 Try sending a message when WiFi is OFF."""
    return


@scenario('WiFi_Toggle.feature', '03 Turn On the WiFi and try send the message')
def test_turn_on_the_wifi_and_try_send_the_message():
    """03 Turn On the WiFi and try send the message."""
    return


@given('The application is launched')
def the_application_is_launched():
    """The application is launched."""
    pass


@when('Current Screen Is Login Screen')
def current_screen_is_login_screen():
    """Current Screen Is Login Screen."""
    pass


@then('01 Select a conversation of contact')
def select_a_conversation_of_contact():
    """01 Select a conversation of contact."""
    messages_screen.click_contact_message("Tharun")


@then('02 Send a message')
def send_a_message():
    """02 Send a message."""
    messages_screen.type_message("This message is sent when the WiFi is ON!!")
    messages_screen.send_button().click()


@then('03 Verify the last sent message')
def verify_the_last_sent_message():
    """03 Verify the last sent message."""
    time.sleep(15)
    assert messages_screen.fetch_recently_sent_message() == "This message is sent when the WiFi is ON!!"


@then('04 On the receiver side verify the last message received')
def on_the_receiver_side_verify_the_last_message_received():
    """04 On the receiver side verify the last message received."""
    receiver_messages_screen.click_contact_message("Anjan Innominds")
    assert receiver_messages_screen.fetch_recently_received_message() == "This message is sent when the WiFi is ON!!"


@then('05 On the sender side turn off the WiFi')
def on_the_sender_side_turn_off_the_wifi():
    """05 On the sender side turn off the WiFi."""
    messages_screen.toggle_wifi_off(device1)


@then('06 Send a message')
def send_a_message():
    """06 Send a message."""
    messages_screen.type_message("This message is sent when the WiFi is Toggled!!")
    messages_screen.send_button().click()


@then('07 Verify the failed message elements')
def verify_the_failed_message_elements():
    """07 Verify the failed message elements."""
    time.sleep(3)
    assert messages_screen.resend_text().text == "Resend"
    assert messages_screen.error_failed_msg().is_displayed()
    assert messages_screen.msg_failed().text == "Message failed"


@then('08 Turn on the WiFi')
def turn_on_the_wifi():
    """08 Turn on the WiFi."""
    messages_screen.toggle_wifi_on(device1)


@then('09 Click on Resend Button')
def click_on_resend_button():
    """09 Click on Resend Button."""
    time.sleep(15)
    messages_screen.click_resend_button()


@then('10 Verify that the Resend button has disappeared')
def verify_that_the_resend_button_has_disappeared():
    """10 Verify that the Resend button has disappeared."""
    try:
        if (messages_screen.resend_icon().is_displayed):
            raise ValueError("Resend Icon Still Exists!!")
    except WebDriverException as WDE:
        if WDE.msg == "NoSuchElementError":
            pass


@then('11 Verify the recently sent message on the sender side')
def verify_the_recently_sent_message_on_the_sender_side():
    """11 Verify the recently sent message on the sender side."""
    assert messages_screen.fetch_recently_sent_message() == "This message is sent when the WiFi is Toggled!!"


@then('12 Verify the recently received message on the receiver side')
def verify_the_recently_received_message_on_the_receiver_side():
    """12 Verify the recently received message on the receiver side."""
    time.sleep(5)
    assert receiver_messages_screen.fetch_recently_received_message() == "This message is sent when the WiFi is Toggled!!"
