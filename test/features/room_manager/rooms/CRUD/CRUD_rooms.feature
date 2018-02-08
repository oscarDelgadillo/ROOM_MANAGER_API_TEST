@CRUD
Feature: Retrieve Rooms
  Test successfully retrieving of Room(s)

  Background:
    Given I send '__CREDENTIALS_USER1' as credentials
      And I POST to /meetings
      And I set the following meeting info
      | organizer | subject                            | body | start                    | end                      | rooms       | attendees | optionalAttendees |
      | __USER1   | Create meeting to Test room status | Test | 2018-02-09T15:00:00.000Z | 2018-02-09T16:00:00.000Z | __USER_ROOM | __USER1   | __USER2           |
      And I send the request
      And I keep the "_id" as "after_item_id" from JSON response

  @bug @delete_item
  Scenario: Verify that is possible to retrieve free rooms
    When I GET to /rooms
      And I set the following params
      | from                     | to                       | status |
      | 2018-02-09T15:00:00.000Z | 2018-02-09T16:00:00.000Z | free   |
      And I send the request
    Then I should get a response with status code 200
      And I should get a collection with only free rooms

  @bug @delete_item
  Scenario: Verify that is possible to retrieve busy rooms
    When I GET to /rooms
      And I set the following params
      | from                     | to                       | status |
      | 2018-02-09T15:00:00.000Z | 2018-02-09T16:00:00.000Z | busy   |
      And I send the request
    Then I should get a response with status code 200
      And The response should be equal in data base rooms collection
      And The response should have a valid schema_room schema

  @delete_item
  Scenario: Verify that is possible to retrieve room by Id
    When I GET to /rooms
      And I have obtained rooms Id of the database
      And I send the request
    Then I should get a response with status code 200
      And The response should be equal in data base rooms collection
      And The response should have a valid schema_room schema