@smoke
Feature: Services Id smoke test
  Validate service retrieving Services

  Scenario: Get Room Manager Services Id
    Given I set GET to /services
    When I set the hostname of the server "at05.local"
      And I send the request
    Then I should get a response with status code 200




