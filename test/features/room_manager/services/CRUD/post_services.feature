@CRUD
Feature: POST services
  Test successfully POST method of services

  @post_service @after_delete_service
  Scenario: Verify that is possible create services
    When I POST to /services
      And I set with the following params for a services
        | type          | hostname   | username             | password                 | deleteLockTime     |
        | __TYPE_SERVER | __HOSTNAME | __USER_ADMINISTRATOR | __PASSWORD_ADMINISTRATOR | __DELETE_LOCK_TIME |
      And I send the request
      And I keep the response as "_post_response" from the previous step
      And I keep service_id as __ServId
    Then I should get a response with status code 200
      And I GET to /services/__ServId
      And I send the request
      And I keep the response as "_validate_response" from the previous step
      And The response "_post_response" should be equal to response "_validate_response"
      And The response should have a valid schema_services schema



