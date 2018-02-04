@smoke
Feature: Services smoke test
  Validate service retrieving Services

  Scenario: Get Room Manager Services
    Given I set GET to /services
    When I set the following params :
      | hostname   | name                 | type           | version               |
      | at05.local | Exchange Server 2013 | ExchangeServer | 15.0 (Build 30516.32) |
      And I send the request
    Then I should get a response with status code 200



