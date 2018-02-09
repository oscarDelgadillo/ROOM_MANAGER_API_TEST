@meetings @CRUD @put
Feature: PUT /meetings/{meetingId}

  Background: Create a meeting
    Given I POST to /meetings
    And I set the following body
         """
            {
               "organizer": "__USER_ADMINISTRATOR",
               "subject": "Scrum Test Meetings Admin",
               "body": "Test meeting",
               "start": "2018-04-21T20:00:00.000Z",
               "end": "2018-05-02T20:09:17.000Z",
               "rooms": [
                 "__USER_ROOM"
               ],
               "attendees": [],
               "optionalAttendees": []
            }
          """
    And I send '__CREDENTIALS_ADMINISTRATOR' as credentials
    And I send the request
    And I keep the "id" as "$id_meeting" from the previous step

  Scenario Outline: : Updating an existing meeting

    When I PUT to /meetings
    And I set the following body
         """
            {
               "organizer": <__USER>,
               "subject":<_subject>,
               "body":<_body>,
               "start":<_start>,
               "end": <_end>,
               "rooms":<_rooms>,
               "attendees":<_attendees>,
               "optionalAttendees":<_optional_attendees>
            }
          """
    And I send '__CREDENTIALS_ADMINISTRATOR' as credentials
    And I send the request update
    Then I should get a response with status code 400
    Examples:
      | __USER                 | _subject                    | _body          | _start                     | _end                       | _rooms        | _attendees | _optional_attendees |
      | "__USER_ADMINISTRATOR" | "Scrum Test Meetings Admin" | "Test meeting" | "2017-04-21T20:00:00.000Z" | "2018-05-02T20:09:17.000Z" | "__USER_ROOM" | []         | null                |
      | "__USER_ADMINISTRATOR" | "Scrum Test Meetings Admin" | "Test meeting" | "2017-04-21T20:00:00.000Z" | "2018-05-02T20:09:17.000Z" | "__USER_ROOM" | null       | []                  |
      | "__USER_ADMINISTRATOR" | "Scrum Test Meetings Admin" | "Test meeting" | "2017-04-21T20:00:00.000Z" | "2018-05-02T20:09:17.000Z" | null          | []         | []                  |
      | "__USER_ADMINISTRATOR" | "Scrum Test Meetings Admin" | "Test meeting" | "2017-04-21T20:00:00.000Z" | null                       | "__USER_ROOM" | []         | []                  |
      | "__USER_ADMINISTRATOR" | "Scrum Test Meetings Admin" | "Test meeting" | null                       | "2018-05-02T20:09:17.000Z" | "__USER_ROOM" | []         | []                  |
      | "__USER_ADMINISTRATOR" | "Scrum Test Meetings Admin" | null           | "2017-04-21T20:00:00.000Z" | "2018-05-02T20:09:17.000Z" | "__USER_ROOM" | []         | []                  |
      | "__USER_ADMINISTRATOR" | null                        | "Test meeting" | "2017-04-21T20:00:00.000Z" | "2018-05-02T20:09:17.000Z" | "__USER_ROOM" | []         | []                  |
      | null                   | "Scrum Test Meetings Admin" | "Test meeting" | "2017-04-21T20:00:00.000Z" | "2018-05-02T20:09:17.000Z" | "__USER_ROOM" | []         | []                  |