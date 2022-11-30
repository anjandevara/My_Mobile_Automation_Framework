Feature: Verifying receiving a message
  Scenario: 01 Verifying receiving a message
    Given The application is launched
    When The current screen is a messages screen
    Then 01 Click an existing contact coversation
    Then 02 Verify the laste received message