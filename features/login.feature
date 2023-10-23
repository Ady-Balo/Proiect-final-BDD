Feature:  Verify that 'ENTER ACCOUNT INFORMATION' is visible


  Scenario: I want to register
    Given I am on the home page
    When Click on 'Signup / Login ' button
    Then 'New User Signup!' is visible


  Scenario: I  fill in the username and email to signup
    When I enter a valid username and a valid email address
    And I click Signup
    Then 'ENTER ACCOUNT INFORMATION' is visible








