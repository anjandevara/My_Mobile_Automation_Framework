Feature: Verifying the delete conversation feature
  Scenario: 01 Verify single conversation delete
    Given The application is launched
    When The current screen is a messages screen
    Then 01 Delete a conversation
    Then 02 Verify that the conversation is missing

  Scenario: 02 Verify multiple conversations delete
    Given The application is launched
    When The current screen is a messages screen
    Then 03 Delete multiple conversations
    Then 04 Verify that the conversations are missing