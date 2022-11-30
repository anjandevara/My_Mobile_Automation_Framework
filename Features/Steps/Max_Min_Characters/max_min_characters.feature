Feature: Verifying the maximum and minimum characters that can be sent through a message
  Scenario: 01 Verifying send button state without sending the message
    Given The application is launched
    When The current screen is a messages screen
    Then 01 Click an existing contact coversation
    Then 02 Verify the Send Button State

  Scenario Outline: 02 Verify the maximum and minimum characters that can be sent through a message
    Given The application is launched
    When The current screen is a messages screen
    Then 03 Enter the <characters>
    Then 04 Verify the <button_state>

    Examples: Characters length
    | characters | button_state |
    |            | true         |
    |A           | true         |
    |Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis p| true|
    |Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis disa p| false|