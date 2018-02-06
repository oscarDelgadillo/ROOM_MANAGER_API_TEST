@smoke
Feature: Validate Rooms service availability
  Test /rooms endpoint service availability

  Scenario: Verify retrieving of Rooms
    When I set GET to /rooms
      And I set the following params
      | from                     | to                       | status |
      | 2017-09-21T20:00:00.000Z | 2018-02-02T20:30:00.000Z | free   |
      And I send the request
    Then I should get a response with status code 200