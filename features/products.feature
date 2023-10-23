Feature: Add product
  # Verificam produsele adaugate in cart

  Scenario: Verify Product quantity in Cart
    Given I am on the home page
    When I click the Man  button
    When I click the Tshirt  button
    And I select TShirt view product button
    When I enter quantity and click Add to Cart button
    When I click View cart alert
    Then I find the quantity button and click to modify