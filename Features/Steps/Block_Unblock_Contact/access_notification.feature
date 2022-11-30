Feature: Receiver should get a notification on receiving a message
  Scenario: Tty accessing the notitfication
    Given The application is launched
    When The current screen is a messages screen
    Then 01 Open the notification panel and access the WAVE Notification
    Then 02 Verify the current name and recently received message