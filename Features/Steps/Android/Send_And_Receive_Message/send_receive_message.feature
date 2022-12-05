Feature: Verifying sending a message
  Scenario: 01 Verifying sending a message
    Given The application is launched
    When The current screen is a messages screen
    Then 01 Click an existing contact coversation
    Then 02 Send a message