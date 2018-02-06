@crudPut
Feature: Put services using service ID

  @after_delete_service
  Scenario: This scenario verify put service by ID
    Given Given I have a Service Created with this data:
      | hostname   | username     | password          | type          |
      | __hostname | __user_marco | __common_password | __type_server |
      And I keep service_id as __ServId
    When I PUT to /services/__ServId
      And I set this change :
        | username     | password          |
        | __user_oscar | __common_password |
      And I send the request
    Then I should get a response with status code 200
      And The response should equals that Get method


