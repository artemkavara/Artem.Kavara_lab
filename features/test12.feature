Feature: Contact Form

  Scenario: I would like to determine topic of request
    Given I am on page "Contact Us"
    When I click on first field of the form
    Then I should see the drop-down list of topics

  Rule: The "Email" and "Phone" fields couldn't be left blank

    Scenario: I would like to leave contact information
      Given I am on page "Contact Us"
      When I am trying to push "SUBMIT" button with blank "Email" and "Phone" fields
      Then the system should return alert
      And the form should not be sent