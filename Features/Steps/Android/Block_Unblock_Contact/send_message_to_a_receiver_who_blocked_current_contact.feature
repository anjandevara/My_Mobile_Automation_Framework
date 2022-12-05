Feature: Sender should not be able to send a message to a Receiver who blocked the current sender
  Scenario: Try sending a message to a Receiver who blocked the current sender
    Given The application is launched
    When The current screen is a messages screen
    Then Try sending a message to the Receiver who blocked the current sender
    Then Verify that the last sent message is not same as the current send message