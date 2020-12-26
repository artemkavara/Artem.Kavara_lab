Feature: Careers Page
   
  Scenario: I would like to find remote work in EPAM
    Given I am on page "Work with us"
    When I press on checkbox "Remote"
    And push the "FIND" buttom
    Then I should see the list of only remote job offers

  Scenario: I would like to define my skills
    Given I am on page "Work with us"
    When I press on "All Skills" box
    Then I should see the list of skills
  
  Scenario Outline: I would like to find job using related word
    Given I am on page "Work with us"
    When I enter <word> in "Keyword or job ID"
    Then I should see the list of offers related to <word>
  
  Examples: Keyword
    | word   |
    | python |
    | java   |
    | aaaddd |