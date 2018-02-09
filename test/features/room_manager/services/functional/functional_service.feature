@functional_services
Feature: Get Services Id functional testing
  Validate service by id retrieving Services

  Background:
    Given Given I have a service Created with this data:
      | hostname   | username     | password          | type          | deleteLockTime     |
      | __HOSTNAME | __USER_NAME1 | __COMMON_PASSWORD | __TYPE_SERVER | __DELETE_LOCK_TIME |
     And I keep service_id as __ServId

  @after_delete_service
  Scenario: Validate that a serviceId valid retrieving status 200
    When I GET to /services/__ServId
     And I send the request
    Then I should get a response with status code 200
     And The response should have a valid schema_services schema

  @after_delete_service
  Scenario Outline: Validate that a serviceId invalid retrieving error message
    Given I set a invalid __ServId as this <invalid_Id>
    When I GET to /services/__ServId
     And I send the request
    Then I should get a response with status code 400
      And The response should display service "BadRequest"
    Examples:
      | invalid_Id |
      | 123        |

  @after_delete_service
  Scenario Outline: Validate that send DELETE  with serviceId invalid retrieving error message
    Given I set a invalid __ServId as this <invalid_Id>
    When I DELETE to /services/__ServId
     And I send the request
    Then I should get a response with status code 400
     And The response should display service "BadRequest"
    Examples:
      | invalid_Id |
      | 123        |
      | "   "      |


  @after_delete_service
  Scenario: Validate that send PUT with deleteLockTime empty retrieving error message
    When I PUT to /services/__ServId
      And I set this change :
      | username     | password          | deleteLockTime            |
      | __USER_NAME2 | __COMMON_PASSWORD | __DELETE_LOCK_TIME_EMPTY |
    And I send the request
    Then I should get a response with status code 400
     And The response should display service "ValidationError"