"""Verify bookmark conversation feature feature tests."""

from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)
from selenium.common.exceptions import NoSuchAttributeException

from Base_Capabilities.Sender_Driver_Initialization import messages_screen
from Locators.Android_Locators import messages_screen as ms
from selenium.common.exceptions import WebDriverException


@scenario('bookmark_conversation.feature', '01 Bookmack multiple conversations of a contact')
def test_bookmack_multiple_conversations_of_a_contact():
    """01 Bookmack multiple conversations of a contact."""
    return


@scenario('bookmark_conversation.feature', '02 Remove Bookmark multiple conversations of a contact')
def test_remove_bookmark_multiple_conversations_of_a_contact():
    """02 Remove Bookmark multiple conversations of a contact."""
    return


@given('The application is launched')
def the_application_is_launched():
    """The application is launched."""
    pass


@when('The current screen is a messages screen')
def the_current_screen_is_a_messages_screen():
    """The current screen is a messages screen."""
    pass


@then('01 Click a contact conversation')
def click_a_contact_conversation():
    """01 Click a contact conversation."""
    messages_screen.click_contact_message("Tharun")


@then('02 Select multiple messages')
def select_multiple_messages():
    """02 Select multiple messages."""
    last_message = messages_screen.fetch_a_specific_message_by_its_index(-1)
    messages_screen.longpress(last_message)
    second_message_from_last = messages_screen.fetch_a_specific_message_by_its_index(-2)
    messages_screen.longpress(second_message_from_last)
    third_message_from_last = messages_screen.fetch_a_specific_message_by_its_index(-3)
    messages_screen.longpress(third_message_from_last)


@then('03 Click on bookmark button')
def click_on_bookmark_button():
    """03 Click on bookmark button."""
    messages_screen.click_save_bookmarks_button()


@then('04 Verify the bookmark icon on the messages')
def verify_the_bookmark_icon_on_the_messages():
    """04 Verify the bookmark icon on the messages."""
    messages_screen.fetch_bookmark_icons_count(3)


@then('05 Navigate to SAVED BOOKMARKS')
def navigate_to_saved_bookmarks():
    """05 Navigate to SAVED BOOKMARKS."""
    last_message = messages_screen.fetch_a_specific_message_by_its_index(-1).text
    second_message_from_last = messages_screen.fetch_a_specific_message_by_its_index(-2).text
    third_message_from_last = messages_screen.fetch_a_specific_message_by_its_index(-3).text
    messages_screen.click_saved_bookmarks()
    last_bookmarked_message = messages_screen.fetch_a_specific_message_by_its_index(-1).text
    second_bookmarked_message_from_last = messages_screen.fetch_a_specific_message_by_its_index(-2).text
    third_bookmarked_message_from_last = messages_screen.fetch_a_specific_message_by_its_index(-3).text

    print("Last Sent Message :: ", last_message)
    print("Last Bookmarked Message :: ", last_bookmarked_message)
    assert last_message == last_bookmarked_message
    assert second_message_from_last == second_bookmarked_message_from_last
    assert third_message_from_last == third_bookmarked_message_from_last


@then('06 Verify that the bookmarked messages are displayed in the SAVED BOOKMARKS SCREEN')
def verify_that_the_bookmarked_messages_are_displayed_in_the_saved_bookmarks_screen():
    """06 Verify that the bookmarked messages are displayed in the SAVED BOOKMARKS SCREEN."""
    pass


@then('07 Click on back key on the app')
def click_on_back_key_on_the_app():
    """07 Click on back key on the app."""
    messages_screen.tap_back_key()


@then('08 Remove bookmarks')
def remove_bookmarks():
    """08 Remove bookmarks."""
    last_message = messages_screen.fetch_a_specific_message_by_its_index(-1)
    messages_screen.longpress(last_message)
    second_message_from_last = messages_screen.fetch_a_specific_message_by_its_index(-2)
    messages_screen.longpress(second_message_from_last)
    third_message_from_last = messages_screen.fetch_a_specific_message_by_its_index(-3)
    messages_screen.longpress(third_message_from_last)
    messages_screen.click_save_bookmarks_button()


@then('09 Verify that the bookmark icons are disappearing')
def verify_that_the_bookmark_icons_are_disappearing():
    """09 Verify that the bookmark icons are disappearing."""
    messages_screen.verify_element_not_displayed(ms.get("bookmark_img"))


@then('10 Verify that the previously bookmarked messages are removed')
def verify_that_the_previously_bookmarked_messages_are_removed():
    """10 Verify that the previously bookmarked messages are removed."""
    pass
