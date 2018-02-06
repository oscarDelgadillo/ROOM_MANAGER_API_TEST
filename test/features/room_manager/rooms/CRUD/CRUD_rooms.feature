@CRUD
Feature: Retrieve Rooms
  Test successfully retrieving of Room(s)

  Background:
    Given I set ZnJhbmNvOlBhc3N3b3JkMTIz as credentials
    And I POST to /meetings
    And I set the following meeting info
      | organizer         | subject                            | body | start                    | end                      | rooms             | attendees         | optionalAttendees |
      | franco@at05.local | Create meeting to Test room status | Test | 2018-02-09T15:00:00.000Z | 2018-02-09T16:00:00.000Z | room01@at05.local | franco@at05.local | marco@at05.local  |
    And I send the request
    And I keep the "id" as "after_item_id" from JSON response

    @bug
#  Scenario: Verify that is possible to retrieve free rooms
#    When I set GET to /rooms
#    And I set the following params
#      | from                     | to                       | status |
#      | 2018-02-09T15:00:00.000Z | 2018-02-09T16:00:00.000Z | free   |
#    And I send the request
#    Then I should get a response with status code 200
#    And I should get an empty Json response

    @bug
  Scenario: Verify that is possible to retrieve busy rooms
    When I set GET to /rooms
    And I set the following params
      | from                     | to                       | status |
      | 2018-02-09T15:00:00.000Z | 2018-02-09T16:00:00.000Z | free   |
    And I send the request
    Then I should get a response with status code 200
    And The response should be equal in data base rooms schema
    And The response should have a valid rooms schema
#
#  Scenario: Verify that is possible to retrieve room by Id
#    When I set GET to /rooms
#    And I have obtained roomsId of the database
#    And I send the request
#    Then I should get a response with status code 200
#    And The response should be equal in data base rooms schema
#    And The response should have a valid rooms schema