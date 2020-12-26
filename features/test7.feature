Feature: Sharing information
  
  Scenario Outline: I would like to share some information
    Given I am on page with brochures
    When I push on a <button>
    Then a <site> window should be opended

  Examples:
    | button | site         |
    | 0      | twitter.com  |
    | 1      | facebook.com |
    | 2      | linkedin.com |