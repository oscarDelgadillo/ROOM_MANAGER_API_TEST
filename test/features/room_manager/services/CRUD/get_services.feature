@CRUD
Feature: GET services
  Test successfully GET method of services

  @get_service @after_delete_item
  Scenario: Verify that is possible retrieve service
    Given I have a service created with the following data:
      | hostname   | username             | password                 | type          | deleteLockTime     |
      | __HOSTNAME | __USER_ADMINISTRATOR | __PASSWORD_ADMINISTRATOR | __TYPE_SERVER | __DELETE_LOCK_TIME |
      And I keep the response as "_expected_response" from the previous step
#      And I keep service_id as __ServId
#    Given I have a service created with the following information
#      | type          | hostname   | username             | password                 | deleteLockTime     |
#      | __TYPE_SERVER | __HOSTNAME | __USER_ADMINISTRATOR | __PASSWORD_ADMINISTRATOR | __DELETE_LOCK_TIME |
#      And I keep the response as $response for later step
    When I GET to /services
#      And I set with the following params
#        | hostname   | name                 | type           | version               |
#        | __HOSTNAME | Exchange Server 2013 | ExchangeServer | 15.0 (Build 30516.32) |
      And I send the request
      And I keep the response as "_actual_response" from the previous step
    Then I should get a response with status code 200
#      And this catch
#      And The response "_expected_response" should be equal to database service schema
#      And The response should be have a property schema
#  I should get a response equal to response with the service created previously


#        And I send the request
#      And I keep the response as "_post_response" from the previous step
#      And I keep service_id as __ServId
#    Then I should get a response with status code 200
#      And I GET to /services/__ServId
#      And I send the request
#      And I keep the response as "_validate_response" from the previous step
#      And The response "_post_response" should be equal to response "_validate_response"