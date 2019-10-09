# Created by Andrey at 10/7/2019
Feature: Test Scenarios for functionality
  # Enter feature description here

  Scenario: Buy product on Amazon and check it in Card icon
    # Enter steps here
    Given Open Amazon page
    When Input iphone 11 pro into amazon_search field
    And Click on search icon_amazom
    Then click_on  item
    Then add to cart
    Then click_on  cart
    Then check 1 item on card
