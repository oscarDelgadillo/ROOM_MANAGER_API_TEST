@smoke
Feature: Rooms smoke test
  Validate service retrieving Rooms

  Scenario: Get Rooms from Server
    Given I have rooms created
    When I GET to /rooms for rooms with the following info
      | from                     | to                       | status |
      | 2017-09-21T20:00:00.000Z | 2018-02-02T20:30:00.000Z | free   |
    Then I should get a response with status code 200