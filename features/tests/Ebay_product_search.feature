# Created by Andrey at 12/3/2019
Feature: Test Scenarios for functionality
  # Enter feature description here

  Scenario: Search led on site and check it on the page
    # Enter steps here
    Given Open Ebay page
    When Input led in Ebay_search field and click
    And click on Ebay_search field
    Then Verify led is present on the page
