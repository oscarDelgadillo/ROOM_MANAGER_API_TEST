@CRUD
Feature: CRUD services
  Test successfully CRUD of services

  @remove_service_after
  Scenario: Verify that is possible create services
    When I POST to /services
      And I set with the following params for a services
        | type          | hostname   | username             | password                 | deleteLockTime     |
        | __TYPE_SERVER | __HOSTNAME | __USER_ADMINISTRATOR | __PASSWORD_ADMINISTRATOR | __DELETE_LOCK_TIME |
      And I send the request
    Then I should get a response with status code 200
      And The response should be saved in database in services schema
#      And The response should be have a property schema


#
#  Scenario: Verify that is possible retrieve service
#    Given I have a service created with the following information
#      | type          | hostname   | username             | password                 | deleteLockTime     |
#      | __TYPE_SERVER | __HOSTNAME | __USER_ADMINISTRATOR | __PASSWORD_ADMINISTRATOR | __DELETE_LOCK_TIME |
#      And I keep the response as $response for later step
#    When I GET /service
#      And I set with the following params
#        | hostname     | name                 | type           | version               |
#        | 10.28.133.16 | Exchange Server 2013 | ExchangeServer | 15.0 (Build 30516.32) |
#      And I send the request
#    Then I should get a response with status code 200
#      And The response should be equal to database service schema
##      And The response should be have a property schema
##  I should get a response equal to response with the service created previously

