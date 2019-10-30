# Created by Andrey at 10/27/2019
Feature: Test Scenarios for functionality sign and card
  # Enter feature description here

  Scenario: User can open and close Today's deals under $25 [update scenario name]
    # Enter steps here
    Given Open Amazon page
    When Store original windows
    And Click to open Deals under $25
    And Switch to the newly opened window
    Then Search Today's Deals are shown
    Then steps to put any product into a cart
    And User can close new window and switch back to original
    Then Add a step to refresh the page
    Then Add a step to verify cart has 1 item
