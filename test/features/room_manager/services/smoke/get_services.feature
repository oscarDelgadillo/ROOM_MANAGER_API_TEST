@smoke
Feature: Services smoke test
  Validate service retrieving Services

  Scenario: Get Room Manager Services
    Given I GET to /services
    When I set the following params :
      | hostname   | name          | type          | version          |
      | __hostname | __name_server | __type_server | __version_server |
    And I send the request
    Then I should get a response with status code 200
