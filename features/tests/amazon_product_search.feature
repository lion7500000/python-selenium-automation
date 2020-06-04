# Created by Andrey at 11/29/2019
Feature: Test for Amazon search functionality
  # Enter feature description here

  Scenario: User can serach a products
    Given Open Amazon page
    When Search the product Dress
    Then Search product for "Dress" is shown