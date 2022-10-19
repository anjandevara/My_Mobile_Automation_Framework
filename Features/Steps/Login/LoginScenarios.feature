Feature: Login Screen
  Scenario: Verify the login screen components
    Given The application is launched
    When Current Screen Is Login Screen
    Then Verify the Email Field Place Holder
    Then Verify the Password Field Place Holder
    Then Verify iOS: REMEMBER ME or Android: REMEMBER EMAIL checkbox is in UNCHECKED State
    Then Verify the LOGIN Button

  Scenario: Click on the Unchecked RememberMe and verify the state is TRUE
    Given The application is launched
    When Current Screen Is Login Screen
    Then Verify iOS: REMEMBER ME or Android: REMEMBER EMAIL checkbox is in UNCHECKED State
    Then Click on the REMEMBER ME checkbox
    Then Verify the REMEMBER ME or Android: REMEMBER EMAIL checkbox state is TRUE
    Then Click on the REMEMBER ME or Android: REMEMBER EMAIL checkbox
    Then Verify the REMEMBER ME or Android: REMEMBER EMAIL checkbox state is False


  Scenario Outline: Verify Error Message "Please enter a valid email." when empty Username & Valid Password are entered
    Given The application is launched
    When Current Screen Is Login Screen
    Then Enter Email ID as <username>
    Then Enter Password as <password>
    Then Click on LOGIN Button
    Then Verify the Error Message displayed as <error>

    Examples: Combinations
      | username                        | password     | error                          |
      |                                 | Qwerty@12345 | Please enter a valid email.    |
      | abc@gmail.com                   |              | Please enter a valid password. |

  Scenario: Verify the error messages displayed when login button is clicked without entering the credentials
    Given The application is launched
    When Current Screen Is Login Screen
    Then Without entering username & password, Click on LOGIN Button
    Then Verify the Error Message displayed at EMAIL Field
    Then Verify the Error Message displayed at PASSWORD Field