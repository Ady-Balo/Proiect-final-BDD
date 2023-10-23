Feature: Test the signup form
"""
  9. Fill details: Title, Name, Email, Password, Date of birth
  10. Select checkbox 'Sign up for our newsletter!'
  11. Select checkbox 'Receive special offers from our partners!'
  12. Fill details: First name, Last name, Company, Address, Address2, Country, State, City, Zipcode, Mobile Number
  13. Click 'Create Account button'
  14. Verify that 'ACCOUNT CREATED!' is visible
  15. Click 'Continue' button
  16. Verify that 'Logged in as username' is visible
  17. Click 'Delete Account' button
  18. Verify that 'ACCOUNT DELETED!' is visible and click 'Continue' button

  """

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



