# Created by Andrey at 10/6/2019
Feature: Test Scenarios for functionality cart icon
  # Enter feature description here

  Scenario: open amazon page and verifies that cart is present

    Given Open Amazon page
    When Click on cart icon
    Then verifies that Your Shopping Cart is empty is present