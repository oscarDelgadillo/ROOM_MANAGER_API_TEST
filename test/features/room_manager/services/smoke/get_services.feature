@smoke
Feature: Services smoke test
  Validate service retrieving Services

  Scenario: Get Room Manager Services
    Given I GET to /services
    When I set the following params :
      | hostname   | name          | type          | version          |
      | __HOSTNAME | __NAME_SERVER | __TYPE_SERVER | __VERSION_SERVER |
    And I send the request
    Then I should get a response with status code 200
