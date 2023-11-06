@ScrollFunctionality

Feature:Scroll  functionality

  Scenario:Test Case 25: Verify Scroll Up using 'Arrow' button and Scroll Down functionality
    Given I am on the home page
    And I verify that home page is visible successfully
    And Scroll down page to bottom
    And Verify text SUBSCRIPTION
    And Click on arrow at bottom right side to move upward
    Then Verify that page is scrolled up to top and Full-Fledged practice website is visible

  @ScrollMagic

  Scenario:Test Case 26: Verify Scroll Up without 'Arrow' button and Scroll Down functionality
    Given I am on the home page
    And I verify that home page is visible successfully
    And Scroll down page to bottom
    And Verify text SUBSCRIPTION
    And Scroll up page to top
    Then Verify that page is scrolled up to top and Full-Fledged practice website is visible