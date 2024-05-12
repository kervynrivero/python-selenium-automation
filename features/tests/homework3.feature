Feature: Target cart is empty Test
  Scenario:  Verify if "Your cart is empty" message appears
    Given Open Target main page
    When Click on cart icon
    Then Verify the cart empty message
