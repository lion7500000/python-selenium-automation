# Created by Andrey at 10/6/2019
Feature: Test Scenarios for functionality
  # Enter feature description here

  Scenario: User can search for Cancelling an order on Amazon

    Given Open Amazon page
    When Click on Customer Service
    Then Input cancel order into search field
    And Click on search icon
    Then Product results Cancel Items or Orders are shown
