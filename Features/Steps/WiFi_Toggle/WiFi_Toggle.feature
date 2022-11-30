Feature: Verify whether the user is able to send a message when the WiFi State is toggle to On or Off.
  Scenario: 01 Try sending a message when WiFi is ON
    Given The application is launched
    When Current Screen Is Login Screen
    Then 01 Select a conversation of contact
    Then 02 Send a message
    Then 03 Verify the last sent message
    Then 04 On the receiver side verify the last message received

  Scenario: 02 Try sending a message when WiFi is OFF
    Given The application is launched
    When Current Screen Is Login Screen
    Then 05 On the sender side turn off the WiFi
    Then 06 Send a message
    Then 07 Verify the failed message elements

  Scenario: 03 Turn On the WiFi and try send the message
    Given The application is launched
    When Current Screen Is Login Screen
    Then 08 Turn on the WiFi
    Then 09 Click on Resend Button
    Then 10 Verify that the Resend button has disappeared
    Then 11 Verify the recently sent message on the sender side
    Then 12 Verify the recently received message on the receiver side