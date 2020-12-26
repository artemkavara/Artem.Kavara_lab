Feature: Search Engine
  
  Scenario: I would like to search some info about EPAM
    Given I am on EPAM website
    When I press "Search" buttom
    Then I should see a text field
    And I should see a buttom "Find"