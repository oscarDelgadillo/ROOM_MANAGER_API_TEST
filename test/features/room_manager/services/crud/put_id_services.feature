@crudPut
Feature: Put services using service ID

  @after_delete_service
  Scenario: This scenario verify put service by ID
    Given Given I have a service Created with this data:
      | hostname   | username     | password          | type          | deleteLockTime     |
      | __HOSTNAME | __USER_NAME1 | __COMMON_PASSWORD | __TYPE_SERVER | __DELETE_LOCK_TIME |
      And I keep service_id as __ServId
    When I PUT to /services/__ServId
     And I set this change :
       | username     | password          |deleteLockTime     |
       | __USER_NAME2 | __COMMON_PASSWORD |__DELETE_LOCK_TIME |
    And I send the request
    Then I should get a response with status code 200
      And I keep the data changed as "__data_changed"
      And I save the json response got from get services as "__new_data"
      And I compare json response "__data_changed" between "__new_data"
      And The response should have a valid schema_services schema




