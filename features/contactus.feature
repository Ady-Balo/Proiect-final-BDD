Feature: Contact Us form


  @test
  Scenario: Contact page verifying
    Given I am on the home page
    When Click on 'Contact Us' button
    And Verify 'GET IN TOUCH' is visible
    And Enter name, email, subject and message
    And Upload file
    Then Click 'Submit' button
    Then Click on alert button
    And Verify success message 'Success! Your details have been submitted successfully.' is visible
    Then Click 'Home' button and verify that landed to home page successfully


# behave -t=test



