@smoke
Feature: Services Id smoke test
  Validate service retrieving Services

  Scenario: Get Room Manager Services Id
    Given I have room manager server up
    When I set GET to /services
    And I set the service ID "5a724a899390bb1630a9be1d"
    Then I should get a response with status code 200




