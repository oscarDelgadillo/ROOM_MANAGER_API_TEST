@CRUD
Feature: GET services
  Test successfully GET method of services

  @get_service @after_delete_item
  Scenario: Verify that is possible retrieve service
    Given I have a service created with the following data:
      | hostname   | username             | password                 | type          | deleteLockTime     |
      | __HOSTNAME | __USER_ADMINISTRATOR | __PASSWORD_ADMINISTRATOR | __TYPE_SERVER | __DELETE_LOCK_TIME |
      And I keep the response as "_expected_response" from the previous step
    When I GET to /services
      And I send the request
      And I keep the response as "_actual_response" from the previous step
    Then I should get a response with status code 200
      And The response "_actual_response" should be contain in database services collection
      And The response should have a valid schema_services schema
