@crud
Feature: Delete services using service ID

  Scenario: This scenario verify Delete by ID
    Given Given I have a Service Created with this data:
      | hostname   | username     | password          | type          | deleteLockTime     |
      | __HOSTNAME | __USER_NAME1 | __COMMON_PASSWORD | __TYPE_SERVER | __DELETE_LOCK_TIME |
      And I keep service_id as __ServId
    When I DELETE to /services/__ServId
      And I send the request
    Then I should get a response with status code 200
     And The response should say service "NotFound"

