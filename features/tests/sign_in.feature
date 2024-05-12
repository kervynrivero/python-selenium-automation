Feature: Sign In Verification
  Scenario: Verify logged out user nav to Sign In
    Given Open Target main page
    When Click on Sign in
    When Click Sign in from dropdown
    Then Verify Sign in form opened