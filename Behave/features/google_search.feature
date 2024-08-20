Feature:Google search for TheTestingAcademy
  Scenario: search for TTA on google
    Given I am on the google search page
    When I search for the "TheTestingAcademy"
    Then I shoulf see the "TheTestingAcademy" as a result