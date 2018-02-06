@CRUD
Feature: CRUD services
  Test successfully CRUD of services

  Scenario: Verify that is possible create service
    When I POST to /services
      And I set with the following params
        | type          | hostname   | username             | password                 | deleteLockTime   |
        | __type_server | __hostname | __user_administrator | __password_administrator | __deleteLockTime |
      And I send the request
    Then I should get a response with status code 200
      And The response should be saved in database in 'services' schema
#      And The response should be have a property schema



#  Scenario: Verify that is possible retrieve service
#    Given I have a service created with the following information
#        | type           | hostname   | username      | password    | deleteLockTime |
#        | ExchangeServer | at05.local | administrator | Password123 | 10             |
#    When I set GET /service
#      | hostname   | name   | type      | version    |
#      | at05.local | Exchange Server 2013 | administrator | Password123 |
#      And I send the request


