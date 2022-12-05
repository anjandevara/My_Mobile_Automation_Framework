Feature: Verifying the whether user is able to UNPIN a conversation
  Scenario: 01 Try to UNPIN a conversation
    Given The application is launched
    When The current screen is a messages screen
    Then 01 Select the top three messages
    Then 02 Click on pin button
    Then 03 Verify the pin icons displayed on the conversations