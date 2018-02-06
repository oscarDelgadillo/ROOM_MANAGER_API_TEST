@smoke
Feature: Information smoke test
  Validate service retrieving information

  Scenario: Get information from Room Manager server
    Given I have room manager server up
    When I set GET to /info
      And I send the request
    Then I should get a response with status code 200