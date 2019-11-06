# Created by Andrey at 9/30/2019
Feature: Test Scenarios for Search functionality


  Scenario: Logged out user sees Sign in page when clicking Orders
    Given Open Amazon page
    #When Click on search item
    When Click Amazon Orders link
    Then Product results for Sign-In are open