@crudPut
Feature: Put services using service ID

  @after_delete_service
  Scenario: This scenario verify put service by ID
    Given Given I have a Service Created with this data:
      | hostname   | username     | password          | type          | deleteLockTime     |
      | __HOSTNAME | __USER_MARCO | __COMMON_PASSWORD | __TYPE_SERVER | __DELETE_LOCK_TIME |
      And I keep service_id as __ServId
    When I PUT to /services/__ServId
     And I set this change :
       | username     | password          |
       | __USER_OSCAR | __COMMON_PASSWORD |
    And I send the request
    Then I should get a response with status code 200
    And The answer should be the same as the answer Get method
      #And The json responce should be valido with its scheme



