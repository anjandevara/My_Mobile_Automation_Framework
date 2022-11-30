Feature: Verify the read receipt
  Scenario: Verify the read receipt in the form of blue ticks on the recently sent message
    Given The application is launched
    When The current screen is a messages screen
    Then Verify the blue ticks on the recently sent message