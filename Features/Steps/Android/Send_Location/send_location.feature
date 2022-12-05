Feature: Verify the location sending feature
  Scenario: 01 Verify the location sending feature
    Given The application is launched
    When The current screen is a messages screen
    Then 01 Click an existing contact coversation
    Then 02 Click on Location Button
    Then 03 Verify GEO Label
    Then 04 Click on send Button
    Then 05 Verify the word Location in the recently send message