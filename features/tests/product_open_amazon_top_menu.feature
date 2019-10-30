# Created by Andrey at 10/28/2019
Feature: Test Scenarios for functionality menu
  # Enter feature description here

  Scenario: open Best Sellers top menu and verify that new page opens

    # Enter steps here
    Given Open Amazon page
    Then click to Best Sellers menu
    Then verify that new page opens