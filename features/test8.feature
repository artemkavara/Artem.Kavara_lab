Feature: Open Source Projects
  
  Scenario Outline: I would like to see the overview of project
    Given I pushed the buttom "Open Source" on the title page of "EPAM" website
    When I press on <num> <project> square
    Then a <page> should be opened

  Examples: Projects
    | num | project        | page           |
    | 0   | CLOUD PIPELINE | cloud-pipeline |
    | 1   | INDIGO ELN 2.0 | indigo-eln-2-0 |
    | 2   | JDI LIGHT      | jdi-light      |
