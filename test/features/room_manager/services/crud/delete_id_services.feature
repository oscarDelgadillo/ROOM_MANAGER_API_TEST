@crud
Feature: Delete services using service ID

  Scenario: This scenario verify Delete by ID
    Given Given I have a service Created with this data:
      | hostname   | username     | password          | type          | deleteLockTime     |
      | __HOSTNAME | __USER_NAME1 | __COMMON_PASSWORD | __TYPE_SERVER | __DELETE_LOCK_TIME |
      And I keep service_id as __ServId
    When I DELETE to /services/__ServId
      And I send the request
    Then I should get a response with status code 200
      And I GET to /services/__ServId
      And I send the request
      And The response should display service "NotFound"
      And The response should have a valid schema_services schema

