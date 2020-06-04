# Created by Andrey at 10/7/2019
Feature: Test Scenarios for functionality
  # Enter feature description here

  Scenario: Buy product on Amazon and check it in Card icon
    # Enter steps here
    Given Open Amazon page
    When Input iphone 11 pro into amazon_search field
    And Click on search icon_amazom
    Then Click on  item
    Then Add to cart
    Then Click on cart icon btn
    Then Verify shopping cart has 1 item
