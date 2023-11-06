Feature:  Verify that 'ENTER ACCOUNT INFORMATION' is visible

  @LoginLogOut
  Scenario:Test Case 4: Logout User
    Given I am on the home page
    When Click on 'Signup / Login ' button
    And Verify 'Login to your account' is visible
    When I enter correct email address
    And I enter correct password
    When I click 'login' button
    And Verify that Logged in as username is visible
    When Click Logout button
    Then Verify that user is navigated to login page

  Scenario: I want to register
    Given I am on the home page
    When Click on 'Signup / Login ' button
    Then 'New User Signup!' is visible


  Scenario Outline: I  fill in the username and email to signup
    When I enter a valid <username> and a valid <email>
    And I click Signup
    Then 'ENTER ACCOUNT INFORMATION' is visible
    Examples:
      | email               | username |
      | p4C5Ams@example.com | Johny    |








