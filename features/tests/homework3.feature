Feature: Target cart is empty Test
  Scenario:  Verify if "Your cart is empty" message appears
    Given Open Target main page
    When Click on cart icon
    Then Verify the cart empty message

  Scenario: Verify logged out user nav to Sign In
    Given Open Target main page
    When Click on Sign in
    When Click Sign in from dropdown
    Then Verify Sign in form opened