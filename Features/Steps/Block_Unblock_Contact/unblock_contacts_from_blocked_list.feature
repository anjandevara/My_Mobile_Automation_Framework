Feature: Unblock the contacts from the blocked list
  Scenario: Unblock the contacts from the blocked list
    Given The application is launched
    When The current screen is a messages screen
    Then 01 Click a conversation
    Then 02 Block any two contacts
    Then 03 Try sending a message to the Receiver
    Then 04 Try sending a message to the Sender
    Then 05 Navigate to Settings and unblock the contacts
    Then 06 Send a message
    Then 07 Open the notification panel and access the WAVE Notification
    Then 08 Verify the current name and recently received message


