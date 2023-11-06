Feature: Search product visibility

  Scenario: Search product

    Given I am on the home page
    And I verify that home page is visible successfully
    And I click on 'Products' button
    And I verify user is navigated to ALL PRODUCTS page successfully
    When I enter product name in search input and click search button
    And I verify 'SEARCHED PRODUCTS' is visible
    Then I verify all the products related to search are visible