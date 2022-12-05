"""Verifying the delete conversation feature feature tests."""

from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)
from Base_Capabilities.Sender_Driver_Initialization import *
from Locators.Android_Locators import messages_screen as ms


@scenario('delete_conversation.feature', '01 Verify single conversation delete')
def test_verify_single_conversation_delete():
    """01 Verify single conversation delete."""
    return


@scenario('delete_conversation.feature', '02 Verify multiple conversations delete')
def test_verify_multiple_conversations_delete():
    """02 Verify multiple conversations delete."""
    return


@given('The application is launched')
def the_application_is_launched():
    """The application is launched."""
    pass


@when('The current screen is a messages screen')
def the_current_screen_is_a_messages_screen():
    """The current screen is a messages screen."""
    pass


@then('01 Delete a conversation')
def delete_a_conversation():
    """01 Delete a conversation."""
    messages_screen.select_conversation("Narayanan")
    messages_screen.click_delete_button()
    messages_screen.cancel_delete_action()

    messages_screen.select_conversation("Narayanan")
    messages_screen.click_delete_button()
    messages_screen.delete_action()



@then('02 Verify that the conversation is missing')
def verify_that_the_conversation_is_missing():
    """02 Verify that the conversation is missing."""
    messages_screen.verify_if_a_conversation_doesnot_exists("Narayanan")


@then('03 Delete multiple conversations')
def delete_multiple_conversations():
    """03 Delete multiple conversations."""
    messages_screen.select_conversation("Tharun")
    messages_screen.select_conversation("Narayanan2")
    messages_screen.click_delete_button()
    messages_screen.cancel_delete_action()

    messages_screen.select_conversation("Tharun")
    messages_screen.select_conversation("Narayanan2")
    messages_screen.click_delete_button()
    messages_screen.delete_action()


@then('04 Verify that the conversations are missing')
def verify_that_the_conversations_are_missing():
    """04 Verify that the conversations are missing."""
    if(messages_screen.start_conversation_screen_message()):
        start_conv = messages_screen.start_conversation_screen_message().text
        assert start_conv == "Start a New Conversation!"
    else:
        messages_screen.verify_if_a_conversation_doesnot_exists("Tharun")
        messages_screen.verify_if_a_conversation_doesnot_exists("Narayanan2")


