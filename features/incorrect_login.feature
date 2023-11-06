Feature: Verify error 'Your email or password is incorrect!' is visible


  Scenario: I want to check login whit invalid credentials
    When Click on 'Signup / Login ' button
    When Verify 'Login to your account' is visible
    When Enter invalid email address and password
    When Click 'login' button
    Then Verify that 'Your email or password is incorrect!' is visible