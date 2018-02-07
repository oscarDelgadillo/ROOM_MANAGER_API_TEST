@smoke
Feature: Services Id smoke test
  Validate service retrieving Services

  Scenario: Get Room Manager Services by Id
    Given I GET to /services
     And I send the request
    When I set the hostname of the server "__EXCHANGE_SERVER"
      And I send the request
    Then I should get a response with status code 200




