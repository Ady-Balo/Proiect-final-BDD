Feature: Test the signup form
  In order to create a new account
  As a user
  I want to be able to create a new account

  Scenario: I submit a filled form and confirm I have a new account
    Given I am on the signup page
    When I fill the title, password and data birth
    When Selecting  checkbox 'Sign up for our newsletter!'
    And Selecting checkbox 'Receive special offers from our partners!'
    When I fill first name, last name, address, country,state, city, zipcode, mobile Number
    And I click 'Create Account button'
    Then I verify that 'ACCOUNT CREATED!' is visible
    And  I click 'Continue' button
    Then I verify 'Logged in as username' is visible
    Then I click the 'Delete Account' button



