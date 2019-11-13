# Created by Andrey at 11/10/2019
Feature: Test for product page
  # Enter feature description here

  Scenario: User can select Books department
    # Enter steps here
    Given Open Amazon page
    When Select Books department
    And Search for Faust
    Then Books department is selected

  Scenario: User can select Amazon Fresh department
    # Enter steps here
    Given Open Amazon page
    When Select Amazon Fresh department
    And Search product fish
    Then Amazon Fresh department is selected in departmen

 #=======================++++=============================
  Scenario: Opens amazone product , hovers over Sales and Deals, then verifies that is deals.

    # Enter steps here
    Given Open Amazon pruduct B074TBCSC8
    When hovers over Sales and Deals
    Then verifies that user sees the deals