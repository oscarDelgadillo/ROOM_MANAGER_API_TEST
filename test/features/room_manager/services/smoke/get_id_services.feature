@smoke
Feature: Services Id smoke test
  Validate service retrieving Services

  Scenario: Get Room Manager Services Id
    Given I GET to /services
    When I set the hostname of the server "__exchange_server"
      And I send the request
    Then I should get a response with status code 200




