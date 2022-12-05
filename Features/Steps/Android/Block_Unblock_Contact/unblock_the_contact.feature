Feature: Receiver should be able to unblock the contact
  Scenario: Try unblock the contact
    Given The application is launched
    When The current screen is a messages screen
    Then Unblock the sender
    Then Tap on back key on the screen
    Then Open the notification panel and clear the notifications