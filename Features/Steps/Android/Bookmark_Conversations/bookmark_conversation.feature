Feature: Verify bookmark conversation feature
  Scenario: 01 Bookmack multiple conversations of a contact
    Given The application is launched
    When The current screen is a messages screen
    Then 01 Click a contact conversation
    Then 02 Select multiple messages
    Then 03 Click on bookmark button
    Then 04 Verify the bookmark icon on the messages
    Then 05 Navigate to SAVED BOOKMARKS
    Then 06 Verify that the bookmarked messages are displayed in the SAVED BOOKMARKS SCREEN
    Then 07 Click on back key on the app

  Scenario: 02 Remove Bookmark multiple conversations of a contact
    Given The application is launched
    When The current screen is a messages screen
    Then 08 Remove bookmarks
    Then 09 Verify that the bookmark icons are disappearing
#    Then 05 Navigate to SAVED BOOKMARKS
    Then 10 Verify that the previously bookmarked messages are removed
