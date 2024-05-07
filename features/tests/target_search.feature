# Created by kervynrivero at 5/6/24
Feature: Target search test
  # Enter feature description here
  Scenario: User can search for a coffee
    Given Open Target main page
    When Search for coffee
    Then Verify search results are shown for coffee

  Scenario: User can search for a tea
    Given Open Target main page
    When Search for tea
    Then Verify search results are shown for tea

 Scenario: Adding product to cart Verification
    Given Open Target main page
    When Search for coffee
    When Adding product to cart
    Then Verify product in our cart in cart page
