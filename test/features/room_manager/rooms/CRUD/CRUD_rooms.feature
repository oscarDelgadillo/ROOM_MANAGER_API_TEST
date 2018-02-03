@CRUD
Feature: Retrieve Rooms
  Test successfully retrieving of Room(s)

  Scenario: Verify that is possible to retrieve free rooms
    Given I set ZnJhbmNvOlBhc3N3b3JkMTIz as credentials
      And I have a meeting POST to /meetings with the following info
      | organizer         | subject                            | body | start                    | end                      | rooms             | attendees         | optionalAttendees |
      | franco@at05.local | Create meeting to Test room status | Test | 2018-02-03T15:00:00.000Z | 2018-02-03T16:00:00.000Z | room01@at05.local | franco@at05.local | marco@at05.local  |
    When I set GET to /rooms
      And I set the following params
      | from                     | to                       | status |
      | 2018-02-03T15:00:00.000Z | 2018-02-03T16:00:00.000Z | free   |
      And I send the request
    Then I should get a response with status code 200
      And I should get an empty Json response