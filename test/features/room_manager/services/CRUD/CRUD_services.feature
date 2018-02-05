#@CRUD
#Feature: CRUD services
#  Test successfully CRUD of services

#  Scenario: Verify that is possible create service
#    When I set POST to /services
#      And I set with the following params
#        | type           | hostname   | username      | password    | deleteLockTime |
#        | ExchangeServer | at05.local | administrator | Password123 | 10             |
#      And I send the request
#    Then I should get a response with status code 200
#      And I response should be equal in the database
